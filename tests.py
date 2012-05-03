import unittest
from datetime import datetime

from calendario import Calendario
from calendario import FechaNoLaborable
from calendario import DiaNoLaborable
from calendario import ReglaExpirable

class TestXXX(unittest.TestCase):
    def test_puedo_agregar_una_fecha_no_laborable(self):
        calendario = Calendario()
        calendario.agregar_fecha_no_laborable(
          FechaNoLaborable(datetime(2012,1,1))
        )

        self.assertTrue(calendario.es_laborable(datetime(2012,06,30)))
        self.assertFalse(calendario.es_laborable(datetime(2012,1,1)))

    def test_puedo_agregar_mas_de_una_fecha_no_laborable(self):
        calendario = Calendario()
        calendario.agregar_fecha_no_laborable(
          FechaNoLaborable(datetime(2012,1,1))
        )
        calendario.agregar_fecha_no_laborable(
          FechaNoLaborable(datetime(2012,3,21))
        )
        calendario.agregar_fecha_no_laborable(
          FechaNoLaborable(datetime(2012,7,14))
        )
        calendario.agregar_fecha_no_laborable(
          FechaNoLaborable(datetime(2012,6,30))
        )

        self.assertFalse(calendario.es_laborable(datetime(2012,06,30)))
        self.assertFalse(calendario.es_laborable(datetime(2012,03,21)))
        self.assertFalse(calendario.es_laborable(datetime(2012,07,14)))
        self.assertFalse(calendario.es_laborable(datetime(2012,1,1)))

        self.assertTrue(calendario.es_laborable(datetime(2012,1,2)))
        self.assertTrue(calendario.es_laborable(datetime(2012,2,24)))
        self.assertTrue(calendario.es_laborable(datetime(2012,7,1)))
        self.assertTrue(calendario.es_laborable(datetime(2012,3,1)))

    def test_puedo_decir_que_un_dia_de_todas_las_semanas_es_no_laborable(self):
        calendario = Calendario()
        calendario.agregar_fecha_no_laborable(DiaNoLaborable("sunday"))
        calendario.agregar_fecha_no_laborable(DiaNoLaborable("monday"))

        self.assertFalse(calendario.es_laborable(datetime(2012,05,13)))
        self.assertFalse(calendario.es_laborable(datetime(2012,05,14)))

    def test_puedo_mezclar_fechas_exactas_y_dias_de_la_semana(self):
        calendario = Calendario()

        calendario.agregar_fecha_no_laborable(DiaNoLaborable("sunday"))
        calendario.agregar_fecha_no_laborable(DiaNoLaborable("monday"))
        calendario.agregar_fecha_no_laborable(
          FechaNoLaborable(datetime(2012,1,1))
        )
        calendario.agregar_fecha_no_laborable(
          FechaNoLaborable(datetime(2012,3,21))
        )

        self.assertFalse(calendario.es_laborable(datetime(2012,03,21)))
        self.assertFalse(calendario.es_laborable(datetime(2012,1,1)))
        self.assertFalse(calendario.es_laborable(datetime(2012,05,13)))
        self.assertFalse(calendario.es_laborable(datetime(2012,05,14)))

        self.assertTrue(calendario.es_laborable(datetime(2012,2,24)))
        self.assertTrue(calendario.es_laborable(datetime(2012,7,3)))

    def test_regla_expirable(self):
        calendario = Calendario()

        calendario.agregar_fecha_no_laborable(
          ReglaExpirable(datetime(2012,02,10), datetime(2012,5,20),
            DiaNoLaborable("tuesday")
          )
        )

        self.assertFalse(calendario.es_laborable(datetime(2012,03,13)))
        self.assertTrue(calendario.es_laborable(datetime(2012,05,22)))
if __name__ == '__main__':
    unittest.main()
