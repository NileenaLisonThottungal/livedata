import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBRegressor
from sklearn.preprocessing import LabelEncoder

# Function to increase quantity
def increase_quantity(product_name, increase_amount):
    with open('product.json', 'r') as f:
        product_data = json.load(f)

    if product_name in product_data:
        product_data[product_name]['quantity'] += increase_amount

        with open('product.json', 'w') as f:
            json.dump(product_data, f, indent=4)
        st.success(f"Quantity of {product_name} increased by {increase_amount}.")
    else:
        st.error(f"Product '{product_name}' not found in the database.")

    return product_data

# Function to preprocess data
def preprocess_data(df):
    df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
    df['Day'] = df['Transaction Date'].dt.day
    df['Month'] = df['Transaction Date'].dt.month
    df['Year'] = df['Transaction Date'].dt.year

    le = LabelEncoder()
    df['Item'] = le.fit_transform(df['Item'])

    return df

# Function to train model
def train_model(df):
    preprocessed_df = preprocess_data(df)
    X = preprocessed_df.drop(columns=['Transaction Date', 'Quantity'])
    y = preprocessed_df['Quantity']

    model = XGBRegressor()
    model.fit(X, y)

    return model

# Function to predict restock values
def predict_restock(web_df, mainpro_df, model):
    preprocessed_web_df = preprocess_data(web_df)
    if 'Mobile Number' in preprocessed_web_df.columns:
        preprocessed_web_df.drop(columns=['Mobile Number'], inplace=True)

    restock_predictions = model.predict(preprocessed_web_df.drop(columns=['Transaction Date', 'Quantity']))
    preprocessed_web_df['Restock Value'] = restock_predictions

    return preprocessed_web_df

# Main function
def new():
    st.title("Product Quantity Management")

    # Prompt user for a PIN to access the restock page
    pin = st.text_input("Enter PIN to access restock page", type="password")
    if st.button("Submit"):
        if pin == "4321":
            st.success("Access granted")
            st.sidebar.title("Increase Quantity")

            with open('product.json', 'r') as f:
                product_data = json.load(f)

            product_name = st.sidebar.selectbox("Select Product Name", list(product_data.keys()))
            increase_amount = st.sidebar.number_input("Enter Increase Amount", min_value=1, step=1)

            if st.sidebar.button("Increase Quantity"):
                product_data = increase_quantity(product_name, increase_amount)

            product_df = pd.DataFrame(product_data).T
            product_df.reset_index(inplace=True)
            product_df.columns = ['Product', 'Price', 'Description', 'Image', 'Quantity']

            st.subheader("Current Quantities")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.set_palette("pastel")
            bars = sns.barplot(x='Product', y='Quantity', data=product_df, ax=ax)
            plt.xticks(rotation=45, ha='right')
            plt.xlabel('Product Name')
            plt.ylabel('Quantity')
            plt.title('Current Quantities of Products')
            legend_labels = product_df['Product'].tolist()
            ax.legend(bars.patches, legend_labels, loc='upper right', bbox_to_anchor=(1.3, 1))
            st.pyplot(fig)

            mainpro_df = pd.read_excel('mainpro.xlsx')
            web_df = pd.read_excel('web.xlsx')
            model = train_model(mainpro_df)
            predicted_restock_web = predict_restock(web_df, mainpro_df, model)

            st.subheader("Restock Values for web.xlsx")
            fig_web, ax_web = plt.subplots(figsize=(10, 6))
            item_names = [str(item) for item in predicted_restock_web['Item'].unique()]
            x_values = range(len(item_names))
            ax_web.bar(x_values, predicted_restock_web.groupby('Item')['Restock Value'].sum(), color='skyblue', label='Restock Value')
            ax_web.set_xlabel('Item')
            ax_web.set_ylabel('Restock Value')
            ax_web.set_title('Web.xlsx - Restock Values')
            ax_web.set_xticks(x_values)
            ax_web.set_xticklabels(item_names, rotation=45, ha='right')
            ax_web.legend()
            st.pyplot(fig_web)

            st.subheader("Line Chart for mainpro.xlsx")
            fig_mainpro, ax_mainpro = plt.subplots(figsize=(10, 6))
            colors = sns.color_palette("husl", len(mainpro_df['Item'].unique()))
            for i, (item, color) in enumerate(zip(mainpro_df['Item'].unique(), colors)):
                item_df = mainpro_df[mainpro_df['Item'] == item]
                ax_mainpro.plot(item_df['Transaction Date'], item_df['Quantity'], marker='o', linestyle='-', color=color, label=item)
            plt.xlabel('Transaction Date')
            plt.ylabel('Quantity')
            plt.title('mainpro.xlsx - Quantity Over Time')
            ax_mainpro.legend(loc='upper left', bbox_to_anchor=(1, 1))
            st.pyplot(fig_mainpro)
        else:
            st.error("Incorrect PIN. Access denied.")


















