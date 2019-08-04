from builder_pattern.product import Product
from builder_pattern.concrete_builder1 import ConcreteBuilder1
from builder_pattern.director import Director

if __name__ == '__main__':
    product = Product()
    concrete_builder1 = ConcreteBuilder1(product)
    director = Director(concrete_builder1)
    director.construct()
    # The final product is director.builder.product
