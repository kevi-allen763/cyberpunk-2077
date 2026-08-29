"""SmartRouter module."""

import math
import random


class SmartRouter:
    """Small collect_session helper."""

    def __init__(self, seed: int = 66) -> None:
        self._state = seed
        self._items: list[int] = []

    def collect_session(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 66) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 66


def main() -> None:
    obj = SmartRouter()
    print(obj.collect_session(66))


if __name__ == "__main__":
    main()
