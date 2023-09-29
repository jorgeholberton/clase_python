"""test for Car class."""

import pytest
from clase_python.model.car import MAX_DISTANCE_CAN_TRAVEL

#lo que entra a la prueba viene del archivo de configuración 
#recibe el objeto car
class TestCar:
    def test_move_distance_traveled_modified(self,car):  
        """assert verifica un booleano """
      
        car.move(4)
        assert car.distance_traveled == 4
            
        car.move(5)
        assert car.distance_traveled == 9
            
        car.move(6)
        assert car.distance_traveled == 14 
        
          
        
    @pytest.mark.parametrize(
        "a,b", 
    [
        (4,4),
        (5,5),
        (6,5)
    ]
    )
    def test_move_distance_traveled_parametrize(self,car_1,a,b):
       
            car_1.move(a)
            assert car_1.distance_traveled==b
       
        
        
    def test_move_max_distance(self, car_2):
   
        """ se mueve el carro a la distancia máxima 5"""
        max_distance = car_2.move(MAX_DISTANCE_CAN_TRAVEL)
    
        """ verificar si la distancia recorrida es igual a la distancia máxima permitida """
        assert max_distance == MAX_DISTANCE_CAN_TRAVEL
    
        """ Intentar mover el carro un poco más de la distancia permitida """
        """ debería moverse solo MAX_DISTANCE_CAN_TRAVEL  """
        exceeded_distance = car_2.move(MAX_DISTANCE_CAN_TRAVEL + 1)
        
        """ verificar si la distancia recorrida todavía es igual a la distancia máxima """
        assert exceeded_distance == MAX_DISTANCE_CAN_TRAVEL
    



        
        
        
        
        
        
        
            
   
            
    
    
   

