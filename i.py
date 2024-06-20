import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import streamlit as st

def demand_forecast():
    """
    Performs demand forecasting using XGBoost model and visualizes the results.

    Returns:
        None
    """

    # Load the dataset from minipro.xlsx
    df = pd.read_excel('minipro.xlsx')

    # Convert the 'Day' column to datetime
    df['Day'] = pd.to_datetime(df[['Year', 'Month', 'Day']])

    # Prepare the data for forecasting
    df['day_of_week'] = df['Day'].dt.dayofweek
    df['month'] = df['Day'].dt.month
    df['year'] = df['Day'].dt.year
    df['day'] = df['Day'].dt.day

    # Aggregate sales data by day
    daily_sales = df.groupby(['Day', 'Item Name'])['Qty'].sum().reset_index()

    # Dropdown menu to select item
    selected_item = st.selectbox('Select Item', daily_sales['Item Name'].unique())

    # Filter data for selected item
    item_sales = daily_sales[daily_sales['Item Name'] == selected_item]
    item_sales = item_sales.set_index('Day').asfreq('D').fillna(0)

    # Feature engineering
    item_sales['lag_1'] = item_sales['Qty'].shift(1).fillna(0)
    item_sales['lag_7'] = item_sales['Qty'].shift(7).fillna(0)
    item_sales['rolling_mean_7'] = item_sales['Qty'].rolling(7).mean().fillna(0)

    # Split data into features and target variable
    X = item_sales[['lag_1', 'lag_7', 'rolling_mean_7']]
    y = item_sales['Qty']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    # Train XGBoost model
    model = xgb.XGBRegressor(objective='reg:squarederror')
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate model
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    # Display forecast
    st.write(f"Forecast for {selected_item} (R^2 Score: {r2:.2f}, MSE: {mse:.2f}):")
    forecast = model.predict(X)
    plt.figure(figsize=(10, 5))
    plt.plot(item_sales.index, item_sales['Qty'], label='Actual', color='blue')
    plt.plot(item_sales.index, forecast, label='Forecast', color='red')
    plt.title(f"Demand Forecast for {selected_item}")
    plt.xlabel("Date")
    plt.ylabel("Quantity")
    plt.legend()
    st.pyplot(plt)

# Call the demand forecast function
demand_forecast()
