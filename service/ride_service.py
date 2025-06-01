from model.ride_status import RideStatus
from model.ride import Ride
from strategy.fare_calculation_strategy import FareCalculationStrategy
from observer.notification_service import NotificationService

class RideService:
    def __init__(self):
        self.available_drivers = []
        self.rides = {}
        self.fare_strategy = FareCalculationStrategy()
        self.notification_service = NotificationService()

    def register_driver(self, driver):
        self.available_drivers.append(driver)

    def book_ride(self, rider, destination):
        if not self.available_drivers:
            print("❌ No available drivers.")
            return None

        driver = self.available_drivers.pop(0)
        ride = Ride(rider, driver, rider.current_location, destination)
        self.rides[str(ride.id)] = ride
        self.notification_service.notify_driver(driver, f"You have a new ride with {rider.name}")
        return ride

    def complete_ride(self, ride_id):
        ride = self.rides.get(ride_id)
        if not ride:
            print("❌ Ride not found.")
            return

        ride.status = RideStatus.COMPLETED
        ride.fare = self.fare_strategy.calculate_fare(ride.source, ride.destination)
        print(f"✅ Ride completed. Fare: ₹{ride.fare}")

    def get_all_rides(self):
        return list(self.rides.values())
