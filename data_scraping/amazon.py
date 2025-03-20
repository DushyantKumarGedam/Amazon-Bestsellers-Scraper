import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import random

# 📌 Read URL from file
with open("url.txt", "r") as file:
    url = file.readline().strip()

# 📌 Send HTTP GET request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

# 📌 Check response status
if response.status_code != 200:
    print(f"❌ Failed to access {url} (Status Code: {response.status_code})")
    exit()

print(f"✅ URL Loaded Successfully: {url}")

# 📌 Parse HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# 📌 Extract product data
data = []
products = soup.find_all("div", class_="zg-grid-general-faceout")

for product in products:
    try:
        title = product.select_one("div._cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
        price = product.select_one("span._cDEzb_p13n-sc-price_3mJ9Z")
        rating = product.select_one("span.a-icon-alt")

        data.append({
            "Product Title": title.text.strip() if title else "N/A",
            "Price": price.text.strip() if price else "Price Not Available",
            "Rating": rating.text.strip() if rating else "No Rating"
        })

    except Exception as e:
        print(f"⚠ Error extracting data: {e}")

    time.sleep(random.uniform(1, 2))  # Reduced sleep time for faster execution

# 📌 Convert to DataFrame
df = pd.DataFrame(data)

# 📌 Save to CSV
csv_file = "data/amazon_bestsellers_products.csv"  # Ensure 'data/' folder exists
df.to_csv(csv_file, index=False)
print(f"✅ Data successfully scraped and saved to {csv_file}")

# ---- 📌 Data Cleaning ----

df.columns = df.columns.astype(str).str.strip().str.lower()  # Normalize column names

# Clean 'price' column
df['price'] = pd.to_numeric(df['price'].str.replace('[₹,]', '', regex=True), errors='coerce')

# Clean 'rating' column
df['rating'] = df['rating'].str.extract(r'(\d+\.\d+)').astype(float)

# Handle missing values
df['price'].fillna(df['price'].median(), inplace=True)
df['rating'].fillna(0, inplace=True)

# 📌 Preview cleaned data
print("\n✅ Cleaned Data Preview:")
print(df.head())

# ---- 📊 Data Visualization ----

# **1️⃣ Price Distribution**
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=30, kde=True, color='skyblue')
plt.title('Price Distribution', fontsize=16)
plt.xlabel('Price (₹)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.savefig("visualizations/price_distribution.png")
plt.show()

# **2️⃣ Rating Distribution**
plt.figure(figsize=(10, 6))
sns.histplot(df['rating'], bins=10, kde=True, color='lightgreen')
plt.title('Rating Distribution', fontsize=16)
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.savefig("visualizations/rating_distribution.png")
plt.show()

# **3️⃣ Scatter Plot: Rating vs Price**
plt.figure(figsize=(10, 6))
sns.scatterplot(x='rating', y='price', hue='price', size='price', data=df, palette='cool', sizes=(20, 200))
plt.title('Rating vs Price Scatter Plot', fontsize=16)
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Price (₹)', fontsize=12)
plt.savefig("visualizations/rating_vs_price.png")
plt.show()

# **4️⃣ Top 10 Most Expensive Products**
top_expensive = df.nlargest(10, 'price')
plt.figure(figsize=(12, 8))
sns.barplot(x='price', y='product title', data=top_expensive, palette='viridis')
plt.title('Top 10 Most Expensive Products', fontsize=16)
plt.xlabel('Price (₹)', fontsize=12)
plt.ylabel('Product Title', fontsize=12)
plt.savefig("visualizations/top_expensive_products.png")
plt.show()
