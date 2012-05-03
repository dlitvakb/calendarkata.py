class Calendario(object):
    def __init__(self):
        self.reglas_de_feriados = []

    def es_laborable(self, una_fecha):
        for regla in self.reglas_de_feriados:
            if regla.es_no_laborable(una_fecha):
                return False
        return True

    def agregar_fecha_no_laborable(self, una_regla):
        self.reglas_de_feriados.append(una_regla)

class FechaNoLaborable(object):
    def __init__(self, una_fecha):
        self.fecha = una_fecha

    def es_no_laborable(self, otra_fecha):
        return self.fecha == otra_fecha

class DiaNoLaborable(object):
    def __init__(self, un_dia):
        self.fecha = { "monday": 1,
                       "tuesday": 2,
                       "wednesday": 3,
                       "thursday": 4,
                       "friday": 5,
                       "saturday": 6,
                       "sunday": 7
                     }[un_dia]

    def es_no_laborable(self, una_fecha):
        return self.fecha == una_fecha.isoweekday()

class ReglaExpirable(object):
    def __init__(self, desde, hasta, regla):
        self.desde = desde
        self.hasta = hasta
        self.regla = regla

    def es_no_laborable(self, una_fecha):
        if self.desde <= una_fecha <= self.hasta:
            return self.regla.es_no_laborable(una_fecha)
        return False

