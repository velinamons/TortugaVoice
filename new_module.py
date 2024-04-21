from __future__ import annotations

class Genius:
    def __init__(self, memory: int | None = None):
        self._memory = memory

    def get_memory(self) -> int | None:
        return self._memory

    def set_memory(self, number: int) -> None:
        self._memory = number

if __name__ == "__main__":
    new_genius = Genius(5)
    print(new_genius.get_memory())
    print(new_genius.set_memory(5))


