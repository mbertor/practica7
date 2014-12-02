__author__ = 'Raul'

class Empleado():
    """
    Esta clase representa un empleado
    """

    def __init__(self,nombre,apellidos,dni,direccion,edad,email,salario):


            self.nom= nombre
            self.nom2 = apellidos
            self.dni = dni
            self.direc = direccion
            self.edad = edad
            self.mail = email
            self.sal = float(salario)

    def get_salario(self):
        """
        Devuelve el salario del empleado
        :return:int
        """
        return self.sal

    def get_dni(self):
        """
        Devuelve el dni del empleado
        :return:int
        """
        return self.dni

    def get_nombre_apellidos(self):
        """
        Devuelve el nombre y los apellidos de un empleado

        Devuelva de forma concatenada en un solo string el nombre y los apellidos del empleado.

        :return:
        """
        return self.nom + ' ' + self.nom2

    def get_edad(self):
        """
        Devuelve la edad de un empleado
        :return:int
        """
        return self.edad

    def get_email(self):
        """
        Devuelve el email de un empleado
        :return:string
        """
        return self.mail

    def get_direccion(self):
        """
        Devuelve la direccion de un empleado
        :return:string
        """
        return self.direc

    def get_salario_mensual(self):
        """
        Devuelve salario mensual de un empleado asumiendo 12 pagas
        :return:int
        """
        num=self.get_salario()/12
        return num
