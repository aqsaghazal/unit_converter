import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1{
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton > button{
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton > button:hover{
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        transform: translateY(-2px);
        color: #black;
        box-shadow: 0px 8px 20px rgba(0, 201, 255, 0.5);
    }
    .result-box{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        color: white;
        background: linear-gradient(45deg, #0b5394, #351c75);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#title and decription
st.markdown("<h1 style='text-align: center;'>Unit Converter</h1>", unsafe_allow_html=True)
st.write("Convert between different units of measurement")

#sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature", "Volume", "Area", "Time", "Currency", "Energy", "Data", "Pressure", "Speed"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Feet", "Miles", "Kilometers", "Centimeters", "Millimeters", "Yards", "Inches"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Feet", "Miles", "Kilometers", "Centimeters", "Millimeters", "Yards", "Inches"])


elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Pounds", "Grams", "Ounces", "Milligrams", "Micrograms"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Pounds", "Grams", "Ounces", "Milligrams", "Micrograms"])


elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])


elif conversion_type == "Volume":
    with col1:  
        from_unit = st.selectbox("From", ["Liters", "Gallons", "Cups", "Pints", "Quarts", "Tablespoons", "Teaspoons"])
    with col2:
        to_unit = st.selectbox("To", ["Liters", "Gallons", "Cups", "Pints", "Quarts", "Tablespoons", "Teaspoons"])


elif conversion_type == "Area":
    with col1:
        from_unit = st.selectbox("From", ["Square Meters", "Square Feet", "Square Miles", "Square Kilometers", "Acres", "Hectares"])        
    with col2:
        to_unit = st.selectbox("To", ["Square Meters", "Square Feet", "Square Miles", "Square Kilometers", "Acres", "Hectares"])


elif conversion_type == "Time":
    with col1:
        from_unit = st.selectbox("From", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])
    with col2:
        to_unit = st.selectbox("To", ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"])


elif conversion_type == "Currency":
    with col1:
        from_unit = st.selectbox("From", ["USD", "EUR", "GBP", "CAD", "AUD", "JPY", "INR"])
    with col2:
        to_unit = st.selectbox("To", ["USD", "EUR", "GBP", "CAD", "AUD", "JPY", "INR"])     


elif conversion_type == "Energy":
    with col1:
        from_unit = st.selectbox("From", ["Joules", "Calories", "Kilojoules", "Kilocalories"])
    with col2:
        to_unit = st.selectbox("To", ["Joules", "Calories", "Kilojoules", "Kilocalories"])


elif     conversion_type == "Speed":
    with col1:
        from_unit = st.selectbox("From", ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots"])
    with col2:
        to_unit = st.selectbox("To", ["Meters per second", "Kilometers per hour", "Miles per hour", "Knots"])


elif conversion_type == "Data":
    with col1:
        from_unit = st.selectbox("From", ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"])
    with col2:
        to_unit = st.selectbox("To", ["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes"])


elif conversion_type == "Pressure":
    with col1:
        from_unit = st.selectbox("From", ["Pascals", "Kilopascals", "Megapascals", "Bar", "Atmospheres", "Torr", "Millimeters of mercury"])
    with col2:
        to_unit = st.selectbox("To", ["Pascals", "Kilopascals", "Megapascals", "Bar", "Atmospheres", "Torr", "Millimeters of mercury"])

#converted function
def length_converter(value, from_unit, to_unit):
    length_unit={
        "Meters":1,
        "Feet":3.28084,
        "Miles":0.000621371,
        "Kilometers":0.001,
        "Centimeters":100,
        "Millimeters":1000,
        "Yards":1.09361,
        "Inches":39.3701
    }
    return (value / length_unit[from_unit]) * length_unit[to_unit]


def weight_converter(value, from_unit, to_unit):
    weight_unit={
        "Kilograms":1,
        "Pounds":2.20462,
        "Grams":1000,
        "Ounces":35.274,
        "Milligrams":1000000,
        "Micrograms":1000000000
    }
    return (value / weight_unit[from_unit]) * weight_unit[to_unit]


def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value + 459.67) * 5/9 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value * 9/5) - 459.67 if to_unit == "Fahrenheit" else value
    return value


def volume_converter(value, from_unit, to_unit):
    volume_unit={
        "Liters":1,
        "Gallons":0.264172,
        "Cups":4.22675,
        "Pints":2.11338,
        "Quarts":1.05669,   
        "Tablespoons":67.628,
        "Teaspoons":202.884
    }
    return (value / volume_unit[from_unit]) * volume_unit[to_unit]


def area_converter(value, from_unit, to_unit):      
    area_unit={
        "Square Meters":1,
        "Square Feet":10.7639,
        "Square Miles":0.000000386102,
        "Square Kilometers":0.000001,
        "Acres":0.000247105,
        "Hectares":0.0001
    }
    return (value / area_unit[from_unit]) * area_unit[to_unit]


def time_converter(value, from_unit, to_unit):
    time_unit={
        "Seconds":1,
        "Minutes":60,
        "Hours":3600,
        "Days":86400,
        "Weeks":604800,
        "Months":2629746,
        "Years":31556952
    }
    return (value / time_unit[from_unit]) * time_unit[to_unit]


def currency_converter(value, from_unit, to_unit):
    currency_unit={
        "USD":1,
        "EUR":0.85,
        "GBP":0.75,
        "CAD":1.30,
        "AUD":1.40, 
        "JPY":110.00,
        "INR":75.00
    }
    return (value / currency_unit[from_unit]) * currency_unit[to_unit]  


def energy_converter(value, from_unit, to_unit):
    energy_unit={
        "Joules":1,
        "Calories":4.184,
        "Kilojoules":0.001, 
        "Kilocalories":0.000239
    }
    return (value / energy_unit[from_unit]) * energy_unit[to_unit]


def speed_converter(value, from_unit, to_unit):
    speed_unit={
        "Meters per second":1,
        "Kilometers per hour":3.6,
        "Miles per hour":2.23694,
        "Knots":1.94384
    }

def data_converter(value, from_unit, to_unit):
    data_unit={
        "Bytes":1,
        "Kilobytes":1024,
        "Megabytes":1048576,
        "Gigabytes":1073741824,
        "Terabytes":1099511627776
    }
    return (value / data_unit[from_unit]) * data_unit[to_unit]


def pressure_converter(value, from_unit, to_unit):
    pressure_unit={
        "Pascals":1,
        "Kilopascals":0.001,
        "Megapascals":0.000001,
        "Bar":0.00001,
        "Atmospheres":0.00000986923,
        "Torr":7.50062,
        "Millimeters of mercury":0.00750062
    }   
    return (value / pressure_unit[from_unit]) * pressure_unit[to_unit]


#button for conversion
if st.button("🤖Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)
    elif conversion_type == "Volume":
        result = volume_converter(value, from_unit, to_unit)
    elif conversion_type == "Area":
        result = area_converter(value, from_unit, to_unit)
    elif conversion_type == "Time":
        result = time_converter(value, from_unit, to_unit)
    elif conversion_type == "Currency":
        result = currency_converter(value, from_unit, to_unit)
    elif conversion_type == "Energy":
        result = energy_converter(value, from_unit, to_unit)
    elif conversion_type == "Speed":
        result = speed_converter(value, from_unit, to_unit)
    elif conversion_type == "Data":
        result = data_converter(value, from_unit, to_unit)
    elif conversion_type == "Pressure":
        result = pressure_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} is equal to {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='footer'>Made by <a href='https://github.com/aqsaghazal'>@Aqsa Ghazal</a></div>", unsafe_allow_html=True)

        
        
        
    
        
    






