# EV Market Analysis Dashboard – Tableau Build Guide

Step-by-step specifications, calculated-field formulas, and dashboard layouts for Tableau Desktop & Tableau Public (Tasks 1–14).

---

## E1: Data Preparation
- **Raw File**: `data/raw_ev_data.csv` (525 vehicle model records, 2021–2024).
- **Cleaned File**: `data/cleaned_ev_data.csv`.
- **Derived Fields**:
  - `MarketSharePct`: `(AnnualSales / TotalAnnualSalesForYear) * 100`
  - `SalesGrowthPct`: Year-over-Year sales growth rate per model/manufacturer.

---

## E2: Connect Data in Tableau (Task 3)
1. In Tableau, select **Connect > Text File** and open `data/cleaned_ev_data.csv`.
2. Verify Data Types & Roles:
   - **Dimensions**: `ModelID`, `Manufacturer`, `Model`, `VehicleCategory`, `BatteryType`, `Year` (Ordinal), `ManufacturingCountry` (Geographic: Country/Region).
   - **Measures**: `BatteryCapacity` (kWh), `DrivingRange` (km), `Price` ($), `AnnualSales`, `CustomerRating`, `ChargingTimeMinutes`, `MarketSharePct`, `SalesGrowthPct`.

---

## Calculated Fields Setup
Create these calculated fields (**Analysis > Create Calculated Field**):

1. **Market Share Calculated %**:
   ```tableau
   SUM([AnnualSales]) / TOTAL(SUM([AnnualSales]))
   ```
   *(Default Number Format: Percentage, 1 decimal)*
2. **Top Manufacturer Share**:
   ```tableau
   WINDOW_MAX(SUM([AnnualSales])) / TOTAL(SUM([AnnualSales]))
   ```
3. **Average Range (km)**:
   ```tableau
   AVG([DrivingRange])
   ```

---

## E3: KPI Cards (Task 4)
**Sheet Name:** `KPI_Cards`
- **Columns**: `Measure Names`
- **Text / Label**: `Measure Values`
- **Filter `Measure Names` to**:
  1. `SUM(AnnualSales)` (Total Sales: **34.3M units**)
  2. `AVG(DrivingRange)` (**395.8 km**)
  3. `AVG(BatteryCapacity)` (**93.6 kWh**)
  4. `AVG(CustomerRating)` (**4.27 / 5.0**)
  5. `AGG(Top Manufacturer Share)` (**~22.4% - Tesla/BYD**)
- **Mark**: Text / Tile KPI card.

---

## E4: Sales & Market Performance (Tasks 5–6)

### Task 5: Annual Sales by Vehicle Category
- **Sheet Name**: `Sales_by_Category`
- **Columns**: `Year`
- **Rows**: `SUM(AnnualSales)`
- **Color**: `VehicleCategory` (SUV, Sedan, Hatchback, Two-wheeler, Truck, Bus)
- **Mark**: Stacked Bar with Line Trend for YoY Sales Growth.

### Task 6: Sales and Market Share by Manufacturer
- **Sheet Name**: `Sales_and_MarketShare_by_Manufacturer`
- **Columns**: `SUM(AnnualSales)`
- **Rows**: `Manufacturer` (Sort descending by sales)
- **Color**: `MarketShare Calculated %`
- **Mark**: Horizontal Bar / Treemap.
- **Label**: Show Sales volume + `MarketShare Calculated %`.

---

## E5: Battery & Range (Tasks 7–8)

### Task 7: Battery Technology Distribution
- **Sheet Name**: `Battery_Tech_Distribution`
- **Marks Card**: Pie or Donut Chart.
- **Color**: `BatteryType` (Enforce consistent palette):
  - **LFP**: Teal `#4E79A7`
  - **NMC**: Navy `#2B5C8F`
  - **NCA**: Orange `#F28E2B`
  - **Sodium-Ion**: Yellow/Amber `#EDC948`
  - **Solid-State**: Emerald `#59A14F`
- **Angle**: `SUM(AnnualSales)`
- **Label**: `BatteryType` + `% of Total`.

### Task 8: Driving Range by Category & Battery Type
- **Sheet Name**: `Driving_Range_by_Category_Battery`
- **Columns**: `VehicleCategory`
- **Rows**: `AVG(DrivingRange)`
- **Color**: `BatteryType`
- **Mark**: Side-by-side Bar / Box Plot.
- **Tooltip**: Include `AVG(BatteryCapacity)` and `AVG(ChargingTimeMinutes)`.

---

## E6: Manufacturing & Customer Satisfaction (Tasks 9–10)

### Task 9: Global Manufacturing Country Map
- **Sheet Name**: `Manufacturing_Country_Map`
- **Latitude & Longitude**: Generated automatically via `ManufacturingCountry`.
- **Detail**: `ManufacturingCountry`
- **Color**: `SUM(AnnualSales)` (Sequential Blue/Green gradient).
- **Size / Label**: `CNT(Model)` (Number of active EV models manufactured).

### Task 10: Customer Rating by Category and Manufacturer
- **Sheet Name**: `Customer_Rating_by_Category_Manufacturer`
- **Columns**: `VehicleCategory`
- **Rows**: `Manufacturer`
- **Color**: `AVG(CustomerRating)` (Diverging Red-to-Green, 3.5 to 5.0).
- **Mark**: Square (Heatmap matrix).
- **Label**: `AVG(CustomerRating)`.

---

## E7: Persona Dashboards (Tasks 11–13)
*Canvas Size: Fixed 1200 x 850 px.*

### Dashboard 1: Executive Strategy
**Target Persona**: Emily Johnson (Market Strategy Director)
- **Top**: KPI Summary Cards.
- **Middle Left**: `Sales_by_Category` (High-growth segments).
- **Middle Right**: `Sales_and_MarketShare_by_Manufacturer`.
- **Bottom**: `Battery_Tech_Distribution` & `Customer_Rating_by_Category_Manufacturer`.

### Dashboard 2: Competitive Intelligence
**Target Persona**: David Chen (BI Manager)
- **Top**: Manufacturer Volume & Market Share Treemap.
- **Middle**: `Manufacturing_Country_Map` (Global footprint).
- **Bottom**: `Customer_Rating_by_Category_Manufacturer` (Competitive benchmark).

### Dashboard 3: Technology Research
**Target Persona**: Dr. Sarah Williams (Sustainable Mobility Analyst)
- **Top**: `Battery_Tech_Distribution` (Adoption of Sodium-Ion & Solid-State).
- **Middle**: `Driving_Range_by_Category_Battery`.
- **Bottom**: Range improvement trend over time & Charging speed analysis.

---

## E8: Interactive Filters & Publishing (Task 14)
1. **Global Shared Filters**:
   - Add filters for `Year`, `VehicleCategory`, `Manufacturer`, `BatteryType`, and `ManufacturingCountry`.
   - Apply to: **All Using This Data Source**.
2. **Cross-filtering Action**:
   - Enable **Use as Filter** on `Sales_by_Category` and `Manufacturing_Country_Map`.
3. **Publishing**:
   - Select **Server > Tableau Public > Save to Tableau Public As...**
   - Save as `EV Market Analysis Dashboard`.
