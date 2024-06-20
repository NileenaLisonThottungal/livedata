import streamlit as st

# Function to display About Us section
def show_about_us():
    # Custom CSS styling
    st.markdown(
        """
        <style>
            .about-container {
                background-color: #f0f0f0;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
            }
            .about-title {
                text-align: center;
                font-size: 36px;
                color: #333333;
                margin-bottom: 30px;
            }
            .company-info {
                text-align: center;
                margin-top: 30px;
            }
            .value-list {
                text-align: center;
                margin-top: 30px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # About Us container
    st.markdown("<div class='about-container'>", unsafe_allow_html=True)

    # Title
    st.markdown("<h1 class='about-title'>About Us</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # Company information
    st.markdown(
        """
        <div class='company-info'>
            Analyticart, the grocery division of a global conglomerate, sets the standard for the grocery industry. 
            With multiple stores worldwide, Analyticart is synonymous with quality grocery retailing and innovative shopping experiences.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class='company-info'>
            Our Vision: To be the global leader in online grocery retail, providing unparalleled value to customers and stakeholders.
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class='company-info'>
            Our Mission: To deliver exceptional grocery products and services, foster innovation, and create lasting value for our customers.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Values list
    st.markdown(
        """
        <div class='value-list'>
            <h3>Our Values:</h3>
            <ul>
                <li>Integrity</li>
                <li>Teamwork</li>
                <li>Accountability</li>
                <li>Innovation</li>
                <li>Commitment</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    # End of About Us container
    st.markdown("</div>", unsafe_allow_html=True)

# Example usage
show_about_us()

