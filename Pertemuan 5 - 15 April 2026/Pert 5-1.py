from numbers import Number

class IntList:
    def __init__(self,*elements):
        self.__elements = elements

    def __getitem__[T: Number](self, index: T):
        if type(index) is int:
            return self.__elements[index]
        else:
            prev_element = self.__elements[int(index)]
            next_element = self.__elements[int(index) + 1]
            frac_index = float(index) % 1.0
            return int((prev_element + next_element) * frac_index)

daftar_bilangan = IntList(1, 6, 8, 10, 13)
print(f"Elemen indeks ke 1,5:{daftar_bilangan[1.5]}")
print(f"Element indeks ke 2:{daftar_bilangan[2]}")
