import streamlit as st
import pandas as pd
from datetime import datetime
import os

def view_checkout(products):
    st.header("Checkout")
    if st.session_state.cart:
        total = 0
        for item, quantity in st.session_state.cart:
            price = products[item]['price']
            st.write(f"{item} - Quantity: {quantity} - Price per item: ${price} - Total: ${price * quantity}")
            total += price * quantity
        st.write(f"Total Price: ${total}")

        mobile_number = st.text_input("Enter your mobile number:")
        pin = st.text_input("Enter PIN:", type="password")

        if st.button("Proceed to Pay", key="proceed_to_pay"):
            if not mobile_number.isdigit() or len(mobile_number) != 10:
                st.error("Please enter a valid 10-digit mobile number.")
            elif pin != "1234":
                st.error("Invalid PIN. Please try again.")
            else:
                save_to_database_and_excel(st.session_state.cart, mobile_number)
                st.success("Payment successful!")
                st.session_state.cart.clear()
    else:
        st.write("Your cart is empty.")

def save_to_database_and_excel(cart, mobile_number):
    data = []
    transaction_date = datetime.now().strftime("%Y-%m-%d")

    for item, quantity in cart:
        data.append({
            "Mobile Number": mobile_number,
            "Transaction Date": transaction_date,
            "Item": item,
            "Quantity": quantity
        })

    df = pd.DataFrame(data)

    # Save to Excel
    book_file = "web.xlsx"
    if os.path.exists(book_file):
        existing_df = pd.read_excel(book_file)
        df = pd.concat([existing_df, df], ignore_index=True)
    df.to_excel(book_file, index=False)



