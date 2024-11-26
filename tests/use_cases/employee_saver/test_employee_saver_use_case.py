from unittest.mock import MagicMock

import pytest

from src.entities.values.employee import Employee
from src.use_cases.employee_saver.dependencies.employee_saver_repository_interface import (
    EmployeeSaverRepositoryInterface,
)
from src.use_cases.employee_saver.use_case import EmployeeSaverUseCase
from src.use_cases.employee_saver.values.employee_dto import EmployeeDTO
from src.use_cases.employee_saver.values.response_dto import ResponseDTO
from tests.use_cases.employee_saver.mocks.employee_saver_repository import (
    create_employee_saver_repository_with_exception_on_saving,
)


def test_exception_response_on_repository_exception():
    employee: EmployeeDTO = EmployeeDTO(first_name="first name", last_name="last name")
    employee_saver_repository: EmployeeSaverRepositoryInterface = (
        create_employee_saver_repository_with_exception_on_saving()
    )

    employee_saver_use_case = EmployeeSaverUseCase(employee_saver_repository)
    actual_response = employee_saver_use_case.execute(employee)
    expected_response = ResponseDTO(executed=False, exception_occurred=True)
    assert actual_response == expected_response


def test_delegating_saving_to_repository():
    employee: EmployeeDTO = EmployeeDTO(first_name="first name", last_name="last name")
    employee_saver_repository: EmployeeSaverRepositoryInterface = MagicMock(
        spec=EmployeeSaverRepositoryInterface
    )
    employee_saver_repository.save = MagicMock()
    employee_saver_use_case = EmployeeSaverUseCase(employee_saver_repository)
    employee_saver_use_case.execute(employee)
    employee_saver_repository.save.assert_called_once()


@pytest.mark.parametrize(
    "employee_dto, employee",
    [
        (
            EmployeeDTO(first_name="first name", last_name="last name"),
            Employee(first_name="first name", last_name="last name"),
        )
    ],
)
def test_saving_right_object(employee_dto, employee):
    employee_saver_repository: EmployeeSaverRepositoryInterface = MagicMock(
        spec=EmployeeSaverRepositoryInterface
    )
    employee_saver_repository.save = MagicMock()

    employee_saver_use_case = EmployeeSaverUseCase(employee_saver_repository)
    employee_saver_use_case.execute(employee_dto)
    employee_saver_repository.save.assert_called_with(employee)
