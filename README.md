# Delivery Time Prediction System 📦

## 🙂 Overview

This project focuses on predicting e-commerce delivery time in days for a logistics company. By analyzing order, product, payment, customer, seller, location, distance, and purchase-time information, the project builds a machine learning regression model to estimate how long an order may take to reach a customer.

*The goal is to support delivery planning, identify potential delays, improve estimated delivery times, and help logistics teams make better operational decisions.*

---

## 💡 Problem Statement & Business Impact

- Customers want reliable delivery estimates when they place online orders.
- Unpredictable delivery times can make logistics planning difficult and negatively affect customer experience.
- Delivery time can vary based on factors such as distance, customer and seller locations, freight costs, and purchase timing.
- **Goal:** Develop a regression model that predicts delivery time in days using information available when an order is placed.
- **Business value:** More useful delivery estimates can help operations teams plan logistics, identify orders that may be at risk of delay, reduce delivery-related costs, and improve customer satisfaction.

---

## 📂 Project Structure

```text
Delivery-Time-Prediction-System/
│
├── data/
│   └── olist_delivery_time_data.csv
│
├── images/                              # EDA charts and visualizations
│
├── model/                               # Saved machine learning model
│
├── notebooks/                           # Jupyter notebooks for analysis and modeling
│   ├── 1_Exploratory_Data_Analysis.ipynb
│   └── 2_Data_Preparation_and_Model_Training.ipynb
│
├── .gitignore
├── app.py                               # Streamlit application
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🔗 Data Source

**Original Olist Dataset:**
[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

**Prepared Kaggle Dataset:**
[Ecommerce Delivery Time Prediction](https://www.kaggle.com/datasets/neuralarin/ecommerce-delivery-time-dataset)

- The prepared dataset is based on the Olist Brazilian e-commerce data and is prepared to analyze ecommerce delivery patterns and train a regression model.

---

## 📊 Dataset Overview

The dataset contains order and logistics information used to predict e-commerce delivery time.

* **Dataset dimensions:** The dataset has 96478 rows and 24 columns.
* **Features:** Order details, product information, payment and freight information, customer and seller locations, delivery distance, and other relevant variables.
* **Target variable:** Delivery time in days.

---

## 🚀 How to Run the Application Locally

Follow these steps to run the application on your local system.

### 1. Clone the Repository

```bash
git clone https://github.com/neuralarin/Delivery-Time-Prediction-System.git

cd Delivery-Time-Prediction-System
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on **Windows PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Ensure that Python 3.12 is installed. Install the required libraries using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

From the repository directory, run the following command:

```bash
streamlit run app.py
```

The application will open in your default web browser. If it does not open automatically, visit the local URL displayed in your terminal, usually `http://localhost:8501`.

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

The tuned **XGBoost Regressor** achieved an MAE of **4.418 days**, an RMSE of **7.549 days**, and an R² score of **0.343** in the reported tuning results. An MAE of around 4.4 days means that predictions differ from actual delivery times by about 4.4 days on average in absolute terms. The R² score indicates that the model explains a limited portion of the variation in delivery time, so there is room for further improvement.

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

### 1. Missing-Value Distribution

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/missing_value_distribution.png" width="100%">

### 2. Delivery-Time Distribution

* **The data is right-skewed. Most orders arrive quickly, while a few extreme outliers take much longer. I applied log transformation during data preprocessing.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/delivery_time_distribution.png" width="100%">

### 3. Estimated vs. Actual Delivery Time

* **The estimated delivery time does not closely match the actual delivery time. While the red trend line shows a positive relationship, the large vertical spread indicates that real-world delivery times are highly variable and can take much longer than estimated.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/estimated_vs_actual_delivery.png" width="100%">

### 4. Delivery Distance vs. Delivery Time

