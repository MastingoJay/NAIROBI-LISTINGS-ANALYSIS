import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Set Page Config
st.set_page_config(page_title="Nairobi Property Predictor", layout="centered")

# 1. LOAD MODEL & CONFIG
@st.cache_resource
def load_assets():
    model = joblib.load('model.pkl')
    # Exact column order from Day 4 Training
    cols = ['bedrooms', 'bathrooms', 'size_sqft', 'parking_spaces', 'has_garden', 
            'location_Kiambu Road', 'location_Kileleshwa', 'location_Kilimani', 
            'location_Kitisuru', 'location_Kyuna', 'location_Lavington', 
            'location_Loresho', 'location_Lower Kabete', 'location_Muthangari', 
            'location_Nyari', 'location_Parklands', 'location_Peponi', 
            'location_Riverside', 'location_Runda', 'location_Spring Valley', 
            'location_Syokimau', 'location_Westlands', 'property_type_House', 
            'property_type_Townhouse']
    return model, cols

model, model_columns = load_assets()

# 2. APP UI
st.title("Nairobi Property Price Predictor")
st.markdown("Estimate the market value of residential properties in Nairobi using Machine Learning.")

st.sidebar.header("Input Property Details")
location = st.sidebar.selectbox("Location", [
    'Karen', 'Kiambu Road', 'Kileleshwa', 'Kilimani', 'Kitisuru', 'Kyuna', 
    'Lavington', 'Loresho', 'Lower Kabete', 'Muthangari', 'Nyari', 'Parklands', 
    'Peponi', 'Riverside', 'Runda', 'Spring Valley', 'Syokimau', 'Westlands'
])
prop_type = st.sidebar.selectbox("Property Type", ['Apartment', 'House', 'Townhouse'])
bedrooms = st.sidebar.slider("Bedrooms", 1, 10, 3)
bathrooms = st.sidebar.slider("Bathrooms", 1, 10, 2)
size_sqft = st.sidebar.number_input("Size (sqft)", 100, 20000, 2500)
parking = st.sidebar.number_input("Parking Spaces", 0, 10, 2)
garden = st.sidebar.checkbox("Has Garden")

# 3. PREDICTION ENGINE
if st.button("Calculate Predicted Price"):
    # Prepare Input DataFrame
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    input_df['bedrooms'] = bedrooms
    input_df['bathrooms'] = bathrooms
    input_df['size_sqft'] = size_sqft
    input_df['parking_spaces'] = parking
    input_df['has_garden'] = 1 if garden else 0
    
    # Set One-Hot Columns
    if f"location_{location}" in model_columns: input_df[f"location_{location}"] = 1
    if f"property_type_{prop_type}" in model_columns: input_df[f"property_type_{prop_type}"] = 1

    # Predict
    pred_log = model.predict(input_df)[0]
    price = np.expm1(pred_log)
    
    # 4. OUTPUTS
    mae = 7044398 # From Day 4 results
    st.success(f"## Estimated Price: KSh {price:,.0f}")
    
    c1, c2 = st.columns(2)
    c1.metric("Lower Bound (-MAE)", f"KSh {max(0, price-mae):,.0f}")
    c2.metric("Upper Bound (+MAE)", f"KSh {price+mae:,.0f}")
    
    # 5. EXPLANATION
    st.subheader("Why this price?")
    drivers = []
    if prop_type == 'House': drivers.append("- **House Premium:** Detached houses carry the highest market weight.")
    if location in ['Nyari', 'Kyuna', 'Runda']: drivers.append(f"- **Prime Location:** {location} is a top-tier neighborhood.")
    if parking >= 3: drivers.append("- **High Utility:** Ample parking significantly boosts value in Nairobi.")
    if bedrooms >= 4: drivers.append("- **Family Capacity:** Large bedroom counts target high-value buyers.")
    
    for d in drivers: st.write(d)