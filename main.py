import streamlit as st
from cart import view_cart, add_to_cart
from checkout import view_checkout, save_to_database_and_excel
from welcome import show_welcome_page
from about import show_about_us
from contact import show_contact_us
from raffle import show_raffle_draw
from charity import show_charity_content
from policies import show_policies
import json
import os
from stati import ai_module
from stati import demand_forecast
from stati import display
from stati import showstat
from restock import new

# Load products from JSON file
def load_products():
    products_file = "product.json"
    if os.path.exists(products_file):
        with open(products_file, "r") as f:
            return json.load(f)
    else:
        return {
            "550 fils kitchen plastic & glassware items": {
                "price": 110.01,
                "description": "Plastic glassware items refer to drinkware made from various types of plastic materials rather than glass.",
                "image": "550 FILS KITCHEN PLASTIC & GLASSWARE ITEMS.jpg",
                "quantity": 30
            },
            "Arwa Water 500mL": {
                "price": 22.00,
                "description": "It is produced by Coca-Cola Bottling Company and is recognized for its purity and high quality.",
                "image": "arwa.jpg",
                "quantity": 30
            },
            "Aquafina water 250mL": {
                "price": 11.00,
                "description": "Aquafina is a well-known bottled water brand owned by PepsiCo.",
                "image": "aquafina.jpg",
                "quantity": 30
            },
            "Al Kawthar Water 6x1.5L": {
                "price": 93.51,
                "description": "Al Kawthar Water is recognized for its quality and accessibility, making it a popular choice ",
                "image": "AL KAWTHAR WATER .jpg",
                "quantity": 30
            },
            "reduce to clear items 300 fils": {
                "price": 60.00,
                "description": "Description of reduce to clear items 300 fils",
                "image": "REDUCE TO CLEAR ITEMS 150 FILS.jpg",
                "quantity": 30
            },
            "al marzook lebanese bread white 5pcs/pk": {
                "price": 22.00,
                "description": "Al Marzook Lebanese is likely referring to a specific brand, business, or product line associated with Lebanese cuisine or culture.",
                "image": "whitebread.jpg",
                "quantity": 30
            },
            "pepsi plastic 400ml": {
                "price": 40.00,
                "description": "Pepsi is a globally recognized carbonated soft drink brand owned by PepsiCo.",
                "image": "pepsi.jpg",
                "quantity": 30
            },
            "abion i/c gold cone vanilla": {
                "price": 68.10,
                "description": "Abion Gold Cone Vanilla is likely referring to a specific brand or product of vanilla-flavored ice cream cones. ",
                "image": "gold.jpg",
                "quantity": 30
            },
            "mirinda citrus 330ml": {
                "price": 50.00,
                "description": "Mirinda Citrus is a popular flavor variant of the Mirinda soft drink brand, which is owned by PepsiCo.l",
                "image": "mirinda.jpg",
                "quantity": 30
            },
            "mirinda citrus plastic 400ml": {
                "price": 40.00,
                "description": "Mirinda Citrus is a popular flavor variant of the Mirinda soft drink brand, which is owned by PepsiCo.",
                "image": "mirinda_bottle.jpg",
                "quantity": 30
            },
            "arwa water 1.5ltr": {
                "price": 143.01,
                "description": "It is produced by Coca-Cola Bottling Company and is recognized for its purity and high quality.",
                "image": "ARWA WATER 1500ML.jpg",
                "quantity": 30
            },
            "o.k. potato crisps ready salted 30gm": {
                "price": 27.00,
                "description": "Potato chips are a popular snack food made from thin slices of potatoes that are fried or baked until crispy. ",
                "image": "O.K. POTATO CRISPS READY SALTED 30GM.jpg",
                "quantity": 30
            }
        }

products = load_products()

# Initialize session state for the cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Function to view the catalog
def view_catalog():
    st.header("WELCOME TO ANALYTICART .....")
    st.header("Catalog")
    for product, details in products.items():
        st.subheader(product)
        image_path = details["image"]
        if image_path:
            st.image(image_path, width=150, caption="Product Image")
        st.write(details["description"])
        st.write(f"Price: ${details['price']}")
        st.write(f"Available Quantity: {details['quantity']}")
        quantity = st.number_input(f"Quantity of {product}", min_value=1, max_value=details["quantity"], step=1, key=f"quantity_{product}")
        if st.button(f"Add {product} to Cart", key=f"add_{product}"):
            add_to_cart(product, quantity, products)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Welcome", "Catalog", "Cart", "About us", "Contact us", "Raffle draw", "Policies", "Charity","Statistics","restock"])

# Page routing
if page == "Welcome":
    show_welcome_page()
elif page == "Catalog":
    view_catalog()
elif page == "Cart":
    view_checkout(products)# Assuming you have access to the products variable
elif page == "About us":
    show_about_us()
elif page == "Contact us":
    show_contact_us()
elif page == "Raffle draw":
    show_raffle_draw()
elif page == "Policies":
    show_policies()
elif page == "Charity":
    show_charity_content()
elif page == "Statistics":
    showstat()
elif page == "restock":
    new()
