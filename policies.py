import streamlit as st

def show_policies():
    st.markdown(
        """
        <style>
            .policy-container {
                background-color: #f0f0f0;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
            }
            .policy-title {
                text-align: center;
                font-size: 36px;
                color: #333333;
                margin-bottom: 30px;
            }
            .policy-content {
                font-size: 18px;
                color: #333333;
                line-height: 1.6;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Policies dropdown
    policies = [
        "Select a policy",
        "Terms and Conditions",
        "Return Policy",
        "Privacy Policy",
        "Service and Warranty"
    ]
    selected_policy = st.selectbox("Select a Policy", policies)

    # Display content based on selection
    if selected_policy == "Terms and Conditions":
        st.markdown("<div class='policy-container'>", unsafe_allow_html=True)
        st.markdown("<h1 class='policy-title'>Terms and Conditions</h1>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='policy-content'>
            Welcome to our grocery store! By shopping with us, you agree to abide by the following terms and conditions:

            1. **Product Availability:** We strive to keep all products listed on our website in stock. However, due to high demand or unforeseen circumstances, certain items may be temporarily unavailable. We appreciate your understanding in such cases.

            2. **Pricing:** We aim to maintain accurate pricing for all items. In case of any discrepancy, the price at the checkout will prevail.

            3. **Quality Assurance:** We ensure the quality and freshness of our products. If you're unsatisfied with the quality of any item, please contact us for a refund or replacement.

            4. **Payment:** We accept various forms of payment, including credit/debit cards and cash on delivery.

            5. **Delivery:** Our delivery service operates within specified areas and timeframes. Kindly provide accurate delivery information to avoid delays.

            Thank you for choosing us for your grocery needs!
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    elif selected_policy == "Return Policy":
        st.markdown("<div class='policy-container'>", unsafe_allow_html=True)
        st.markdown("<h1 class='policy-title'>Return Policy</h1>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='policy-content'>
            We want you to be completely satisfied with your purchase. If you're not happy with any item, you may return it under the following conditions:

            1. **Damaged or Defective Products:** If any product is received damaged or defective, please contact us within 24 hours of delivery for a refund or replacement.

            2. **Incorrect Items:** In case you receive an incorrect item, we'll arrange for a return and replacement at no extra cost.

            3. **Change of Mind:** Unfortunately, we cannot accept returns for items due to a change of mind.

            Please ensure that returned items are unused and in their original packaging.

            Thank you for understanding!
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    elif selected_policy == "Privacy Policy":
        st.markdown("<div class='policy-container'>", unsafe_allow_html=True)
        st.markdown("<h1 class='policy-title'>Privacy Policy</h1>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='policy-content'>
            At our grocery store, we prioritize the privacy and security of our customers' information. Here's how we handle your data:

            1. **Information Collection:** We collect personal information such as name, address, and contact details for order processing and delivery purposes.

            2. **Data Security:** Your data is stored securely and is accessible only to authorized personnel involved in order fulfillment.

            3. **Third-party Disclosure:** We do not share your information with third parties except for delivery purposes or when required by law.

            4. **Opt-out Option:** You may choose to opt out of marketing communications at any time by contacting our customer support.

            By shopping with us, you consent to the collection and use of your information as outlined in this policy.

            Thank you for trusting us with your information!
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

    elif selected_policy == "Service and Warranty":
        st.markdown("<div class='policy-container'>", unsafe_allow_html=True)
        st.markdown("<h1 class='policy-title'>Service and Warranty</h1>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class='policy-content'>
            We stand behind the quality of our products. Here's what you need to know about our service and warranty:

            1. **Product Guarantee:** We guarantee the freshness and quality of all our products. If you're dissatisfied with any item, please contact us for a refund or replacement.

            2. **Warranty:** Certain products may come with manufacturer warranties. Please refer to the product description or contact us for warranty details.

            3. **Customer Support:** Our customer support team is available to assist you with any queries or issues regarding our products and services.

            Your satisfaction is our priority!
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

# Example usage
show_policies()
