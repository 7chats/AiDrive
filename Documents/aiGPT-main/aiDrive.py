class AiDrivenVehicle:
    def __init__(self, vehicleType, maxSpeed):
        self.vehicleType = vehicleType
        self.maxSpeed = maxSpeed

    def aiDrive(self, speed):
        if speed > self.maxSpeed:
            print(f"Warning: Cannot drive at {speed} km/h. Maximum speed for this {self.vehicleType} is {self.maxSpeed} km/h.")
            speed = self.maxSpeed

        print(f"Driving {self.vehicleType} at {speed} km/h using AI control system.")

def main():
    vehicleType = "car"
    maxSpeed = 120
    desiredSpeed = 80

    myVehicle = AiDrivenVehicle(vehicleType, maxSpeed)
    myVehicle.aiDrive(desiredSpeed)

if __name__ == "__main__":
    main()

"""
Driving car at 80 km/h using AI control system.
"""
