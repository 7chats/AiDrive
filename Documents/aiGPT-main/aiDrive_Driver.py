
from aiDrive import AiDrivenVehicle

def main():
    vehicleType = "car"
    maxSpeed = 120
    desiredSpeed = 80

    myVehicle = AiDrivenVehicle(vehicleType, maxSpeed)
    myVehicle.aiDrive(desiredSpeed)

if __name__ == "__main__":
    main()
