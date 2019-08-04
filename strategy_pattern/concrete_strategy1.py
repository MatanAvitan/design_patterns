from strategy_pattern.strategy import Strategy


class ConcreteStrategy1(Strategy):

    def algorithm_interface(self):
        print('algorithm one')
