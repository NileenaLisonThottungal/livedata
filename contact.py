import streamlit as st

# Function to display Contact Us section
def show_contact_us():
    # Custom CSS styling
    st.markdown(
        """
        <style>
            .contact-container {
                background-color: #f0f0f0;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
            }
            .contact-title {
                text-align: center;
                font-size: 36px;
                color: #333333;
                margin-bottom: 30px;
            }
            .contact-info {
                text-align: center;
                margin-top: 30px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Contact Us container
    st.markdown("<div class='contact-container'>", unsafe_allow_html=True)

    # Title
    st.markdown("<h1 class='contact-title'>Contact Us</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Contact information
    st.markdown(
        """
        <div class='contact-info'>
            <p>PINCODE 678908</p>
            <p>CR no: 7328399728/90</p>
            <p>Tel: 23323232</p>
            <p>Email: analyticart@gmail.com</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Regional Office
    st.markdown("<h3>Regional Office</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='contact-info'>
            <p>PINCODE: 678908</p>
            <p>D Road, Kerala</p>
            <p>Tel: 35363636</p>
            <p>Email: customercare@in.analyticart.com</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # End of Contact Us container
    st.markdown("</div>", unsafe_allow_html=True)

# Example usage
show_contact_us()
