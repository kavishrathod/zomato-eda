# 🍽️ Exploratory Data Analysis – Zomato Bangalore Restaurants

**Author:** Kavish Rathod  
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn  
**Dataset:** Zomato Bangalore Restaurant Dataset (1000 records, 9 features)

---

## 📌 Objective

To perform end-to-end Exploratory Data Analysis on the Zomato Bangalore dataset and extract actionable insights on restaurant ratings, cuisine trends, pricing patterns, and location-based distribution.

---

## 📁 Project Structure

```
zomato-eda/
│
├── zomato.csv              # Dataset
├── zomato_eda.py           # Main EDA script
├── README.md               # Project documentation
│
└── plots/
    ├── 01_rating_distribution.png
    ├── 02_online_order_vs_rating.png
    ├── 03_top_locations.png
    ├── 04_cuisine_popularity.png
    ├── 05_cost_distribution.png
    ├── 06_rest_type_vs_rating.png
    └── 07_correlation_heatmap.png
```

---

## 🔍 Steps Performed

### 1. Data Loading & Overview
- Loaded dataset with 1000 rows and 9 columns
- Inspected data types, shape, and column descriptions

### 2. Data Cleaning
- Identified and filled **80 missing ratings** with median value
- Identified and filled **40 missing cost values** with median value
- Removed duplicate rows
- Detected outliers in votes column using IQR method

### 3. Exploratory Analysis & Visualisations

| Plot | Description |
|------|-------------|
| Rating Distribution | Histogram showing how ratings are spread across restaurants |
| Online Order vs Rating | Boxplot comparing ratings based on online order availability |
| Top Locations | Bar chart of top 10 locations by restaurant count |
| Cuisine Popularity | Horizontal bar chart of top 10 most popular cuisines |
| Cost Distribution | Histogram of approximate cost for two people |
| Restaurant Type vs Rating | Avg rating by restaurant type |
| Correlation Heatmap | Correlation between rating, votes, and cost |

---

## 💡 Key Insights

1. **Rating Distribution**
   - Average restaurant rating is **3.70 / 5**
   - Most restaurants fall between **3.5 – 4.5** rating range

2. **Online Ordering Impact**
   - Restaurants with online ordering show comparable ratings to those without
   - Online ordering availability is high (~65% of restaurants)

3. **Location Trends**
   - Areas like **Koramangala, Indiranagar, and Whitefield** have the highest restaurant density
   - These are prime tech and commercial hubs driving food demand

4. **Cuisine Trends**
   - **North Indian and South Indian** cuisines are most prevalent
   - Fast Food and Chinese are rapidly growing categories

5. **Pricing Patterns**
   - Average cost for two people is approximately **₹618**
   - Majority of restaurants target the **₹200–₹600** budget segment
   - Fine Dining restaurants dominate the ₹1000+ range

6. **Votes & Ratings Correlation**
   - Higher-voted restaurants tend to maintain slightly better ratings
   - Indicates popular restaurants sustain quality over time

---

## ▶️ How to Run

```bash
# Clone the repo
git clone https://github.com/kavishrathod/zomato-eda.git
cd zomato-eda

# Install dependencies
pip install pandas numpy matplotlib seaborn

# Run the analysis
python zomato_eda.py
```

All plots will be saved in the `plots/` folder.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core programming language |
| Pandas | Data loading, cleaning, manipulation |
| NumPy | Numerical operations, outlier detection |
| Matplotlib | Custom visualisations |
| Seaborn | Statistical plots |

---

## 📊 Sample Visualisations

> Run the script to generate all plots in the `/plots` directory.

---

## 📬 Contact

**Kavish Rathod**  
📧 kavishrathod2004@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/kavishrathod) | [GitHub](https://github.com/kavishrathod)
