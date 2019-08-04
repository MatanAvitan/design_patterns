from builder_pattern.builder import Builder


class ConcreteBuilder1(Builder):
    def build_part_a(self):
        print('Building part a of Concrete Builder 1')

    def build_part_b(self):
        print('Building part b of Concrete Builder 1')

    def build_part_c(self):
        print('Building part c of Concrete Builder 1')
