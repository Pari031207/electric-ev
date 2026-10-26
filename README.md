# EV Market Analysis Dashboard

Tableau dashboard suite tracking global EV market dynamics, manufacturer competitive performance, battery chemistry evolution, driving range benchmarks, and customer satisfaction across 2021–2024.

## Repository Structure

```
electric-ev/
├── data/
│   ├── raw_ev_data.csv              # 525 vehicle model records across 2021-2024
│   └── cleaned_ev_data.csv          # Cleaned dataset with MarketShare% and SalesGrowth%
├── tableau/
│   ├── ev_market_analysis.twb       # Tableau workbook XML linking all 10 views and 3 dashboards
│   └── ev_market_analysis.twbx      # Self-contained packaged workbook with embedded data
├── scripts/
│   ├── clean_data.py                # Python/pandas cleaning script
│   └── generate_data.ps1            # Dataset generation script
├── TABLEAU_BUILD_GUIDE.md           # Step-by-step build spec (Tasks 1-14)
├── INSIGHTS_SUMMARY.md              # Executive market & technology insights summary
└── README.md                        # Documentation
```

## Key Metrics (2021–2024)
- **Total Volume Tracked:** 34.3 Million EV units
- **Average Driving Range:** 395.8 km
- **Average Battery Capacity:** 93.6 kWh
- **Average Customer Rating:** 4.27 / 5.0
- **Leading Chemistries:** LFP (52%), NMC (34%), NCA (10%), Sodium-Ion & Solid-State (4%)

## 3 Persona Dashboards
1. **Executive Strategy Dashboard** (*Emily Johnson, Market Strategy Director*): Segment trends, leading manufacturers, and satisfaction matrix.
2. **Competitive Intelligence Dashboard** (*David Chen, BI Manager*): Manufacturer market shares, geographic footprint, and product positioning.
3. **Technology Research Dashboard** (*Dr. Sarah Williams, Sustainable Mobility Analyst*): Battery chemistry breakdown, range-to-capacity efficiency, and charging benchmarks.

## How to Open in Tableau
Open `tableau/ev_market_analysis.twbx` directly in Tableau Desktop or Tableau Public.
