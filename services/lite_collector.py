"""RemoteCollector module."""

import math
import random


class RemoteCollector:
    """Small render_builder helper."""

    def __init__(self, seed: int = 76) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_builder(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 76) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 76


def main() -> None:
    obj = RemoteCollector()
    print(obj.render_builder(76))


if __name__ == "__main__":
    main()
