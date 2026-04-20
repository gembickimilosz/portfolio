class Car:
    def __init__(self):
        # Nested dictionary of cars
        self.cars = {
            'Car1': {'make': 'Toyota', 'model': 'Corolla', 'year': 2020, 'color': 'Blue', 'engine': 'Hybrid'},
            'Car2': {'make': 'Tesla', 'model': 'Model 3', 'year': 2022, 'color': 'White', 'engine': 'Electric'},
            'Car3': {'make': 'Ford', 'model': 'Mustang', 'year': 2019, 'color': 'Red', 'engine': 'Petrol'}
        }

    def show_all_items(self):
        print("Showing all car items:")
        for key, value in self.cars.items():
            print(f"{key}: {value}")

    def show_all_keys(self):
        print("Showing all car keys:")
        for key in self.cars.keys():
            print(key)

    def show_all_values(self):
        print("Showing all car values:")
        for value in self.cars.values():
            print(value)

# Test the Car class

if __name__ == "__main__":
    car_data = Car()

    print("Car Dictionary Example\n")
    
    car_data.show_all_keys()
    print("\n-----------------------------\n")
    
    car_data.show_all_values()
    print("\n-----------------------------\n")
    
    car_data.show_all_items()