import uuid
from .ride_status import RideStatus

class Ride:
    def __init__(self, rider, driver, source, destination):
        self.id = uuid.uuid4()
        self.rider = rider
        self.driver = driver
        self.source = source
        self.destination = destination
        self.status = RideStatus.ONGOING
        self.fare = 0.0
