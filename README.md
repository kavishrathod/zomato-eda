# 🍽️ Exploratory Data Analysis – Zomato Bangalore Restaurants

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn  
**Dataset:** Zomato Bangalore Restaurant Dataset (7,105 records, 12 features)

---

## 📌 Objective

To perform end-to-end Exploratory Data Analysis on the Zomato Bangalore dataset and extract actionable insights on restaurant ratings, cuisine trends, pricing patterns, and location-based distribution.

---

## 📁 Project Structure

```
zomato-eda/
│
├── Zomato_Restaurants_Dataset.csv   # Dataset
├── zomato_eda.ipynb                 # Main EDA notebook
├── README.md                        # Project documentation
```

---

## 🔍 Steps Performed

### 1. Data Loading & Overview
- Loaded dataset with 7,105 rows and 12 columns
- Inspected data types, shape, and column descriptions

### 2. Data Cleaning
- Renamed columns for easier access
- Dropped unnamed/irrelevant columns
- Cleaned location column (extracted primary area from combined strings)
- Extracted primary cuisine and primary restaurant type from combined values
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
| Restaurant Type vs Rating | Top 10 restaurant types by average rating |
| Correlation Heatmap | Correlation between rating, votes, and cost |

---

## 💡 Key Insights

1. **Ratings** - Most restaurants (78.7%) are rated between 3.0 and 4.2. The average rating is 3.48, suggesting moderate satisfaction overall across Bangalore.

2. **Online Ordering** - Restaurants that accept online orders have a slightly higher average rating (3.55) compared to those that don't (3.41). About 52.5% of restaurants offer online ordering.

3. **Location** - Byresandra, Bannerghatta Road and Brookefield have the highest number of restaurants, indicating strong dining demand in these areas.

4. **Cuisines** - North Indian cuisine is by far the most popular (1,943 restaurants), followed by South Indian and Chinese. This reflects Bangalore's diverse food culture.

5. **Pricing** - Average cost for two people is ₹536, with median at ₹400. About 68% of restaurants fall in the ₹200–₹600 range, showing budget-friendly dining dominates.

6. **Votes vs Rating** - There is a moderate positive correlation (0.32) between votes and rating, and also between cost and rating (0.33). Higher-priced restaurants tend to get better ratings and more engagement.

---

## ▶️ How to Run

```bash
# Clone the repo
git clone https://github.com/kavishrathod/zomato-eda.git
cd zomato-eda

# Install dependencies
pip install pandas numpy matplotlib seaborn

# Open notebook
jupyter notebook zomato_eda.ipynb
```

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

## 📬 Contact

**Kavish Rathod**  
📧 kavishrathod2004@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/kavishrathod) | [GitHub](https://github.com/kavishrathod)
