from abc import ABC, abstractmethod


class Builder(ABC):
    def __init__(self, product):
        self.product = product

    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def build_part_c(self):
        pass
