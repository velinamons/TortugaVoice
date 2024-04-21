class Genius:
    def __int__(self):
        self._memory = -1

    def get_memory(self):
        return self._memory

    def set_memory(self, number: int) -> None:
        self._memory = number

new_genius = Genius()
print(new_genius.get_memory())
print(new_genius.set_memory(5))