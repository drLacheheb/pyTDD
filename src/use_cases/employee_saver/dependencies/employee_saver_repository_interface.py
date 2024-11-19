from abc import ABCMeta, abstractmethod


class EmployeeSaverRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def save(self, employee):
        pass
