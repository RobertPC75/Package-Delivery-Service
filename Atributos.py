# Auto detect text files and perform LF normalization
class Package:
    def __init__(self, code, peso, costo_por_gramo, descripcion):
        self.code = code
        self.peso = max(0, peso)
        self.costo_por_gramo = max(0, costo_por_gramo)
        self.descripcion = descripcion

    def calcular(self):
        return self.peso * self.costo_por_gramo


class StandardPackage(Package):
    def __init__(self, code, peso, costo_por_gramo, descripcion, cuota_entrega_dos_dias):
        super().__init__(code, peso, costo_por_gramo, descripcion)
        self.cuota_entrega_dos_dias = cuota_entrega_dos_dias

    def calcular(self):
        return super().calcular() + self.cuota_entrega_dos_dias


class OverweightPackage(Package):
    def __init__(self, code, peso, costo_por_gramo, descripcion, costo_por_sobrepeso):
        super().__init__(code, peso, costo_por_gramo, descripcion)
        self.costo_por_sobrepeso = costo_por_sobrepeso

    def calcular(self):
        if self.peso <= 1000:
            return super().calcular()
        else:
            costo_sobrepeso = (self.peso - 1000) * self.costo_por_sobrepeso
            return super().calcular() + costo_sobrepeso
