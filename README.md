
# 📦 Amazon Bestsellers Scraper
### Scrape Bestselling Electronics from Amazon & Analyze the Data!

![Amazon Scraper Banner](https://user-images.githubusercontent.com/your_image.png)  
*(Replace with an actual image if needed)*

---

## 🚀 Features
✅ Scrapes Amazon's Bestsellers (Electronics)  
✅ Saves Data to CSV  
✅ Cleans & Processes Data  
✅ Generates Visualizations (Price & Ratings)  
✅ Fully Automated – Just Run & Get Insights!  

---

## 📂 Folder Structure
```
amazon_scraper_project/
│── data_scraping/
│   ├── amazon.py               # Main script (scraping, cleaning, visualization)
│   ├── requirements.txt        # Required Python libraries
│── data/
│   ├── amazon_bestsellers.csv  # Scraped product data (saved here)
│── visualizations/
│   ├── price_distribution.png  # Graphs saved here
│   ├── rating_distribution.png
│── url.txt                     # Stores Amazon URL
│── README.md                    # Project documentation
```

---

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/amazon_scraper_project.git
cd amazon_scraper_project
```

### 2️⃣ Install Dependencies
```bash
pip install -r data_scraping/requirements.txt
```

### 3️⃣ Add an Amazon URL
Edit `url.txt` and add an Amazon Bestsellers URL (Example):
```
https://www.amazon.in/gp/bestsellers/electronics/
```

---

## ▶️ How to Run
Run the script with:
```bash
python3 data_scraping/amazon.py
```
✅ This will:  
- Scrape Amazon's Bestsellers  
- Save data in `data/amazon_bestsellers.csv`  
- Generate **graphs** in `visualizations/`  

---

## 📊 Sample Output
- **Price Distribution**  
  ![Price Distribution Graph](https://user-images.githubusercontent.com/sample_price_graph.png) *(Replace with actual image)*  
- **Rating vs Price Scatter Plot**  
  ![Scatter Plot](https://user-images.githubusercontent.com/sample_scatter_plot.png)  

---

## 🔍 How It Works
✔ Reads the **Amazon URL** from `url.txt`  
✔ **Sends a request** to Amazon (with headers to avoid blocks)  
✔ **Extracts product details** (Title, Price, Rating)  
✔ **Cleans & Processes Data**  
✔ **Generates visualizations**  

---

## 💡 Customization
### 🖊 Modify the Categories
To scrape different categories, **update the URL** in `url.txt`:
```
https://www.amazon.in/gp/bestsellers/books/
```

### 📅 Scrape Multiple Pages
Modify the script to loop through multiple pages:
```python
for page in range(1, 5):
    url = f"https://www.amazon.in/gp/bestsellers/electronics/?pg={page}"
```

---

## 📌 Contributing
🚀 Contributions are welcome! If you find a bug or want to add features:  
1. **Fork the repo**  
2. **Create a new branch** (`feature-new-idea`)  
3. **Commit & push**  
4. **Open a Pull Request**  

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to use and modify it.  

---

## 💬 Contact & Support
📧 **Email:** your-email@example.com  
🐙 **GitHub:** [@yourusername](https://github.com/yourusername)  

If you found this useful, **⭐ Star the repo** and share! 🚀  

---

### 🎉 Happy Scraping! 🚀
```

---

## **📌 How to Use This File**
1. **Copy** the above code.  
2. **Create a `README.md` file** in your GitHub repository:
   ```bash
   touch README.md
   ```
3. **Paste the content** inside `README.md`.  
4. **Commit & Push** to GitHub:
   ```bash
   git add README.md
   git commit -m "Added project documentation"
   git push origin main
   ```

Now, your repository is **ready for GitHub** and **easy to use for others! 🚀**