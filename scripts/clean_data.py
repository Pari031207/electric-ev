"""
Data Cleaning and Feature Engineering for EV Market Analysis Dashboard
Epic 1: Data Preparation & Derived Fields
"""
import pandas as pd
import numpy as np

def clean_ev_data(input_csv="data/raw_ev_data.csv", output_csv="data/cleaned_ev_data.csv"):
    df = pd.read_csv(input_csv)
    
    # 1. Deduplicate & Handle missing values
    df = df.drop_duplicates()
    df['BatteryCapacity'] = df['BatteryCapacity'].fillna(df['BatteryCapacity'].median())
    df['DrivingRange'] = df['DrivingRange'].fillna(df['DrivingRange'].median())
    df['Price'] = df['Price'].fillna(df['Price'].median())
    df['AnnualSales'] = df['AnnualSales'].fillna(0).astype(int)
    df['CustomerRating'] = df['CustomerRating'].fillna(df['CustomerRating'].mean()).round(2)
    
    # 2. Derive MarketShare % per year
    yearly_totals = df.groupby('Year')['AnnualSales'].transform('sum')
    df['MarketSharePct'] = ((df['AnnualSales'] / yearly_totals) * 100).round(2)
    
    # 3. Derive Sales Growth % (YoY)
    df_sorted = df.sort_values(by=['Manufacturer', 'Model', 'Year'])
    df['SalesGrowthPct'] = df_sorted.groupby(['Manufacturer', 'Model'])['AnnualSales'].pct_change() * 100
    df['SalesGrowthPct'] = df['SalesGrowthPct'].fillna(0.0).round(1)
    
    df.to_csv(output_csv, index=False)
    print(f"Data successfully cleaned and saved to {output_csv}. Total records: {len(df)}")

if __name__ == "__main__":
    clean_ev_data()
