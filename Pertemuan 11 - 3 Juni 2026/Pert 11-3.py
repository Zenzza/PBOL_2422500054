from warnings import warn

class ClassSaya:
    nilai_baru:int

    warn("Gunakan 'nilai_baru' sebagai gantinya", DeprecationWarning)

    @property
    def nilai_lama (self):
        return

    @nilai_lama.setter
    def nilai_lama(self, value):
        self.nilai_baru = value

classku = ClassSaya()
classku.nilai_lama = 42
print(classku.nilai_baru)