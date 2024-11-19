from unittest.mock import Mock, MagicMock

from src.use_cases.employee_saver.dependencies.employee_saver_repository_interface import \
    EmployeeSaverRepositoryInterface


def create_employee_saver_repository_with_exception_on_saving():
    employee_saver_repository: EmployeeSaverRepositoryInterface = MagicMock(
        spec=EmployeeSaverRepositoryInterface
    )
    employee_saver_repository.save = MagicMock(side_effect=Exception)
    return employee_saver_repository
