import streamlit as st

# Title and description
st.title("Unit Converter")
st.write("Convert between different units easily with this simple app.")

# Conversion functions
def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084,
        'inches': 39.3701
    }
    
    if value < 0:
        return "Error: Negative values are not supported for length conversions."

    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Error: Unsupported unit. Please select a valid unit."
    
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Sidebar for user input
st.sidebar.header("Choose Conversion Type")
conversion_type = st.sidebar.selectbox("Select a type of conversion", ["Length", "Temperature", "Weight"])

if conversion_type == "Length":
    st.subheader("Length Converter")
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches'])
    to_unit = st.selectbox("To Unit", ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches'])
    
    if st.button("Convert"):
        result = length_converter(value, from_unit, to_unit)
        if isinstance(result, str):
            st.error(result)
        else:
            st.success(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")

elif conversion_type == "Temperature":
    st.subheader("Temperature Converter")
    value = st.number_input("Enter temperature:", format="%.2f")
    from_unit = st.selectbox("From Unit", ['Celsius', 'Fahrenheit', 'Kelvin'])
    to_unit = st.selectbox("To Unit", ['Celsius', 'Fahrenheit', 'Kelvin'])
    
    if st.button("Convert"):
        if from_unit == to_unit:
            result = value
        elif from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            result = value * 9/5 + 32
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            result = value + 273.15
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            result = (value - 32) * 5/9
        elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            result = value - 273.15
        elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
            result = (value - 273.15) * 9/5 + 32
        
        st.success(f"{value:.2f} {from_unit} is equal to {result:.2f} {to_unit}")

elif conversion_type == "Weight":
    st.subheader("Weight Converter")
    value = st.number_input("Enter weight:", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit", ['kilograms', 'grams', 'pounds', 'ounces'])
    to_unit = st.selectbox("To Unit", ['kilograms', 'grams', 'pounds', 'ounces'])
    
    weight_factors = {
        'kilograms': 1,
        'grams': 1000,
        'pounds': 2.20462,
        'ounces': 35.274
    }

    if st.button("Convert"):
        if from_unit == to_unit:
            result = value
        else:
            result = value * weight_factors[to_unit] / weight_factors[from_unit]
        
        st.success(f"{value:.2f} {from_unit} is equal to {result:.2f} {to_unit}")

st.sidebar.info("Built with Streamlit and Python by Iqra — Happy Converting!\n\nNeed help? [Learn about unit conversions](https://www.unitconverters.net)")


