"""HybridFactory module."""

import math
import random


class HybridFactory:
    """Small run_factory helper."""

    def __init__(self, seed: int = 54) -> None:
        self._state = seed
        self._items: list[int] = []

    def run_factory(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 54) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 54


def main() -> None:
    obj = HybridFactory()
    print(obj.run_factory(54))


if __name__ == "__main__":
    main()
