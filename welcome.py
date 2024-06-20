import streamlit as st

# Function to display Welcome page
def show_welcome_page():
    # Set page width and center content
    st.markdown(
        f"""
        <style>
            .reportview-container .main .block-container {{
                max-width: 800px;
                padding-top: 2rem;
                padding-right: 2rem;
                padding-left: 2rem;
                padding-bottom: 5rem;
            }}
            .title-container {{
                text-align: center;
                margin-bottom: 2rem;
            }}
            .title {{
                font-size: 60px;
                color: #333333;
                text-transform: uppercase;
                animation: move 2s infinite alternate; /* Animate the title */
            }}
            @keyframes move {{
                from {{ transform: translateX(-5px); }}
                to {{ transform: translateX(5px); }}
            }}
            .description {{
                text-align: center;
                font-size: 18px;
                color: #666666;
                margin-bottom: 2rem;
            }}
            .contact-info {{
                text-align: center;
                margin-top: 2rem;
            }}
            .contact-info h3 {{
                font-size: 24px;
                color: #333333;
                margin-bottom: 1rem;
            }}
            .contact-info p {{
                font-size: 18px;
                color: #666666;
                margin-bottom: 0.5rem;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    # Welcome title
    st.markdown("<div class='title-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='title'>WELCOME TO ANALYTICART</h1>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)  # Horizontal line
    
    # Description
    st.markdown(
        """
        <div class="description">
            Welcome to our online store! We offer a wide range of products to meet all your shopping needs. 
            Explore our catalog, add items to your cart, and enjoy a seamless shopping experience.
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Image
    st.image("grocery.jpg", caption="ANALYTICART", use_column_width=True)
    
    # Contact information
    st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
    st.markdown("<h3>Contact Us:</h3>", unsafe_allow_html=True)
    st.markdown("<p>Email: analyticart@example.com</p>", unsafe_allow_html=True)
    st.markdown("<p>Phone: +123 456 7890</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Example usage
show_welcome_page()

