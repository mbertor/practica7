import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest import TestCase

from mockito import *

from src.Departamento import *
from src.Empleado import *


__author__ = 'Raul'


class TestDepartamento(TestCase):
    """
    Implementacion tests para la clase departamento.
    """

    def test_get_salario_total(self):
        """
        Test unitario sobre el metodo get_salario_total de la clase departamento

        Comprueba el buen funcionamiento de la funcion utilizando objetos simulados de la clase empleado

        :return:
        """
        empleado1 = mock(Empleado)
        when(empleado1).get_salario().thenReturn(1000)

        empleado2 = mock(Empleado)
        when(empleado2).get_salario().thenReturn(2000)

        empleado3 = mock(Empleado)
        when(empleado3).get_salario().thenReturn(1000)

        departamento = Departamento('Calidad', 1)
        departamento.aniadir_empleado(empleado1)
        departamento.aniadir_empleado(empleado2)
        departamento.aniadir_empleado(empleado3)
        self.assertEqual(departamento.get_salario_total(), 4000)


    def test_salario_total_mensual(self):
        """
        Test unitario sobre el metodo get_salario_total_mensual de la clase departamento

        Comprueba el buen funcionamiento de la funcion utilizando objetos simulados de la clase empleado
        :return:
        """
        empleado1 = mock(Empleado)
        when(empleado1).get_salario_mensual().thenReturn(1000)

        empleado2 = mock(Empleado)
        when(empleado2).get_salario_mensual().thenReturn(2000)

        empleado3 = mock(Empleado)
        when(empleado3).get_salario_mensual().thenReturn(1000)

        departamento = Departamento('Calidad', 1)
        departamento.aniadir_empleado(empleado1)
        departamento.aniadir_empleado(empleado2)
        departamento.aniadir_empleado(empleado3)
        self.assertEqual(departamento.salario_total_mensual(), 4000)