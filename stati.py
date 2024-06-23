import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import shutil
from i import demand_forecast

# Copy the file
source_file = "web.xlsx"
destination_file = "news.xlsx"
shutil.copyfile(source_file, destination_file)
print(f"File '{source_file}' copied to '{destination_file}' successfully.")

def ai_module():
    # Load dataset
    df = pd.read_excel('mainpro.xlsx')

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Convert 'Transaction Date' to datetime
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

    # Feature Engineering for datetime column
    df['year'] = df['Transaction Date'].dt.year
    df['month'] = df['Transaction Date'].dt.month
    df['day'] = df['Transaction Date'].dt.day

    # Drop original datetime column
    df.drop('Transaction Date', axis=1, inplace=True)

    # Encoding categorical variables
    encoder = OneHotEncoder(drop='first', sparse_output=False)  # Changed to sparse=False for compatibility
    encoded_cols = encoder.fit_transform(df[['Item']])
    encoded_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(['Item']))
    df_encoded = pd.concat([df, encoded_df], axis=1)
    df_encoded.drop('Item', axis=1, inplace=True)

    # Removing outliers using IQR method
    Q1 = df_encoded.quantile(0.25)
    Q3 = df_encoded.quantile(0.75)
    IQR = Q3 - Q1
    df_no_outliers = df_encoded[~((df_encoded < (Q1 - 1.5 * IQR)) | (df_encoded > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Split data into features and target variable
    X = df_no_outliers.drop('Quantity', axis=1)
    y = df_no_outliers['Quantity']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scaling numerical features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Initialize Gradient Boosting Regressor
    gb_model = GradientBoostingRegressor(random_state=42)

    # Hyperparameter tuning for GradientBoostingRegressor
    param_grid_gb = {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.05, 0.1, 0.2],
        'max_depth': [3, 5, 7]
    }

    grid_search_gb = GridSearchCV(estimator=gb_model, param_grid=param_grid_gb, cv=3, scoring='neg_mean_squared_error', verbose=1, n_jobs=-1)
    grid_search_gb.fit(X_train_scaled, y_train)

    print("Best Parameters for GradientBoostingRegressor:", grid_search_gb.best_params_)
    print("Best RMSE for GradientBoostingRegressor:", np.sqrt(-grid_search_gb.best_score_))

    best_gb_model = grid_search_gb.best_estimator_

    # Make predictions with Gradient Boosting model
    predictions_gb = best_gb_model.predict(X_test_scaled)

    # Evaluate Gradient Boosting model
    rmse_gb = np.sqrt(mean_squared_error(y_test, predictions_gb))
    r2_gb = r2_score(y_test, predictions_gb)
    mae_gb = mean_absolute_error(y_test, predictions_gb)

    # Create DataFrame with actual and predicted values
    results = pd.DataFrame({'Actual': y_test.values, 'Predicted': predictions_gb})

    # Plot actual vs predicted values
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(results.index, results['Actual'], label='Actual', marker='o', color='green')
    ax.plot(results.index, results['Predicted'], label='Predicted', marker='x')
    ax.set_xlabel('Index')
    ax.set_ylabel('Quantity')
    ax.set_title('Actual vs Predicted Quantity')
    ax.legend()
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(fig)

    # Baseline model: Use mean of the target variable as predictions
    baseline_predictions = np.full_like(y_test, fill_value=y_train.mean())

    # Calculate RMSE for baseline model
    baseline_rmse = np.sqrt(mean_squared_error(y_test, baseline_predictions))

    # Compare RMSE scores
    st.write(f'RMSE Score (Model): {rmse_gb:.2f}')
    st.write(f'R-squared Score (Model): {r2_gb:.2f}')
    st.write(f'Mean Absolute Error (MAE): {mae_gb:.2f}')
    st.write(f'RMSE Score (Baseline): {baseline_rmse:.2f}')

    # Provide context-based evaluation
    if rmse_gb < baseline_rmse:
        st.write("The model's RMSE is lower than the baseline, indicating better performance.")
    elif rmse_gb > baseline_rmse:
        st.write("The model's RMSE is higher than the baseline, indicating worse performance.")
    else:
        st.write("The model's RMSE is equal to the baseline.")

def display():
    st.title("Sales Analysis and Average Daily Sales Calculator")
    st.write("### Upload the datasets (Excel files)")

    @st.cache_data(ttl=60)
    def load_data_sales():
        """
        Load the sales dataset.
        """
        return pd.read_excel("minipro.xlsx")

    @st.cache_data(ttl=60)
    def load_data_customers():
        """
        Load the customers dataset.
        """
        return pd.read_excel("web.xlsx")

    df_sales = load_data_sales()
    df_customers = load_data_customers()

    # Calculate average daily sales
    total_quantity_sales = df_sales.groupby('Item Name')['Qty'].sum()
    total_days_sold = df_sales.groupby('Item Name')['Day'].nunique()
    average_daily_sales = total_quantity_sales / total_days_sold

    # Convert average daily sales to integers
    average_daily_sales = average_daily_sales.astype(int)

    # Display average daily sales
    st.write("### Average Daily Sales for Each Product")
    st.write(average_daily_sales)

    # Group the data by item to calculate total quantity sold for each product
    total_sales_by_item = df_customers.groupby('Item')['Quantity'].sum()

    # Artistic bar chart showing average daily sales for each product
    st.write("### Bar Chart - Average Daily Sales for Each Product")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(y=average_daily_sales.index, x=average_daily_sales.values, hue=average_daily_sales.index, palette='viridis', ax=ax, dodge=False)
    ax.set_xlabel('Average Daily Sales')
    ax.set_ylabel('Product')
    ax.set_title('Average Daily Sales for Each Product', fontsize=16)
    ax.grid(axis='x')
    for i in ax.containers:
        ax.bar_label(i,)
    st.pyplot(fig)

    # Artistic bar chart showing total sales for each product
    st.write("### Bar Chart - Total Sales for Each Product")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.barplot(y=total_sales_by_item.index, x=total_sales_by_item.values, hue=total_sales_by_item.index, palette='plasma', ax=ax, dodge=False)
    ax.set_xlabel('Total Sales')
    ax.set_ylabel('Product')
    ax.set_title('Total Sales for Each Product', fontsize=16)
    ax.grid(axis='x')
    for i in ax.containers:
        ax.bar_label(i,)
    st.pyplot(fig)

    # Group the data by mobile number to calculate total quantity purchased by each customer
    total_quantity_by_customer = df_customers.groupby('Mobile Number')['Quantity'].sum()

    # Identify the top 5 customers based on quantity purchased
    top_customers = total_quantity_by_customer.nlargest(5)

    # Display the top 5 customers
    st.write("### Top 5 Customers Based on Quantity Purchased")
    st.write(top_customers)

    # Artistic pie chart for top 5 customers
    st.write("### Pie Chart - Top 5 Customers Based on Quantity Purchased")
    fig, ax = plt.subplots(figsize=(8, 8))
    top_customers.plot(kind='pie', autopct='%1.1f%%', ax=ax, colors=sns.color_palette('pastel'))
    ax.set_ylabel('')
    ax.set_title('Top 5 Customers Based on Quantity Purchased', fontsize=16)
    st.pyplot(fig)

    # Add a refresh button to manually refresh the data
    if st.button("Refresh Data"):
        st.experimental_rerun()
    def showstat():
    st.title("Sales Analysis, Demand Forecasting, and AI Module")

    # Create a select box in the sidebar to choose the functionality
    selected_option = st.sidebar.selectbox("Select Functionality", ["Display Sales", "AI Module", "Demand Forecast"])


    # Execute the selected functionality
    if selected_option == "Display Sales":
        display()
    elif selected_option == "AI Module":
        ai_module()
    elif selected_option == "Demand Forecast":
        demand_forecast()
# Run the Streamlit app
if __name__ == '__main__':
    showstat()
