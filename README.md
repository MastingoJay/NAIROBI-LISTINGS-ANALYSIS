# NAIROBI-LISTINGS-ANALYSIS

![Python](https://img.shields.io/badge/python-3.12+-blue.svg) 
![Pip](https://img.shields.io/badge/pip-v24.0+-green.svg)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.3+-orange.svg)
![Pandas](https://img.shields.io/badge/pandas-2.1+-blueviolet.svg)
![NumPy](https://img.shields.io/badge/numpy-1.26+-brightgreen.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-latest-yellow.svg)

Nairobi house price prediction : scraping → cleaning → ML → Streamlit dashboard

This project is a full-stack machine learning system that predicts residential property prices in Nairobi, Kenya, using real market listings. From raw web data to a live prediction app, it showcases an end-to-end data science workflow built for real-world impact.

![](https://github.com/MastingoJay/NAIROBI-LISTINGS-ANALYSIS/blob/main/pictures/Nairobi%20Global%20Trade%20Center.jfif)

#  What This Project Does

The Nairobi real estate market is complex, fragmented, and often opaque. This system cuts through the noise by learning from actual property listings and delivering data-driven price estimates.

At a Glance

- Scrapes real property listings from the web

- Cleans and standardizes messy market data

- Trains ML models to learn pricing patterns

- Visualizes market trends and price drivers

- Serves predictions through an interactive web app

# Key Achievements

### Model Details:

- Model: Random Forest Regressor

- Features: 24

- Training samples: 213

- Test samples: 54

### Performance Metrics:

- MAE: ±7.04M KES → ~18% improvement over baseline

- R²: 0.703 → Explains 70.3% of price variance

# Problem Statement

Property pricing in Nairobi often relies on:

- Guesswork

- Inconsistent agent advice

- Limited market transparency

This leads to overpriced listings, missed opportunities, and poor investment decisions.

# Project Architecture

## Project Structure

```text
nairobi_property/
├── data/
│   ├── raw_listings.csv
│   ├── clean_listings.csv
│   └── data_dictionary.md
│
├── models/
│   └── model.pkl
│
├── notebooks/
│   ├── day1.ipynb
│   ├── day2_cleaning.ipynb
│   ├── day2_eda.ipynb
│   ├── day3_baseline_model.ipynb
│   └── day4_model_improvement.ipynb
│
├── scripts/
│   ├── clean_data.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── visualizations.py
│   └── predict.py
│
├── scrapping/
│   ├── convert.py
│   ├── read_scrapped_data.py
│   ├── property_scraper.py
│   └── run_scrapper.py
│
├── app/
│   └── streamlit_app.py
│
├── visualizations/
├── screenshots/
├── requirements.txt
└── README.md

```
# Interactive Web Application
A high-performance Streamlit interface that bridges the gap between complex machine learning and user-friendly property valuation.

### home page
![](https://github.com/MastingoJay/NAIROBI-LISTINGS-ANALYSIS/blob/main/pictures/pricing%20app%20home%20page.png)

### price prediction 
![](https://github.com/MastingoJay/NAIROBI-LISTINGS-ANALYSIS/blob/main/pictures/pricing%20app%20service%20page.png)

### Core Features
* **Modern UI/UX:** Clean, responsive design with a gradient-styled interface and intuitive property configuration controls.
* **Instant Valuations:** Real-time price predictions that update dynamically as user inputs change.
* **Smart Ranges:** Provides a "Price Ceiling" and "Floor Price" based on the model's Mean Absolute Error (MAE), offering a realistic confidence interval.
* **Market Intelligence:** Embedded dashboard showing the top 5 most expensive locations and bedroom-to-value growth trends.
* **Interactive Visuals:** Dynamic charts powered by **Plotly** for a deeper understanding of market segments.
* **Price Efficiency:** Automatic calculation of price-per-square-foot to help users identify undervalued deals.

### How to Launch
1. Ensure you have the dependencies installed: `pip install -r requirements.txt`
2. Run the application from the root directory:
   ```bash
   streamlit run app/pricing_app.py

# Data Pipeline

## 1. Data Collection
- Source: Property24.co.ke
- Method: Custom BeautifulSoup web scraper.
- Features: Location, type, bedrooms, bathrooms, size, amenities, price.

## 2. Data Cleaning
- Removed duplicate listings and standardized location names.
- Filtered size outliers (<200 sqft or >20,000 sqft).
- Filtered price outliers (<5M KES or >100M KES).

## 3. Feature Engineering

Created Features:

- price_per_sqft - Price normalized by size for comparison

- amenity_score - Count of amenities (0-5)

- month - Temporal features from listing dates


## 4. Model Training

**Models Developed:**

| Model               | MAE (M KES) | R² Score | Notes |
|--------------------|-------------|----------|-------|
| Linear Regression  | 8.04        | 0.623    | Baseline, works best for mid-range properties |
| Random Forest      | 7.04        | 0.703    | Winner! Better handling of non-linear relationships and amenities impact |

**Winner:** Random Forest Regressor 

**Improvements Over Baseline:**  
- **MAE:** 12.6% better (8.04M → 7.04M KES)  
- **R²:** 12.9% improvement (0.623 → 0.703)  
- Handles non-linear relationships and complex feature interactions more effectively.

# Tech Stack
### Core
- Python 3.12  
- Pandas  
- NumPy  
- Scikit-learn  

### Visualization
- Matplotlib  
- Seaborn  
- Plotly  

### Data Collection
- BeautifulSoup  
- Requests  

### Development
- Jupyter Notebook  
- Git  
- Pickle


# Visual Analytics

Includes publication-ready plots: 

- Top 10 Most Expensive Locations by Price
- Top 10 Cheapest Listings
- Locations with Most Listings (Top 10)
- Locations with Highest Price per Sqft
- Top 10 Most Expensive Locations by Median Price
- Top 10 Cheapest Locations by Median Price
- Average Price by Property Type
- Median Price by Number of Bedrooms
- Top 10 Listings by Amenity Score
- Simple Linear Regression line showing relationship between property size and price  

**Designed with:**  
- Clean formatting  
- Professional color gradients  
- Clear annotations  
- Tools: Matplotlib, Seaborn, Plotly, **Power BI**

## Power BI Visualizations

![](https://github.com/MastingoJay/NAIROBI-LISTINGS-ANALYSIS/blob/main/pictures/nairobi%20home%20page.png)

![](https://github.com/MastingoJay/NAIROBI-LISTINGS-ANALYSIS/blob/main/pictures/market%20overview.png)

![](https://github.com/MastingoJay/NAIROBI-LISTINGS-ANALYSIS/blob/main/pictures/regional%20performance.png)

![](https://github.com/MastingoJay/NAIROBI-LISTINGS-ANALYSIS/blob/main/pictures/amenity%20analysis.png)

![](https://github.com/MastingoJay/NAIROBI-LISTINGS-ANALYSIS/blob/main/pictures/investment.png)

![](https://github.com/MastingoJay/NAIROBI-LISTINGS-ANALYSIS/blob/main/pictures/insights.png)

# Navigation Instructions

- Buttons have been added to the Home, Dashboard, and Insights pages for easy navigation.

- To navigate, click on a button, then press Ctrl + Enter to move to the selected page.

##  Future Enhancements

- Multi-source data scraping  
- Geo-spatial features (GPS coordinates)  
- Time-series market trends  
- Advanced models (XGBoost, LightGBM)  
- Property age & condition features  
- Full production deployment

##  Who This Is For

- **Buyers** – Validate listing prices  
- **Sellers** – Price competitively  
- **Agents & Investors** – Provide data-backed advice  
- **Developers** – Forecast ROI  
- **Researchers** – Study urban housing trends

















