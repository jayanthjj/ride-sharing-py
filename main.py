from service.ride_service import RideService
from controller.ride_controller import RideController

if __name__ == "__main__":
    ride_service = RideService()
    controller = RideController(ride_service)

    controller.register_driver("Arjun", 12.9611, 77.6387)
    ride_id = controller.book_ride("Ravi", 12.9716, 77.5946, 12.9250, 77.5938)
    if ride_id:
        controller.complete_ride(str(ride_id))
    controller.print_history()
