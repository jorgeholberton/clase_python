"""test for Car class."""

import pytest
from clase_python.model.car import Car

class TestCar2:
    
    def test_door_modified(self,car):  
        """assert verifica un booleano """
       
        car.doors(3)
        assert car.door_quantity == 3
            
        car.doors(5)
        assert car.door_quantity == 5
            
        car.doors(9)
        assert car.door_quantity == 3 
       
    
    
    @pytest.mark.parametrize(
        "a,b", 
    [
        (3,3),
        (5,5),
        (7,3)
    ]
    )
    def test_door_quantity_parametrize(self,car_2,a,b):
      
            car_2.doors(a)
            assert car_2.door_quantity==b
       