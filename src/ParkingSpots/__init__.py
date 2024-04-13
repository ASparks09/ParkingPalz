# ParkingSpots.py

class ParkingSpot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spots = capacity

    def taken_spot(self):
        if self.available_spots > 0:
            self.available_spots -= 1
            print("Spot taken. Available spots: ", self.available_spots)
        else:
            print("No available spots")