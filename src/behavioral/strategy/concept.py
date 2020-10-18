from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    """The Strategy interface declares operations commom to all supported versions of
    some algorithm.

    The Context uses this interface to call the algotithm defined by Concrete Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: List) -> List:
        pass


class Context:
    """The Context defines the interface of interest to clients."""

    def __init__(self, strategy: Strategy) -> None:
        """Usually, the Context accepts a strategy through the constructor, but also
        provides a setter to change it at runtime."""
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work with
        all strategies via the Strategy interface."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """Usually, the Context allows replacing a Strategy object at runtime."""
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """The Context delegates some work to the Strategy object instead of implementing
        multiple versions of the algorithm on its own."""
        result = self._strategy.do_algorithm(['a', 'b', 'c'])
        print(result)


class ConcreteStrategyA(Strategy):
    """Concrete Strategies implement the algotithm while following the base Strategy
    interface. The interface makes them interchangeable in the Context."""

    def do_algorithm(self, data: List) -> List:
        print('sorting list...')
        return sorted(data)


class ConcreteStrategyB(Strategy):

    def do_algorithm(self, data: List) -> List:
        print('reversing and sorting list...')
        return list(reversed(sorted(data)))


def main() -> None:
    # The client code picks a concrete strategy and passes it to the context.
    # It should be aware of the differences between strategies in order to make the right choice.
    context = Context(ConcreteStrategyA())
    context.do_some_business_logic()

    # The context can change the Strategy in runtime.
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()


if __name__ == '__main__':
    main()
