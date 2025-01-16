import numpy as np
import pandas as pd

# Defining the data
data = {
    "Sales": [230, 181, 165, 150, 97, 192, 181, 189, 172, 170],
    "Price": [125, 99, 97, 115, 120, 100, 80, 90, 95, 125],
    "Advert": [200, 55, 105, 85, 0, 150, 85, 120, 110, 130],
    "Ass_Hours": [109, 107, 98, 71, 82, 103, 111, 93, 86, 78]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Mean of each column
mean_sales = np.mean(df["Sales"])
mean_price = np.mean(df["Price"])
mean_advert = np.mean(df["Advert"])
mean_ass_hours = np.mean(df["Ass_Hours"])

# Covariance calculations
n = len(df)  # number of data points

# Covariance of Sales and Price
cov_sales_price = sum((df["Sales"] - mean_sales) * (df["Price"] - mean_price)) / (n - 1)

# Covariance of Sales and Advert
cov_sales_advert = sum((df["Sales"] - mean_sales) * (df["Advert"] - mean_advert)) / (n - 1)

# Covariance of Sales and Ass_Hours
cov_sales_ass_hours = sum((df["Sales"] - mean_sales) * (df["Ass_Hours"] - mean_ass_hours)) / (n - 1)

# Covariance of Price and Advert
cov_price_advert = sum((df["Price"] - mean_price) * (df["Advert"] - mean_advert)) / (n - 1)

# Covariance of Price and Ass_Hours
cov_price_ass_hours = sum((df["Price"] - mean_price) * (df["Ass_Hours"] - mean_ass_hours)) / (n - 1)

# Covariance of Advert and Ass_Hours
cov_advert_ass_hours = sum((df["Advert"] - mean_advert) * (df["Ass_Hours"] - mean_ass_hours)) / (n - 1)

# Creating a covariance matrix manually
manual_covariance_matrix = pd.DataFrame({
    "Sales": [df["Sales"].var(ddof=1), cov_sales_price, cov_sales_advert, cov_sales_ass_hours],
    "Price": [cov_sales_price, df["Price"].var(ddof=1), cov_price_advert, cov_price_ass_hours],
    "Advert": [cov_sales_advert, cov_price_advert, df["Advert"].var(ddof=1), cov_advert_ass_hours],
    "Ass_Hours": [cov_sales_ass_hours, cov_price_ass_hours, cov_advert_ass_hours, df["Ass_Hours"].var(ddof=1)]
}, index=["Sales", "Price", "Advert", "Ass_Hours"])

manual_covariance_matrix
