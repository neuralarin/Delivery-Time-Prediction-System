import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model/delivero_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Delivero — Your delivery partner",
    page_icon="🚚",
    layout="centered"
)

# Title
st.markdown(
    """
    <h2 style="
        font-size: 45px;
        margin-bottom: 10px;
        white-space: nowrap;
    ">
        Delivero — Your delivery partner 🚚
    </h2>
    """,
    unsafe_allow_html=True
)

# Order details
st.markdown(
    """
    <h2 style="
        font-size: 20px;
        margin-bottom: 10px;
        white-space: nowrap;
    ">
        Order Details
    </h2>
    """,
    unsafe_allow_html=True
)

n_items = st.number_input(
    "Number of items",
    min_value=1,
    max_value=21,
    value=1
)

n_sellers = st.number_input(
    "Number of sellers",
    min_value=1,
    max_value=5,
    value=1
)

total_price = st.number_input(
    "Total price ($)",
    min_value=0.0,
    value=100.0
)

total_freight = st.number_input(
    "Total freight ($)",
    min_value=0.0,
    value=20.0
)

avg_price = st.number_input(
    "Average item price ($)",
    min_value=0.0,
    value=90.0
)

payment_value = st.number_input(
    "Payment value ($)",
    min_value=0.0,
    value=110.0
)

payment_installments = st.number_input(
    "Payment installments",
    min_value=0,
    max_value=24,
    value=1
)

product_weight_g = st.number_input(
    "Product weight (g)",
    min_value=0.0,
    value=700.0
)

product_length_cm = st.number_input(
    "Product length (cm)",
    min_value=0.0,
    value=25.0
)

product_height_cm = st.number_input(
    "Product height (cm)",
    min_value=0.0,
    value=13.0
)

product_width_cm = st.number_input(
    "Product width (cm)",
    min_value=0.0,
    value=20.0
)

distance_km = st.number_input(
    "Distance (km)",
    min_value=0.0,
    value=430.0
)

estimated_delivery_days = st.number_input(
    "Estimated delivery days (seller's estimate)",
    min_value=0.0,
    value=23.0
)


# Order timing
st.markdown(
    """
    <h2 style="
        font-size: 20px;
        margin-bottom: 10px;
        white-space: nowrap;
    ">
        Order Timing
    </h2>
    """,
    unsafe_allow_html=True
)

purchase_dayofweek = st.selectbox(
    "Day of week (0=Mon ... 6=Sun)",
    list(range(7))
)

purchase_month = st.selectbox(
    "Month",
    list(range(1, 13))
)

purchase_hour = st.slider(
    "Hour of purchase",
    0,
    23,
    12
)

purchase_is_weekend = st.selectbox(
    "Weekend order?",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)


# Location & category
st.markdown(
    """
    <h2 style="
        font-size: 20px;
        margin-bottom: 10px;
        white-space: nowrap;
    ">
        Location & Category
    </h2>
    """,
    unsafe_allow_html=True
)

BRAZIL_STATES = [
    'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT',
    'PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO'
]

PRODUCT_CATEGORIES = [
    'agro_industry_and_commerce','air_conditioning','art','arts_and_craftmanship',
    'audio','auto','baby','bed_bath_table','books_general_interest',
    'books_imported','books_technical','cds_dvds_musicals','christmas_supplies',
    'cine_photo','computers','computers_accessories','consoles_games',
    'construction_tools_construction','construction_tools_lights',
    'construction_tools_safety','cool_stuff','costruction_tools_garden',
    'costruction_tools_tools','diapers_and_hygiene','drinks','dvds_blu_ray',
    'electronics','fashio_female_clothing','fashion_bags_accessories',
    'fashion_childrens_clothes','fashion_male_clothing','fashion_shoes',
    'fashion_sport','fashion_underwear_beach','fixed_telephony','flowers',
    'food','food_drink','furniture_bedroom','furniture_decor',
    'furniture_living_room','furniture_mattress_and_upholstery',
    'garden_tools','health_beauty','home_appliances','home_appliances_2',
    'home_comfort_2','home_confort','home_construction','housewares',
    'industry_commerce_and_business',
    'kitchen_dining_laundry_garden_furniture','la_cuisine',
    'luggage_accessories','market_place','music','musical_instruments',
    'office_furniture','party_supplies','perfumery','pet_shop',
    'security_and_services','signaling_and_security','small_appliances',
    'small_appliances_home_oven_and_coffee','sports_leisure','stationery',
    'tablets_printing_image','telephony','toys','watches_gifts'
]

customer_state = st.selectbox(
    "Customer state",
    BRAZIL_STATES
)

seller_state = st.selectbox(
    "Seller state",
    BRAZIL_STATES
)

payment_type = st.selectbox(
    "Payment type",
    ['boleto', 'credit_card', 'debit_card', 'voucher']
)

product_category_name_english = st.selectbox(
    "Product category",
    PRODUCT_CATEGORIES
)


# Derived feature
same_state = 1 if customer_state == seller_state else 0


# Prediction
st.divider()

if st.button("Predict Delivery Time", use_container_width=True):

    input_df = pd.DataFrame([{
        "n_items": n_items,
        "n_sellers": n_sellers,
        "total_price": total_price,
        "total_freight": total_freight,
        "avg_price": avg_price,
        "product_weight_g": product_weight_g,
        "product_length_cm": product_length_cm,
        "product_height_cm": product_height_cm,
        "product_width_cm": product_width_cm,
        "payment_value": payment_value,
        "distance_km": distance_km,
        "purchase_dayofweek": purchase_dayofweek,
        "purchase_month": purchase_month,
        "purchase_hour": purchase_hour,
        "purchase_is_weekend": purchase_is_weekend,
        "same_state": same_state,
        "estimated_delivery_days": estimated_delivery_days,
        "payment_installments": payment_installments,
        "payment_type": payment_type,
        "customer_state": customer_state,
        "seller_state": seller_state,
        "product_category_name_english": product_category_name_english,
    }])

    pred_log = model.predict(input_df)
    pred_days = np.expm1(pred_log)[0]

    st.success(
        f"Estimated delivery time: **{pred_days:.1f} days 🎉**"
    )