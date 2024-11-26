from src.entities.values.employee import Employee
from src.use_cases.employee_saver.values.response_dto import ResponseDTO


class EmployeeSaverUseCase:
    def __init__(self, employee_saver_repository):
        self.employee_saver_repository = employee_saver_repository

    def execute(self, employee) -> ResponseDTO:
        try:
            self.employee_saver_repository.save(
                Employee(first_name=employee.first_name, last_name=employee.last_name)
            )

        except Exception:
            return ResponseDTO(executed=False, exception_occurred=True)
