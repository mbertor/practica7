__author__ = 'Raul'


class Empresa():
    """
    Representa una empresa
    """
    def __init__(self, nombre_empresa, cif, razon_social):
        """
        Constructor de una empresa

        Constructor al que se le pase como argumentos nombre_empresa, cif y razon_social. El constructor  inicializa una lista de departamentos a un valor vacio.
        :param nombre_empresa: Nombre de la empresa
        :param cif: Cif de la empresa
        :param razon_social: Razon social de la empresa
        :return:
        """
        self.nombre = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.lista_dpt = []