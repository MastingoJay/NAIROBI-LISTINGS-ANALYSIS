# Nairobi House Price Data Dictionary

## Dataset Overview
- Total Listings: 501 properties
- Collection Date: February 18, 2026
- Locations Covered: 18 Nairobi neighborhoods
- Property Types: Apartment (455), House (28), Townhouse (18)

## Column Descriptions

| Column | Type | Examples | Stats / Notes |
|--------|------|---------|---------------|
| location | object | Westlands, Kilimani, Kileleshwa, Riverside, Lower Kabete | Missing: 0, Unique: 18 |
| property_type | object | Apartment, House, Townhouse | Missing: 0, Unique: 3 |
| bedrooms | int64 | 1, 3, 4, 2, 5 | Missing: 0, Range: 1 - 8 |
| bathrooms | int64 | 1, 3, 5, 2, 6 | Missing: 0, Range: 1 - 9 |
| size_sqft | float64 | 699.66, 1668.42, 2271.2, 1291.68, 1130.22 | Missing: 23, Range: 32.29 - 43099.06, Outliers possible |
| amenities | object | Parking (1), Parking (3), Parking (2), Parking (4), Parking (7) | Missing: 6, Unique: 13 |
| price_kes | int64 | 6500000, 21714000, 27500000, 14800000, 9700000 | Missing: 0, Range: 360000 - 350000000, Mean: 22731066.47, Median: 13000000.00 |
| listing_date | object | 2026-02-18 | Missing: 0, Unique: 1 |

## Data Quality Issues Identified

### Critical Issues
- Duplicates: 233 duplicate rows
- Price outliers: 360,000 KES property in Runda - impossibly low
- Size outliers: 96.88 sqft properties with 2 bedrooms - impossible
- Missing values: 23 missing sizes, 6 missing amenities

## Location Summary (Top 10 by count)

| location    |   count |     min_price |   max_price |
|:------------|--------:|--------------:|------------:|
| Westlands   |     265 |      5.3e+06  |    8.7e+07  |
| Kilimani    |      86 |      5.5e+06  |    6.25e+07 |
| Kileleshwa  |      53 |      5.11e+06 |    9e+07    |
| Syokimau    |      17 |      4.8e+06  |    1.25e+07 |
| Riverside   |      14 |      7.2e+06  |    2.8e+07  |
| Lavington   |      12 |      1e+07    |    2.2e+08  |
| Runda       |      10 | 360000        |    2.6e+08  |
| Parklands   |       8 |      6.6e+06  |    6.5e+07  |
| Kitisuru    |       7 |      6e+07    |    3.5e+08  |
| Kiambu Road |       7 |      3.45e+07 |    8.5e+07  |

## Property Type Breakdown

| property_type   |   count |   avg_price |
|:----------------|--------:|------------:|
| Apartment       |     455 | 1.58899e+07 |
| House           |      28 | 9.65843e+07 |
| Townhouse       |      18 | 8.07778e+07 |

## Notes
- Review and clean outliers in price and size.
- Fill missing amenities with 'None'.
- Consider engineered features: price_per_sqft, amenity_score, month from listing_date.
