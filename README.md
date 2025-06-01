# Rideshare Application

A Python-based low-level design implementation of a rideshare service, demonstrating object-oriented design principles and common design patterns.

## Project Overview

This application simulates a basic rideshare platform where:
- Drivers can register themselves
- Riders can book rides
- Rides can be completed with fare calculation
- Notifications are sent to drivers

## Architecture and Design Patterns

The project implements several design patterns:

1. **MVC Architecture**
   - **Model**: Data objects like Ride, Rider, Driver, Location
   - **Controller**: RideController handling user interactions
   - **Service**: RideService managing business logic

2. **Observer Pattern**
   - NotificationService observes ride events and notifies drivers

3. **Strategy Pattern**
   - FareCalculationStrategy for calculating ride fares

## Project Structure

```
rideshare_lld_py/
├── main.py                     # Application entry point
├── controller/
│   └── ride_controller.py      # Handles user requests
├── model/
│   ├── driver.py               # Driver entity
│   ├── location.py             # Location representation
│   ├── ride_status.py          # Enum for ride status
│   ├── ride.py                 # Ride entity
│   └── rider.py                # Rider entity
├── observer/
│   └── notification_service.py # Notification system
├── service/
│   └── ride_service.py         # Core business logic
└── strategy/
    └── fare_calculation_strategy.py # Fare calculation algorithm
```

## Features

- Driver registration with current location
- Ride booking with source and destination
- Ride completion with fare calculation
- Ride history tracking
- Driver notifications

## Usage

Run the application using:

```bash
python main.py
```

The sample code in `main.py` demonstrates:
1. Registering a driver named "Arjun"
2. Booking a ride for "Ravi"
3. Completing the ride
4. Printing ride history

## Extending the Application

To extend this application, you could:

1. Add user authentication
2. Implement different fare calculation strategies
3. Add ride rating functionality
4. Implement ride cancellation
5. Add payment processing
6. Create a proper database integration

## Technical Details

- Uses UUID for generating unique ride IDs
- Implements enum for ride status management
- Calculates fare based on distance between coordinates
- Simulates notifications to drivers

## Requirements

- Python 3.x