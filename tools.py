import json
from typing import Dict

def get_flight_times(departure: str, arrival: str) -> str:
  flights: Dict[str, Dict[str, str]] = {
    'NYC-LAX': {'departure': '08:00 AM', 'arrival': '11:30 AM', 'duration': '5h 30m'},
    'LAX-NYC': {'departure': '02:00 PM', 'arrival': '10:30 PM', 'duration': '5h 30m'},
    'LHR-JFK': {'departure': '10:00 AM', 'arrival': '01:00 PM', 'duration': '8h 00m'},
    'JFK-LHR': {'departure': '09:00 PM', 'arrival': '09:00 AM', 'duration': '7h 00m'},
    'CDG-DXB': {'departure': '11:00 AM', 'arrival': '08:00 PM', 'duration': '6h 00m'},
    'DXB-CDG': {'departure': '03:00 AM', 'arrival': '07:30 AM', 'duration': '7h 30m'},
  }

  key = f'{departure}-{arrival}'.upper()
  return json.dumps(flights.get(key, {'error': 'Flight not found'}))

def add_numbers(a: int, b: int) -> str:
  return str(int(a) + int(b))

functions = {
    'get_flight_times': {
        'description': 'Get the flight times between two cities',
        'params': {
            'departure': {'type': 'string', 'description': 'The departure city (airport code)'},
            'arrival': {'type': 'string', 'description': 'The arrival city (airport code)'},
        },
        'func': get_flight_times,
    },
    'add_numbers': {
        'description': 'Adds two numbers together.',
        'params': {
            'a': {'type': 'int', 'description': 'The first number to add'},
            'b': {'type': 'int', 'description': 'The second number to add'},
        },
        'func': add_numbers,
    }
}