* **Delivery distance affects delivery time. The upward trend line indicates a positive relationship: as distance increases, delivery time also increases.**
* **The wide vertical spread of the data points—especially at distances under 4,000 km—shows that many short-distance deliveries can still take a long time. This indicates that distance is an important factor, but it is not the only variable determining delivery time.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/delivery_time_vs_delivery_distance.png" width="100%">

### 5. Same-State vs. Cross-State Deliveries

* **Same-state deliveries are noticeably faster. The plot for same-state deliveries (1) shows a lower median delivery time compared to cross-state deliveries (0). The tighter and lower box for same-state deliveries indicates that the majority of these orders are completed in fewer days, while cross-state deliveries have a wider range and more extreme delays.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/same_state_vs_cross_state.png" width="100%">

### 6. Customer States with the Longest Delivery Times

* **The states experiencing the longest average delivery times are RR (nearly 30 days), followed by AP and AM (between 25 and 28 days).**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/longest_delivery_time_by_customer_state.png" width="100%">

### 7. Seller States with the Slowest Deliveries

* **The seller state with the slowest average delivery time is AM (nearly 50 days on average). Other slowest states are RO, CE, and MA, which all average around 18 days.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/longest_delivery_time_by_seller_state.png" width="100%">

### 8. Number of Sellers vs. Delivery Time

* **Orders involving multiple sellers do not generally take longer to deliver. The most extreme delivery delays occur mostly with single-seller orders, while orders involving multiple sellers (between 2 and 5) have fewer extreme outliers.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/number_of_seller_vs_delivery_time.png" width="100%">

### 9. Number of Items vs. Delivery Time

* **The number of items in an order has little impact on delivery time. The median delivery time remains almost the same across all categories, whether a customer orders one item or seven.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/number_of_items_vs_delivery_time.png" width="100%">

### 10. Order Value vs. Delivery Time

* **Higher order values rarely affect delivery time, while the most extreme delivery delays occur with much cheaper orders.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/order_value_vs_delivery_time.png" width="100%">

### 11. Purchase Timing vs. Delivery Time

* **Purchase month:** Average delivery time changes throughout the year, peaking at over 16 days in month 2 and dropping to a low of about 9 days in month 8.
* **Hour of day:** Orders placed at hour 4 show the fastest average delivery times, at under 12 days.
* **Day of the week:** Day 4 and day 5 show higher average delivery times compared to the rest of the week.
* **Weekend vs weekday:** Median delivery times are nearly identical, while weekday orders have more extreme outliers.

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/order_time_vs_delivery_time.png" width="100%">

### 12. Correlation Heatmap

**distance_km, estimated_delivery_days, and total_freight are positively correlated, meaning that as these variables increase, delivery time tends to increase. same_state is negatively correlated, meaning deliveries within the same state tend to take fewer days. These variables are therefore useful predictors for delivery-time prediction.**

<img src="https://github.com/neuralarin/Delivery-Time-Prediction-System/blob/main/images/correlation_heatmap.png" width="100%">

---

## 🚀 Streamlit Deployment

The trained XGBoost model is saved using **Joblib** and integrated into a Streamlit application. Users can enter order, product, customer, seller, location, distance, and purchase-time information through the interface.

The application processes the inputs using the same preprocessing pipeline used during model training and generates an estimated delivery time in days.

This provides a simple way to demonstrate how the trained machine learning model could be used by business or operations teams for real-time delivery-time estimation.

---

## 💼 Business Impact

If implemented in production, the delivery-time prediction model can help the company reduce delivery delays, improve ETA accuracy, optimize logistics planning, identify orders that may need additional monitoring and proactively manage high-risk orders. This can lead to lower delivery-related costs, fewer customer complaints, higher customer satisfaction, improved delivery experience and improved repeat purchases.

---

## 🔮 Future Improvements

- Add more relevant operational and logistics features.
- Perform advanced feature engineering using historical delivery patterns.
- Improve handling of extreme delivery-time outliers.
- Add explainability features to show which factors influence each prediction.
- Retrain and monitor the model as new delivery data becomes available.
