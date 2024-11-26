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
    employee_dto: EmployeeDTO = EmployeeDTO(
        first_name="first name", last_name="last name"
    )
    employee_saver_repository: EmployeeSaverRepositoryInterface = (
        create_employee_saver_repository_with_exception_on_saving()
    )

    employee_saver_use_case = EmployeeSaverUseCase(employee_saver_repository)
    actual_response = employee_saver_use_case.execute(employee_dto)
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
            EmployeeDTO(first_name="first name 1", last_name="last name 1"),
            Employee(first_name="first name 1", last_name="last name 1"),
        ),
        (
            EmployeeDTO(first_name="first name 2", last_name="last name 2"),
            Employee(first_name="first name 2", last_name="last name 2"),
        ),
        (
            EmployeeDTO(first_name="first name 3", last_name="last name 3"),
            Employee(first_name="first name 3", last_name="last name 3"),
        ),
        (
            EmployeeDTO(first_name="first name 4", last_name="last name 4"),
            Employee(first_name="first name 4", last_name="last name 4"),
        ),
        (
            EmployeeDTO(first_name="first name 5", last_name="last name 5"),
            Employee(first_name="first name 5", last_name="last name 5"),
        ),
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


def test_successful_saving_return_success_response():
    employee_dto: EmployeeDTO = EmployeeDTO(
        first_name="first name", last_name="last name"
    )
    employee_saver_repository: EmployeeSaverRepositoryInterface = MagicMock(
        spec=EmployeeSaverRepositoryInterface
    )
    employee_saver_repository.save = MagicMock()

    employee_saver_use_case = EmployeeSaverUseCase(employee_saver_repository)
    actual_response = employee_saver_use_case.execute(employee_dto)
    expected_response = ResponseDTO(executed=True, exception_occurred=False)
    assert actual_response == expected_response
