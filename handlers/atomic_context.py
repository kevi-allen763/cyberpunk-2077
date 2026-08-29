"""SharedLoader module."""

import math
import random


class SharedLoader:
    """Small parse_adapter helper."""

    def __init__(self, seed: int = 74) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_adapter(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 74) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 74


def main() -> None:
    obj = SharedLoader()
    print(obj.parse_adapter(74))


if __name__ == "__main__":
    main()
