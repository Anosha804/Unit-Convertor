import streamlit as st

# Set Page Config
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
          body {
            background-color: #f5f5f5;
        }
        .stApp {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px 24px;
            border-radius: 8px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .result-card {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #333;
        }
        .custom-header {
            font-size: 22px;
            font-weight: bold;
            color: #333;
            margin-bottom: 5px;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 5px;
            display: inline-block;
        }
        /* Enhanced Dropdown & Input Box Styling */
        .stSelectbox>div, .stNumberInput>div {
            background-color: white !important;
            border: 2px solid #4CAF50 !important;
            border-radius: 10px !important;
            padding: 5px !important;
            font-size: 16px !important;
        }
        .stSelectbox:hover>div, .stNumberInput:hover>div {
            border-color: #45a049 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function for unit conversion
def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084
        },
        "Weight": {
            "Grams": 1, "Kilograms": 0.001, "Pounds": 0.00220462, "Ounces": 0.035274
        },
        "Temperature": {
            "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15
        }
    }
    
    if category == "Temperature":
        if from_unit == "Fahrenheit":
            value = (value - 32) * 5/9  # Convert Fahrenheit to Celsius
        elif from_unit == "Kelvin":
            value = value - 273.15  # Convert Kelvin to Celsius
        
        return conversions[category][to_unit](value)
    
    base_value = value / conversions[category][from_unit]  # Convert to base unit
    return base_value * conversions[category][to_unit]  # Convert to target unit

# Header
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📏 Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("---")

# Enhanced Select Category Section
st.markdown("<p class='custom-header'>🔹 Select a Category:</p>", unsafe_allow_html=True)
categories = ["Length 📏", "Weight ⚖️", "Temperature 🌡️"]
category = st.selectbox("", categories)

# Extracting the category name (removing emoji)
category_name = category.split(" ")[0]

# Unit options based on category
unit_options = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Weight": ["Grams", "Kilograms", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Enhanced Convert From Section
st.markdown("<p class='custom-header'>🔄 Convert From:</p>", unsafe_allow_html=True)
from_unit = st.selectbox("Select Unit To convert from", unit_options[category_name])

# Enhanced Convert To Section
st.markdown("<p class='custom-header'>➡️ Convert To:</p>", unsafe_allow_html=True)
to_unit = st.selectbox("Select Unit To Convert To", unit_options[category_name])

# Enhanced Enter Value Section
st.markdown("<p class='custom-header'>✍️ Enter Value:</p>", unsafe_allow_html=True)
value = st.number_input("", value=0.0, step=0.1)

# Convert Button
if st.button("🚀 Convert"):
    result = convert_units(value, from_unit, to_unit, category_name)
    st.markdown(
        f"""
        <div class="result-card">
            {value} {from_unit} = <span style="color: #4CAF50;">{result:.2f}</span> {to_unit}
        </div>
        """,
        unsafe_allow_html=True,
    )
