from src.entities.values.employee import Employee
from src.use_cases.employee_saver.values.employee_dto import EmployeeDTO
from src.use_cases.employee_saver.values.response_dto import ResponseDTO


class EmployeeSaverUseCase:
    def __init__(self, employee_saver_repository):
        self.employee_saver_repository = employee_saver_repository

    def execute(self, employee_dto: EmployeeDTO) -> ResponseDTO:
        def save_to_repository(_employee_dto: EmployeeDTO) -> None:
            def __map_dto_to_employee(__employee_dto: EmployeeDTO) -> Employee:
                return Employee(
                    first_name=__employee_dto.first_name,
                    last_name=__employee_dto.last_name,
                )

            def __save(__employee: Employee) -> None:
                self.employee_saver_repository.save(__employee)

            employee: Employee = __map_dto_to_employee(_employee_dto)
            __save(employee)

        try:
            save_to_repository(employee_dto)
            return ResponseDTO(executed=True, exception_occurred=False)

        except Exception:
            return ResponseDTO(executed=False, exception_occurred=True)
