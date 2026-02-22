import streamlit as st
import pandas as pd
import numpy as np
import joblib  
import os
import plotly.express as px
import plotly.graph_objects as go

# --- 0. DYNAMIC PATH SETUP ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Nairobi Property Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CUSTOM CSS FOR STYLING
st.markdown("""
<style>
    .main-header {
        font-size: 4rem; /* Increased from 2.8rem */
        font-weight: 800;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 0rem;
        padding-top: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.4rem; /* Slightly increased for balance */
        color: #4B5563;
        text-align: center;
        margin-bottom: 2.5rem;
    }
    .prediction-box {
        background: linear-gradient(135deg, #87CEEB 0%, #1E3A8A 100%);
        padding: 2.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: #F3F4F6;
        padding: 1.2rem;
        border-radius: 10px;
        border-top: 5px solid #87CEEB;
        text-align: center;
    }
    /* Make the sidebar buttons pop */
    .stButton>button {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# 3. HELPER FUNCTIONS
@st.cache_resource
def load_assets():
    """Load model from the 'models' folder"""
    model_path = os.path.join(PROJECT_ROOT, 'models', 'model.pkl')
    model = joblib.load(model_path)
    
    model_columns = [
        'bedrooms', 'bathrooms', 'size_sqft', 'parking_spaces', 'has_garden', 
        'location_Kiambu Road', 'location_Kileleshwa', 'location_Kilimani', 
        'location_Kitisuru', 'location_Kyuna', 'location_Lavington', 
        'location_Loresho', 'location_Lower Kabete', 'location_Muthangari', 
        'location_Nyari', 'location_Parklands', 'location_Peponi', 
        'location_Riverside', 'location_Runda', 'location_Spring Valley', 
        'location_Syokimau', 'location_Westlands', 'property_type_House', 
        'property_type_Townhouse'
    ]
    return model, model_columns

@st.cache_data
def get_historical_data():
    """Load data from the 'data' folder"""
    data_path = os.path.join(PROJECT_ROOT, 'data', 'clean_listings.csv')
    return pd.read_csv(data_path)

# 4. DATA LOADING
try:
    model, model_columns = load_assets()
    df = get_historical_data()
except Exception as e:
    st.error(f"Error loading files: {e}. Check your folder structure (data/ and models/)")
    st.stop()

# 5. SIDEBAR INPUTS
st.sidebar.markdown("### 🛠️ Property Configuration")

if st.sidebar.button("🔄 Reset All Inputs", use_container_width=True):
    st.rerun()

location = st.sidebar.selectbox("Select Location", sorted(df['location'].unique()))
prop_type = st.sidebar.selectbox("Property Type", sorted(df['property_type'].unique()))

col_s1, col_s2 = st.sidebar.columns(2)
bedrooms = col_s1.number_input("Bedrooms", 1, 10, 3)
bathrooms = col_s2.number_input("Bathrooms", 1, 10, 2)

size_sqft = st.sidebar.slider("Size (Sqft)", 200, 10000, 2500)
parking = st.sidebar.slider("Parking Spaces", 0, 5, 2)
garden = st.sidebar.checkbox("Has Private Garden")

st.sidebar.markdown("---")
predict_btn = st.sidebar.button("🔮 Calculate Valuation", type="primary", use_container_width=True)

# 6. MAIN CONTENT AREA
st.markdown('<h1 class="main-header">🏠 Nairobi Property Predictor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Real Estate Valuations for the 2026 Market</p>', unsafe_allow_html=True)

layout_col1, layout_col2 = st.columns([2, 1])

with layout_col1:
    if predict_btn:
        # Create Input DataFrame
        input_row = pd.DataFrame(0, index=[0], columns=model_columns)
        input_row['bedrooms'] = bedrooms
        input_row['bathrooms'] = bathrooms
        input_row['size_sqft'] = size_sqft
        input_row['parking_spaces'] = parking
        input_row['has_garden'] = 1 if garden else 0
        
        # Set Dummy Variables
        if f"location_{location}" in model_columns: input_row[f"location_{location}"] = 1
        if f"property_type_{prop_type}" in model_columns: input_row[f"property_type_{prop_type}"] = 1
        
        # Prediction
        pred_log = model.predict(input_row)[0]
        prediction = np.expm1(pred_log)
        
        # Display Result
        st.markdown(f"""
            <div class="prediction-box">
                <p style="margin:0; font-size:1.3rem; font-weight: 500;">Estimated Market Value</p>
                <h1 style="margin:0; font-size:4.5rem;">KSh {prediction:,.0f}</h1>
                <p style="margin:0; opacity:0.9;">{prediction/1e6:.2f} Million KES</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Range Metrics (MAE = 7.04M)
        mae = 7044398
        m1, m2, m3 = st.columns(3)
        m1.markdown(f'<div class="metric-card"><b>Min Range</b><br>KSh {(prediction-mae)/1e6:.1f}M</div>', unsafe_allow_html=True)
        m2.markdown(f'<div class="metric-card"><b>Expected</b><br>KSh {prediction/1e6:.1f}M</div>', unsafe_allow_html=True)
        m3.markdown(f'<div class="metric-card"><b>Max Range</b><br>KSh {(prediction+mae)/1e6:.1f}M</div>', unsafe_allow_html=True)

        st.info(f"💡 **Insight:** At **KSh {prediction/size_sqft:,.0f} per sqft**, this property is priced within the top market tier of {location}.")
    else:
        st.image(
            "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80", 
            use_container_width=True
        )
        st.write("### How it works")
        st.write("Adjust the filters on the left to see how location, size, and amenities impact the valuation of a property in Nairobi's 2026 market.")

with layout_col2:
    st.subheader("📊 Market Intelligence")
    
    # Visual 1: Median Prices by Location
    top_locs = df.groupby('location')['price_kes'].median().sort_values(ascending=False).head(5)
    fig_loc = px.bar(top_locs, x=top_locs.values/1e6, y=top_locs.index, 
                     orientation='h', title="Top 5 Expensive Areas (M KES)",
                     labels={'x':'Median Price', 'y':''}, color_discrete_sequence=['#1E3A8A'])
    fig_loc.update_layout(height=350, margin=dict(t=40, b=0, l=0, r=0))
    st.plotly_chart(fig_loc, use_container_width=True)
    
    st.divider()
    
    # Visual 2: Bedroom Value Impact
    bed_val = df.groupby('bedrooms')['price_kes'].median() / 1e6
    fig_bed = px.line(bed_val, x=bed_val.index, y=bed_val.values, 
                      title="Value Growth by Bedroom Count", markers=True)
    fig_bed.update_traces(line_color='#87CEEB', line_width=4)
    fig_bed.update_layout(height=300, margin=dict(t=40, b=0, l=0, r=0))
    st.plotly_chart(fig_bed, use_container_width=True)

# 7. FOOTER
st.markdown("---")
st.caption("© 2026 Nairobi Real Estate Analytics")