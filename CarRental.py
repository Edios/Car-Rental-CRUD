import json
from dataclasses import dataclass, field, asdict


@dataclass
class Car:
    """
    Definition of Car object
    """
    Id: int
    Manufacturer: str
    Model: str
    DateOfProduction: int
    Mileage: int

    def __str__(self):
        return f"Car with ID {self.Id}: {self.Manufacturer}, {self.Model} \n" \
               f"-Date Of Production: {self.DateOfProduction}, Mileage: {self.Mileage}"


@dataclass
class CarRental:
    """
    Definition of Car rental. Require name on creation.
    """
    Name: str
    CarCollection: list = field(default_factory=lambda: [])

    def AddCar(self, car: Car) -> int:
        """
        Create an instance of car to car collection
        :param car: Definition of Car Object
        :return:id
        """
        self.CarCollection.append(car)
        return car.Id

    def RemoveCar(self, id: int) -> bool:
        """
        Remove Car instance from Car list based on id
        :param id:
        :return:state of operation
        """
        for position, car in enumerate(self.CarCollection):
            if id==car.Id:
                self.CarCollection.remove(self.CarCollection[position])
                return True
        return False

    def ShowCar(self, *args: int):
        """
        Print Cars Collection on the screen.
        :param args: ID of car in database
        :return: Return list of cars from actual Car Collection list based on ID criteria
        """
        CarToShow = []
        if not args:
            for car in self.CarCollection:
                CarToShow = self.CarCollection
                print(car)
        for arg in args:
            for car in self.CarCollection:
                if arg == car.Id:
                    print(car)
                    CarToShow.append(car)
        return CarToShow

    def deserialize(self, data)->None:
        """
        Take car data and append it to car collection
        :param data:
        :return: None
        """
        self.CarCollection.append(Car(**data))

    def serialize(self, id:int,filename:str):
        """
        Serialize Car data to json file
        :param id: Car ID
        :param filename: Name of output file
        :return: None
        """
        for car in self.CarCollection:
            if id==car.Id:
                data=asdict(car)
                with open(filename,"w") as file:
                    file.write(json.dumps(data))

if __name__ == "__main__":
    rental = CarRental('Car Rental Gdansk')
    rental.AddCar(Car(0, "Skoda", "Fabia", 2005, 150000))
    rental.AddCar(Car(1, "Peugot", "Boxer", 2021, 70000))
    rental.AddCar(Car(2, "Opel", "Omega", 2021, 100))
    rental.AddCar(Car(3, "Volvo", "XC90", 2017, 100000))
    rental.RemoveCar(2)
    print('All car list:')
    rental.ShowCar()
    print('Concrete car list: ')
    rental.ShowCar(1,3)
    with open('carlist.json','r') as file:
        data=json.load(file)
        rental.deserialize(data)
    rental.ShowCar()
    rental.serialize(3,'serialized_data.json')