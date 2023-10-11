class ParkingLot:
    def __init__(self):
        self.levels = {
            'A': {i: None for i in range(1, 21)},
            'B': {i: None for i in range(21, 41)}
        }

    def park_vehicle(self, vehicle_number):
        for level, parking_spaces in self.levels.items():
            for spot, vehicle in parking_spaces.items():
                if vehicle is None:
                    parking_spaces[spot] = vehicle_number
                    return {'level': level, 'spot': spot}
        return "Parking lot is full"

    def retrieve_parking_spot(self, vehicle_number):
        for level, parking_spaces in self.levels.items():
            for spot, vehicle in parking_spaces.items():
                if vehicle == vehicle_number:
                    return {'level': level, 'spot': spot}
        return "Vehicle not found"



parking_lot = ParkingLot()

# Park a vehicle print spot
print(parking_lot.park_vehicle('DL1'))
print(parking_lot.park_vehicle('UP1'))

# Retrieve spot of vehicle
print(parking_lot.retrieve_parking_spot('DL1'))

# Retrieve spot of vehicle that dont exist
print(parking_lot.retrieve_parking_spot('HR3'))