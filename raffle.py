import streamlit as st
import random

# Function to display Raffle Draw section
def show_raffle_draw():
    # Custom CSS styling
    st.markdown(
        """
        <style>
            .raffle-container {
                background-color: #f0f0f0;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
            }
            .raffle-title {
                text-align: center;
                font-size: 36px;
                color: #333333;
                margin-bottom: 30px;
            }
            .raffle-option {
                text-align: center;
                margin-top: 30px;
            }
            .raffle-option h3 {
                font-size: 24px;
                color: #333333;
                margin-bottom: 10px;
            }
            .raffle-option p {
                font-size: 18px;
                color: #666666;
                margin-bottom: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Raffle Draw container
    st.markdown("<div class='raffle-container'>", unsafe_allow_html=True)

    # Title
    st.markdown("<h1 class='raffle-title'>Raffle Draw</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Raffle options
    option = st.radio("Select an Option:", ["Prizes", "Entry", "Winners"])
    
    # Display content based on selected option
    if option == "Prizes":
        st.write("PRIZES ARE--")
        st.write("1st prize is car & Qr 10,000")
        st.write("2nd prize is bike & Qr 1,000")
        st.write("3rd prize is Laptop & Qr 1,000 gift voucher")
    elif option == "Entry":
        n = st.text_input("Enter your name:")
        e = st.text_input("Enter your email id:")
        if st.button("Submit Entry"):
            lucky_number = random.randint(1, 100)
            st.write(f"Your lucky number is: {lucky_number}")
    elif option == "Winners":
        st.write("Lucky number of the 1st prize winner is:", random.randint(1, 100))
        st.write("Lucky number of the 2nd prize winner is:", random.randint(1, 100))
        st.write("Lucky number of the 3rd prize winner is:", random.randint(1, 100))

    # End of Raffle Draw container
    st.markdown("</div>", unsafe_allow_html=True)

# Example usage
show_raffle_draw()
