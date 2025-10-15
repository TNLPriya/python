import pandas as pd
import numpy as np
data = pd.DataFrame({
    'Product': ['Laptop', 'Headphones', 'Mouse', 'Keyboard'] * 5,
    'Units_Sold': np.random.randint(5, 50, 20),
    'Price_per_Unit': np.random.randint(1000, 5000, 20)
})
data['Total_Sales'] = data['Units_Sold'] * data['Price_per_Unit']
top_product = data.groupby('Product')['Total_Sales'].sum().idxmax()
total_sales = data['Total_Sales'].sum()
print("Top Selling Product:", top_product)
print("Total Sales: ₹", total_sales)
print("\nSample Data:\n", data)
