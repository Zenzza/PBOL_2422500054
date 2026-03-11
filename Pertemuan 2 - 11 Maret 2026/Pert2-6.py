from dataclasses import dataclass

@dataclass
class Komputer:
    processor: str
    ram: str
    penyimpanan: str
    kartu_grafis: str

komputer_biasa = Komputer(
    processor="Intel Core i5",
    ram="16GB DDR4",
    penyimpanan="512 GB SSD",
    kartu_grafis="NVIDIA GTX 1060"
)

print("Spesifikasi Komputer Kerja Saya:")
print(f"""Processor: {komputer_biasa.processor}
RAM: {komputer_biasa.ram}
Penyimpanan: {komputer_biasa.penyimpanan}
Kartu Grafis: {komputer_biasa.kartu_grafis}""")