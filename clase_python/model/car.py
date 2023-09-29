from clase_python.core.abcs.vehicle_abcs import Vehicle
#from core.abcs.vehicle_abcs import Vehicle
""" variable global """
MAX_DISTANCE_CAN_TRAVEL=5 
AVAILABLE_CAR_BRANDS=["NISSAN","TOYOTA","BMW"]
MIN_DOOR_QUANTITY=3
MAX_DOOR_QUANTITY=6

class Car(Vehicle):
    """ constructor """
    def __init__(self,brand:str,model:int,door_quantity:int) -> None:
        
        self._brand=brand
        self._model=model
        self._door_quantity=door_quantity
        self._distance_traveled=0
       
   
    def move(self, additional_distance) -> int:
        if additional_distance <= MAX_DISTANCE_CAN_TRAVEL:
            self._distance_traveled += additional_distance
        else:
            self._distance_traveled += MAX_DISTANCE_CAN_TRAVEL
        return min(self._distance_traveled, MAX_DISTANCE_CAN_TRAVEL)
    
    def doors(self, additional_door: int) -> None:
        if additional_door >= MIN_DOOR_QUANTITY and additional_door <= MAX_DOOR_QUANTITY :
            self._door_quantity =additional_door
        else:
            self._door_quantity = MIN_DOOR_QUANTITY
        
      
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self,brand):
        if brand in AVAILABLE_CAR_BRANDS:
            self._brand=brand
        else:
            print("Ingrese una marca valida")
            
    """ igual que los getters  """        
    @property 
    def distance_traveled(self):
        return self._distance_traveled
    
    @distance_traveled.setter
    def distance_traveled(self,distance_traveled):
            self._distance_traveled = distance_traveled
            
    
    ##igual que los getters   doors      
    @property 
    def door_quantity(self):
        return self._door_quantity
    
    @door_quantity.setter
    def door_quantity(self,door_quantity):
            self._door_quantity = door_quantity