from __future__ import annotations


class Genius:
    def __init__(self, memory: int | None = None):
        self._memory = memory

    @property
    def memory(self) -> int | None:
        return self._memory

    @memory.setter
    def memory(self, number: int) -> None:
        self._memory = number

    def clear(self) -> None:
        self._memory = 0


if __name__ == "__main__":
    new_genius = Genius(5)
    print(new_genius.memory)
    new_genius.memory = 5
    print(new_genius.memory)
    new_genius.clear()
    print(new_genius.memory)
