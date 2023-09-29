from model.car import Car

def main():
    carro1: Car = Car("NISSAN",2020,4);
    carro2: Car = Car("BMW",2024,20);
    carro3: Car = Car("BMW",2024,20);
    
    carro1.move(4)
    carro2.move(10)
    print("Marca: ",carro1.brand,"Distancia recorrida: ",carro1.distance_traveled)
    print("Marca: ",carro2.brand,"Distancia recorrida: ",carro2.distance_traveled)
    
    carro3.doors(8)
    print("Cantidad Puertas: ",carro3.door_quantity)
    
if __name__ == "__main__":
    main()