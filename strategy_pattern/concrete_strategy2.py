from strategy_pattern.strategy import Strategy


class ConcreteStrategy2(Strategy):

    def algorithm_interface(self):
        print('algorithm two')
