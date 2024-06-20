import streamlit as st
import json

# Function to add items to the cart
def add_to_cart(product_name, quantity, products):
    if quantity <= products[product_name]['quantity']:
        st.session_state.cart.append((product_name, quantity))
        products[product_name]['quantity'] -= quantity
        save_products(products)
        st.success(f"{quantity} of {product_name} added to cart!")
    else:
        st.error("Insufficient stock!")

# Function to save products to a JSON file
def save_products(products):
    with open("product.json", "w") as f:
        json.dump(products, f, indent=4)

# Function to view the cart
def view_cart(products):
    st.header("Cart")
    if st.session_state.cart:
        total = 0
        for item, quantity in st.session_state.cart:
            price = products[item]['price']
            st.write(f"{item} - Quantity: {quantity} - Price per item: ${price} - Total: ${price * quantity}")
            total += price * quantity
        st.write(f"Total Price: ${total}")
    else:
        st.write("Your cart is empty.")
