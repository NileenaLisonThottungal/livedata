import streamlit as st

# Function to display Charity content
def show_charity_content():
    # Custom CSS styling
    st.markdown(
        """
        <style>
            .charity-container {
                background-color: #f0f0f0;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
            }
            .charity-title {
                text-align: center;
                font-size: 36px;
                color: #333333;
                margin-bottom: 30px;
            }
            .input-field {
                width: 100%;
                padding: 10px;
                font-size: 16px;
                margin-bottom: 20px;
                border: 1px solid #cccccc;
                border-radius: 5px;
            }
            .submit-button {
                display: block;
                width: 100%;
                padding: 10px;
                font-size: 18px;
                text-align: center;
                background-color: #0084ff;
                color: #ffffff;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            .submit-button:hover {
                background-color: #0056b3;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Charity container
    st.markdown("<div class='charity-container'>", unsafe_allow_html=True)

    # Title
    st.markdown("<h1 class='charity-title'>Charity</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Input fields
    account_number = st.text_input("Enter your Account Number:", key="account_number")
    amount = st.number_input("Enter the amount to be transferred", min_value=0, key="amount")
    otp = st.text_input("Enter your OTP:", key="otp", type="password")

    # Confirm Transaction button
    if st.button("Confirm Transaction", key="confirm-transaction"):
        if otp == "1234":
            st.success(f"Transaction successfully completed. Amount transferred: {amount}")
        else:
            st.error("Invalid OTP. Please try again.")

    # End of Charity container
    st.markdown("</div>", unsafe_allow_html=True)

# Example usage
show_charity_content()
