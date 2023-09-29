"""test for Car class."""

import pytest 

from clase_python.model.car import Car

""" agregamos un decorador fixture permite la entrada de datos """
"""fixture lo convierte en objeto a pasar a la prueba """

@pytest.fixture()
def car():
    return Car("BMW",2004,4) 


@pytest.fixture()
def car_1():
    return Car("BMW",2004,4)  

@pytest.fixture()
def car_2():
    return Car("BMW",2004,4) 



