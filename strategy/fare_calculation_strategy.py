class FareCalculationStrategy:
    def calculate_fare(self, source, destination):
        distance = ((destination.latitude - source.latitude) ** 2 + (destination.longitude - source.longitude) ** 2) ** 0.5
        return 10 + distance * 50
