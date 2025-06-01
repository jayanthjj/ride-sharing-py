class RideController:
    def __init__(self, ride_service):
        self.ride_service = ride_service

    def register_driver(self, name, lat, lng):
        from model.location import Location
        from model.driver import Driver
        driver = Driver(name, Location(lat, lng))
        self.ride_service.register_driver(driver)

    def book_ride(self, name, lat, lng, drop_lat, drop_lng):
        from model.location import Location
        from model.rider import Rider
        rider = Rider(name, Location(lat, lng))
        destination = Location(drop_lat, drop_lng)
        ride = self.ride_service.book_ride(rider, destination)
        if ride:
            print(f"🚕 Ride booked with ID: {ride.id}")
            return ride.id
        return None

    def complete_ride(self, ride_id):
        self.ride_service.complete_ride(ride_id)

    def print_history(self):
        rides = self.ride_service.get_all_rides()
        for r in rides:
            print(f"📘 Ride {r.id}: {r.status.name}, Fare: ₹{r.fare}")
