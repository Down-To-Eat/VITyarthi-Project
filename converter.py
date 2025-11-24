"""
Conversion Engine Module
Handles all unit conversion calculations with high precision
Author: [Your Name]
Date: November 24, 2025
"""

import math

# Length conversion factors (all to meters as base)
LENGTH_UNITS = {
    'meter': 1.0,
    'kilometer': 1000.0,
    'centimeter': 0.01,
    'millimeter': 0.001,
    'mile': 1609.344,
    'yard': 0.9144,
    'foot': 0.3048,
    'inch': 0.0254
}

# Weight conversion factors (all to kilograms as base)
WEIGHT_UNITS = {
    'kilogram': 1.0,
    'gram': 0.001,
    'milligram': 0.000001,
    'pound': 0.453592,
    'ounce': 0.0283495,
    'ton': 1000.0
}

# Time conversion factors (all to seconds as base)
TIME_UNITS = {
    'second': 1.0,
    'minute': 60.0,
    'hour': 3600.0,
    'day': 86400.0,
    'week': 604800.0,
    'month': 2592000.0,  # 30 days average
    'year': 31536000.0   # 365 days
}

def convert_length (value, from_unit, to_unit):
    """
    Convert length between different units
    
    Args:
        value (float): The value to convert
        from_unit (str): Source unit
        to_unit (str): Target unit
    
    Returns:
        float: Converted value
    
    Raises:
        ValueError: If units are invalid
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in LENGTH_UNITS:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if to_unit not in LENGTH_UNITS:
        raise ValueError(f"Invalid target unit: {to_unit}")
    
    # Convert to base unit (meters) then to target
    meters = value * LENGTH_UNITS[from_unit]
    result = meters / LENGTH_UNITS[to_unit]
    return round(result, 6)

def convert_temperature (value, from_unit, to_unit):
    """
    Convert temperature between Celsius, Fahrenheit, and Kelvin
    
    Args:
        value (float): Temperature value
        from_unit (str): Source scale (celsius/fahrenheit/kelvin)
        to_unit (str): Target scale
    
    Returns:
        float: Converted temperature
    
    Raises:
        ValueError: If units are invalid
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    valid_units = ['celsius', 'fahrenheit', 'kelvin']
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("Temperature units must be: celsius, fahrenheit, or kelvin")
    
    # Convert to Celsius as intermediate
    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5.0 / 9.0
    elif from_unit == 'kelvin':
        celsius = value - 273.15
    
    # Convert from Celsius to target
    if to_unit == 'celsius':
        result = celsius
    elif to_unit == 'fahrenheit':
        result = (celsius * 9.0 / 5.0) + 32
    elif to_unit == 'kelvin':
        result = celsius + 273.15
    
    return round(result, 4)

def convert_weight(value, from_unit, to_unit):
    """
    Convert weight/mass between different units
    
    Args:
        value (float): Weight value
        from_unit (str): Source unit
        to_unit (str): Target unit
    
    Returns:
        float: Converted weight
    
    Raises:
        ValueError: If units are invalid
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in WEIGHT_UNITS:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if to_unit not in WEIGHT_UNITS:
        raise ValueError(f"Invalid target unit: {to_unit}")
    
    # Convert to base unit (kg) then to target
    kg = value * WEIGHT_UNITS[from_unit]
    result = kg / WEIGHT_UNITS[to_unit]
    return round(result, 6)

def convert_time(value, from_unit, to_unit):
    """
    Convert time between different units
    
    Args:
        value (float): Time value
        from_unit (str): Source unit
        to_unit (str): Target unit
    
    Returns:
        float: Converted time
    
    Raises:
        ValueError: If units are invalid
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    if from_unit not in TIME_UNITS:
        raise ValueError(f"Invalid source unit: {from_unit}")
    if to_unit not in TIME_UNITS:
        raise ValueError(f"Invalid target unit: {to_unit}")
    
    # Convert to base unit (seconds) then to target
    seconds = value * TIME_UNITS[from_unit]
    result = seconds / TIME_UNITS[to_unit]
    return round(result, 6)

# Quick reference dictionaries for menu display
CATEGORY_UNITS = {
    'length': list(LENGTH_UNITS.keys()),
    'temperature': ['celsius', 'fahrenheit', 'kelvin'],
    'weight': list(WEIGHT_UNITS.keys()),
    'time': list(TIME_UNITS.keys())
}

def get_available_units(category):
    """Get list of available units for a category"""
    return CATEGORY_UNITS.get(category.lower(), [])
