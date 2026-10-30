from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/length")
def get_length(length: int, unit1: str, unit2: str):
    # Conversion factors for length units
    conversion_factors = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254
    }

    # Check if the provided units are valid
    if unit1 in conversion_factors and unit2 in conversion_factors:

        # Convert the length to meters first
        length_in_meters = length * conversion_factors[unit1]

        # Convert from meters to the target unit
        converted_length = length_in_meters / conversion_factors[unit2]

        return {
            "original_length": length,
            "original_unit": unit1,
            "converted_length": converted_length,
            "converted_unit": unit2
        }
    
    else:
        # Construct a helpful error message showing which unit is wrong
        invalid_units = [u for u in [unit1, unit2] if u not in conversion_factors]
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "INVALID_UNITS",
                "message": f"Unsupported or invalid unit(s) provided: {', '.join(invalid_units)}.",
                "supported_units": list(conversion_factors.keys())
            }
        )
@app.get("/weight")
def get_weight(weight: float, unit1: str, unit2: str):
    # Conversion factors for weight units
    conversion_factors = {
        "kilograms": 1,
        "grams": 0.001,
        "milligrams": 0.000001,
        "pounds": 0.453592,
        "ounces": 0.0283495,
        "labs": 0.453592,
        "tones": 1000
    }

    # Check if the provided units are valid
    if unit1 in conversion_factors and unit2 in conversion_factors:

        # Convert the weight to kilograms first
        weight_in_kilograms = weight * conversion_factors[unit1]

        # Convert from kilograms to the target unit
        converted_weight = weight_in_kilograms / conversion_factors[unit2]

        return {
            "original_weight": weight,
            "original_unit": unit1,
            "converted_weight": converted_weight,
            "converted_unit": unit2
        }
    
    else:
        # Construct a helpful error message showing which unit is wrong
        invalid_units = [u for u in [unit1, unit2] if u not in conversion_factors]
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "INVALID_UNITS",
                "message": f"Unsupported or invalid unit(s) provided: {', '.join(invalid_units)}.",
                "supported_units": list(conversion_factors.keys())
            }
        )
@app.get("/temperature")
def get_temperature(temperature: float, unit1: str, unit2: str):
    conversion_factors = {
        "celsius": lambda x: x,
        "fahrenheit": lambda x: (x - 32) * 5/9,
        "kelvin": lambda x: x - 273.15
    }
    if unit1 in conversion_factors and unit2 in conversion_factors:
        # Convert the temperature to Celsius first
        temp_in_celsius = conversion_factors[unit1](temperature)

        # Convert from Celsius to the target unit
        if unit2 == "celsius":
            converted_temp = temp_in_celsius
        elif unit2 == "fahrenheit":
            converted_temp = (temp_in_celsius * 9/5) + 32
        elif unit2 == "kelvin":
            converted_temp = temp_in_celsius + 273.15

        return {
            "original_temperature": temperature,
            "original_unit": unit1,
            "converted_temperature": converted_temp,
            "converted_unit": unit2
        }
    else:
        # Construct a helpful error message showing which unit is wrong
        invalid_units = [u for u in [unit1, unit2] if u not in conversion_factors]
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "INVALID_UNITS",
                "message": f"Unsupported or invalid unit(s) provided: {', '.join(invalid_units)}.",
                "supported_units": list(conversion_factors.keys())
            }
        )