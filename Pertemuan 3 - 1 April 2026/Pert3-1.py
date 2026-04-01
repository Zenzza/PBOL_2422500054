from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def cetak(self):
        pass

class PrinterKekinian:
    def mulai_cetak(self):
        print("Yo, Hello all. Waddap!!!")

class AdapterPrinterKekinian(Printer):
    def __init__(self, printer):
        self.__printer = printer

    def cetak(self):
        self.__printer.mulai_cetak()

printer_kekinian = PrinterKekinian()
printer_warisan = AdapterPrinterKekinian(printer_kekinian)
printer_warisan.cetak()