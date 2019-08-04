from strategy_pattern.concrete_strategy1 import ConcreteStrategy1
from strategy_pattern.context import Context

if __name__ == '__main__':
    # Example
    concrete_strategy1 = ConcreteStrategy1()
    context = Context(concrete_strategy1)
    context.strategy.algorithm_interface()
