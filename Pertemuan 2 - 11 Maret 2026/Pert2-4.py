from access_modifiers import privatemethod
from typing import Final

class _ObjekTunggal:
    def lakukan_sesuatu(self):
        print("Objek tunggal sednag melakukan sesuatu")

class ObjekTunggal:
    __instan: Final[_ObjekTunggal] = _ObjekTunggal()
    @privatemethod
    def __init__(self):
        pass

    @staticmethod
    def dapatkan_instan():
        return ObjekTunggal.__instan

instan_tunggal = ObjekTunggal.dapatkan_instan()
instan_tunggal.lakukan_sesuatu()