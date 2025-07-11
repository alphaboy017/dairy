#!/usr/bin/env python3
"""
Test script for the Dairy Supply & Demand Forecasting application
"""

import pandas as pd
import numpy as np
import sys
import os

def test_data_loading():
    """Test if the dataset can be loaded correctly"""
    print("🧪 Testing data loading...")
    
    try:
        # Load the dataset
        df = pd.read_csv('Dairy_Supply_Demand_20000.csv')
        print(f"✅ Dataset loaded successfully: {len(df)} records")
        
        # Check required columns
        required_columns = [
            'Date', 'Milk_Supply_Liters', 'Downtime_Hours',
            'Milk_500ml_Demand', 'Milk_500ml_Inventory',
            'Milk_1L_Demand', 'Milk_1L_Inventory',
            'Butter_Demand', 'Butter_Inventory',
            'Cheese_Demand', 'Cheese_Inventory',
            'Yogurt_Demand', 'Yogurt_Inventory'
        ]
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"❌ Missing columns: {missing_columns}")
            return False
        else:
            print("✅ All required columns present")
        
        # Check data types
        df['Date'] = pd.to_datetime(df['Date'])
        print("✅ Date column converted to datetime")
        
        # Check for missing values
        missing_values = df.isnull().sum()
        if missing_values.sum() > 0:
            print(f"⚠️  Missing values found: {missing_values[missing_values > 0].to_dict()}")
        else:
            print("✅ No missing values found")
        
        # Basic statistics
        print(f"📊 Date range: {df['Date'].min()} to {df['Date'].max()}")
        print(f"📊 Total milk supply: {df['Milk_Supply_Liters'].sum():,.0f} liters")
        print(f"📊 Average daily supply: {df['Milk_Supply_Liters'].mean():,.0f} liters")
        
        return True
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return False

def test_dependencies():
    """Test if all required dependencies can be imported"""
    print("\n🧪 Testing dependencies...")
    
    required_packages = [
        'streamlit', 'pandas', 'numpy', 'plotly', 'matplotlib', 
        'seaborn', 'sklearn', 'xgboost', 'lightgbm', 'prophet'
    ]
    
    failed_imports = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {failed_imports}")
        print("Please install missing packages: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All dependencies available")
        return True

def test_data_processing():
    """Test data processing functions"""
    print("\n🧪 Testing data processing...")
    
    try:
        # Load and process data
        df = pd.read_csv('Dairy_Supply_Demand_20000.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')
        
        # Add derived features
        df['DayOfWeek'] = df['Date'].dt.dayofweek
        df['Month'] = df['Date'].dt.month
        df['Quarter'] = df['Date'].dt.quarter
        df['Year'] = df['Date'].dt.year
        
        # Calculate capacity utilization
        df['Total_Demand'] = (df['Milk_500ml_Demand'] + df['Milk_1L_Demand'] + 
                             df['Butter_Demand'] + df['Cheese_Demand'] + df['Yogurt_Demand'])
        df['Total_Inventory'] = (df['Milk_500ml_Inventory'] + df['Milk_1L_Inventory'] + 
                                df['Butter_Inventory'] + df['Cheese_Inventory'] + df['Yogurt_Inventory'])
        
        df['Demand_Supply_Ratio'] = df['Total_Demand'] / df['Milk_Supply_Liters']
        df['Inventory_Turnover'] = df['Total_Demand'] / df['Total_Inventory']
        df['Capacity_Utilization'] = (df['Total_Demand'] / (df['Total_Demand'] + df['Total_Inventory'])) * 100
        
        print("✅ Data processing completed successfully")
        print(f"📊 Average capacity utilization: {df['Capacity_Utilization'].mean():.1f}%")
        print(f"📊 Average demand-supply ratio: {df['Demand_Supply_Ratio'].mean():.2f}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in data processing: {e}")
        return False

def test_ml_models():
    """Test if ML models can be trained"""
    print("\n🧪 Testing ML models...")
    
    try:
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.metrics import mean_squared_error
        
        # Load and prepare data
        df = pd.read_csv('Dairy_Supply_Demand_20000.csv')
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')
        
        # Simple feature engineering
        df['DayOfWeek'] = df['Date'].dt.dayofweek
        df['Month'] = df['Date'].dt.month
        df['Total_Demand'] = (df['Milk_500ml_Demand'] + df['Milk_1L_Demand'] + 
                             df['Butter_Demand'] + df['Cheese_Demand'] + df['Yogurt_Demand'])
        
        # Prepare features
        features = ['DayOfWeek', 'Month', 'Milk_Supply_Liters', 'Downtime_Hours']
        X = df[features].dropna()
        y = df['Total_Demand'].dropna()
        
        # Align X and y
        common_index = X.index.intersection(y.index)
        X = X.loc[common_index]
        y = y.loc[common_index]
        
        if len(X) < 100:
            print("❌ Insufficient data for training")
            return False
        
        # Train a simple model
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestRegressor(n_estimators=10, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        
        print("✅ ML model training completed successfully")
        print(f"📊 Test RMSE: {rmse:.2f}")
        print(f"📊 Training samples: {len(X_train)}")
        print(f"📊 Test samples: {len(X_test)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in ML model testing: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Starting Dairy Forecasting Application Tests\n")
    
    tests = [
        ("Data Loading", test_data_loading),
        ("Dependencies", test_dependencies),
        ("Data Processing", test_data_processing),
        ("ML Models", test_ml_models)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{'='*50}")
        print(f"Running {test_name} Test")
        print('='*50)
        
        if test_func():
            passed += 1
            print(f"✅ {test_name} test PASSED")
        else:
            print(f"❌ {test_name} test FAILED")
    
    print(f"\n{'='*50}")
    print(f"Test Results: {passed}/{total} tests passed")
    print('='*50)
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to run.")
        print("\nTo start the application:")
        print("streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main() 