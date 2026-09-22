# Delivery Time Prediction System 📦

## 🚚 Industry Domain 

Supply Chain & Logistics Department 

---

## 🏢 About the Company 

Delivero is an ecommerce logistic company focused on making online shopping faster, simpler, and more reliable. The company connects customers, sellers, and delivery operations to ensure orders reach customers on time. Delivero uses data and technology to improve delivery planning, reduce delays, control logistics costs, and create a better customer experience globally.

---

## 🥺 Problem Statement

Delivero wants to predict how many days an ecommerce order will take to reach the customer after purchase. The model uses order, product, payment, customer, seller, location, distance, and purchase-time information to estimate delivery time and help the company plan operations.

---

## 🎯 Objective

Build a regression model that predicts delivery time in days using information available when an order is placed. The goal is to improve planning, identify orders at risk of delay, reduce delays, and support better delivery operations.

---

## 🔗 Data Source

**Original Olist Dataset:**
[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Prepared Kaggle Dataset:**
[Ecommerce Delivery Time Prediction](https://www.kaggle.com/datasets/neuralarin/ecommerce-delivery-time-dataset)

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

---

## 📈 Data Visualization

### 1. What is the distribution of missing values in data?

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/missing_value_distribution.png" width="100%">

### 2. How does Delivero's delivery-time distribution look like?

* **The data is right-skewed. Most orders arrive quickly, while a few extreme outliers take much longer. I will apply log transformation during data preprocessing.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/delivery_time_distribution.png" width="100%">

### 3. Does the estimated delivery time match actual delivery time?

* **The estimated delivery time does not closely match the actual delivery time. While the red trend line shows a positive relationship, the large vertical spread indicates that real-world delivery times are highly variable and can take much longer than estimated.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/estimated_vs_actual_delivery.png" width="100%">

### 4. Does delivery distance affect delivery time?

* **Yes, delivery distance affects delivery time. The upward trend line indicates a positive relationship: as distance increases, delivery time also increases.**
* **The wide vertical spread of the data points—especially at distances under 4,000 km—shows that many short-distance deliveries can still take a long time. This indicates that distance is an important factor, but it is not the only variable determining delivery time.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/delivery_time_vs_delivery_distance.png" width="100%">

### 5. Are same-state deliveries faster?

* **Yes, same-state deliveries are noticeably faster. The plot for same-state deliveries (1) shows a lower median delivery time compared to cross-state deliveries (0). The tighter and lower box for same-state deliveries indicates that the majority of these orders are completed in fewer days, while cross-state deliveries have a wider range and more extreme delays.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/same_state_vs_cross_state.png" width="100%">

### 6. Which customer states experience the longest delivery times?

* **The states experiencing the longest average delivery times are RR (nearly 30 days), followed by AP and AM (between 25 and 28 days).**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/longest_delivery_time_by_customer_state.png" width="100%">

### 7. Which seller states have the slowest deliveries?

* **The seller state with the slowest average delivery time is AM (nearly 50 days on average). Other slowest states are RO, CE, and MA, which all average around 18 days.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/longest_delivery_time_by_seller_state.png" width="100%">

### 8. If one customer buys products from multiple sellers, does the order take more days to reach them?

* **No, orders involving multiple sellers do not generally take longer to deliver. The most extreme delivery delays occur mostly with single-seller orders, while orders involving multiple sellers (between 2 and 5) have fewer extreme outliers.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/number_of_seller_vs_delivery_time.png" width="100%">

### 9. Do bigger or more complicated orders take more days to reach the customer?

* **The number of items in an order has little impact on delivery time. The median delivery time remains almost the same across all categories, whether a customer orders one item or seven.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/number_of_items_vs_delivery_time.png" width="100%">

### 10. Does order value or freight cost affect delivery time?

* **Higher order values rarely affect delivery time, while the most extreme delivery delays occur with much cheaper orders.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/order_value_vs_delivery_time.png" width="100%">

### 11. Does order timing affect delivery time?

* **Purchase month:** Average delivery time changes throughout the year, peaking at over 16 days in month 2 and dropping to a low of about 9 days in month 8.
* **Hour of day:** Orders placed at hour 4 show the fastest average delivery times, at under 12 days.
* **Day of the week:** Day 4 and day 5 show higher average delivery times compared to the rest of the week.
* **Weekend vs weekday:** Median delivery times are nearly identical, while weekday orders have more extreme outliers.

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/order_time_vs_delivery_time.png" width="100%">

### 12. Which variables are most strongly related to delivery time?

**distance_km, estimated_delivery_days, and total_freight are positively correlated, meaning that as these variables increase, delivery time tends to increase. same_state is negatively correlated, meaning deliveries within the same state tend to take fewer days. These variables are therefore useful predictors for delivery-time prediction.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/correlation_heatmap.png" width="100%">

---

## 🔄 Workflow

### 1. Data Preparation

* Prepared [Ecommerce Delivery Time Prediction](https://www.kaggle.com/datasets/neuralarin/ecommerce-delivery-time-dataset) from the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) to analyze delivery behaviour.

### 2. Data Analysis

* Performed EDA to understand delivery patterns.
* Analyzed feature distributions against the target variable.

### 3. Data Preprocessing

* Handled missing values by filling missing numerical values with the median, which is robust to outliers, and missing categorical values with `Unknown`.
* Handled categorical variables using One-Hot Encoding.
* Applied log transformation to right-skewed numerical features through the preprocessing pipeline.

### 4. Model Selection

* Linear Regression
* K-Nearest Neighbors
* Decision Tree
* Random Forest
* XGBoost

### 5. Choosing Metric

* **Mean Absolute Error (MAE)** is the primary metric for predicting delivery time in days because it directly represents the average prediction error in days, making the result easy to understand from a business perspective.

### 6. Hyperparameter Optimization

* Used `RandomizedSearchCV` to improve model performance.
* Selected the best-performing model based on validation metrics.

### 7. Deployment

* Saved the trained model using Joblib.
* Built a Streamlit application for real-time delivery-time predictions.
* The application allows users to enter order-related details and receive an estimated delivery time through an interactive interface.

---

## 📈 Baseline Summary

| Model             |   MAE |   RMSE |     R² | Selected Model          |
| ----------------- | ----: | -----: | -----: | ----------------------- |
| **Random Forest** | 4.486 |  7.595 |  0.335 | **🏆 Champion Model**   |
| **XGBoost**       | 4.489 |  7.645 |  0.326 | **⏳ Competitive Model** |
| Linear Regression | 4.860 |  8.153 |  0.234 | Bad performance         |
| KNN               | 5.064 |  8.271 |  0.211 | Worse performance       |
| Decision Tree     | 6.564 | 10.977 | -0.389 | Worst performance       |

---

## Hyperparameter Tuning

| Model               |       MAE |      RMSE |        R² |
| ------------------- | --------: | --------: | --------: |
| Tuned XGBoost       | **4.418** | **7.549** | **0.343** |
| Tuned Random Forest |     4.814 |     8.065 |     0.250 |

An **XGBoost Regressor** was tuned using `RandomizedSearchCV`, improving delivery-time prediction to **MAE 4.45 days / R² 0.34**, and deployed as an interactive Streamlit application for real-time predictions.

---

## 🚀 Streamlit Deployment

The trained XGBoost model is saved using **Joblib** and integrated into a Streamlit application. Users can enter order, product, customer, seller, location, distance, and purchase-time information through the interface.

The application processes the inputs using the same preprocessing pipeline used during model training and generates an estimated delivery time in days.

This provides a simple way to demonstrate how the trained machine learning model could be used by business or operations teams for real-time delivery-time estimation.

---

## 💼 Business Impact

If implemented in production, the delivery-time prediction model can help the company reduce delivery delays, improve ETA accuracy, optimize logistics planning, and proactively manage high-risk orders. This can lead to lower delivery-related costs, fewer customer complaints, higher customer satisfaction, and improved repeat purchases.

---

## 🔮 Future Improvements

* Add more relevant operational and logistics features.
* Perform advanced feature engineering using historical delivery patterns.
* Improve handling of extreme delivery-time outliers.
* Add explainability features to show which factors influence each prediction.
* Retrain the model periodically with new delivery data.
