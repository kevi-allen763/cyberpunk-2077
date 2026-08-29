"""StreamParser module."""

import math
import random


class StreamParser:
    """Small parse_context helper."""

    def __init__(self, seed: int = 96) -> None:
        self._state = seed
        self._items: list[int] = []

    def parse_context(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 96) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 96


def main() -> None:
    obj = StreamParser()
    print(obj.parse_context(96))


if __name__ == "__main__":
    main()
