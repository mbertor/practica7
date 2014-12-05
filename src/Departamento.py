__author__ = 'Raul'


class Departamento():
    """
    Esta clase representa un departamento
    """

    def __init__(self, nombre, id):
        """
        Constructor departamento
        Crea  un departamento con los argumentos dados.

        :param nombre: nombre del departamento
        :param id: id del departamento
        :return: nuevo departamento
        """
        self.nombre_depto= nombre
        self.id_depto= id
        self.lista= []

    def aniadir_empleado(self,empleado):
        """
        Anyade un empleado al departamento
        Incorpora un empleado a la lista de empleados de un departamento

        :param empleado: empleado a anyadir
        """
        self.lista.append(empleado)

    def get_salario_total(self):
        """
        Calcula el salario total de todos los empleados
        que componen el departamento

         :return:int
        """
        num=0
        for i in self.lista:
             num += i.get_salario()
        return num

    def get_nombre_depto(self):
        """
        Devuelve el nombre del departamento
        :return:string
        """
        return self.nombre_depto

    def salario_total_mensual(self):
        """
        Calcula el salario total de todos los empleados que componen el departamento

        :return:int
        """
        num = 0
        for i in self.lista:
            num += i.get_salario_mensual()
        return num