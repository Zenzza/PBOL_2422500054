from functools import cached_property

class LazyClass:
    @cached_property
    def value(self):
        print('Hello')
        return "World"

lazy = LazyClass()
nilai_lazy = lazy.value
for i in range(1,6):
    print(f"Nilai \"atribut malas\" pada iterasi ke-{i}: {nilai_lazy}")