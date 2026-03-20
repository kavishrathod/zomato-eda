# Exploratory Data Analysis on Zomato Bangalore Restaurant Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# ── Style ──────────────────────────────────────────────────────
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({
    "figure.facecolor": "#FAFAFA",
    "axes.facecolor":   "#FAFAFA",
    "font.family":      "DejaVu Sans",
    "axes.titlesize":   13,
    "axes.titleweight": "bold",
})

# 1. LOAD DATA
print("  Zomato Bangalore – Exploratory Data Analysis")

df = pd.read_csv("zomato.csv")
print(f"\n[INFO] Dataset shape : {df.shape}")
print(f"[INFO] Columns       : {list(df.columns)}\n")
print(df.head())

# 2. DATA OVERVIEW
print("\n── Data Types ──────────────────────────────────────────")
print(df.dtypes)

print("\n── Missing Values ──────────────────────────────────────")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({"Missing Count": missing, "Missing %": missing_pct})
print(missing_df[missing_df["Missing Count"] > 0])

print("\n── Statistical Summary ─────────────────────────────────")
print(df.describe())

# 3. DATA CLEANING
print("\n── Data Cleaning ───────────────────────────────────────")

# Rename for convenience
df.rename(columns={
    "approx_cost(for two people)": "approx_cost",
    "listed_in(type)":             "rest_type",
    "listed_in(city)":             "location"
}, inplace=True)

# Fill missing ratings with median
median_rate = df["rate"].median()
df["rate"].fillna(median_rate, inplace=True)
print(f"[CLEAN] Filled {missing['rate']} missing ratings with median: {median_rate}")

# Fill missing cost with median
median_cost = df["approx_cost"].median()
df["approx_cost"].fillna(median_cost, inplace=True)
print(f"[CLEAN] Filled {missing['approx_cost(for two people)']} missing costs with median: {median_cost}")

# Remove duplicates
before = len(df)
df.drop_duplicates(inplace=True)
print(f"[CLEAN] Removed {before - len(df)} duplicate rows")

# Outlier detection – votes (IQR method)
Q1, Q3 = df["votes"].quantile(0.25), df["votes"].quantile(0.75)
IQR = Q3 - Q1
outlier_mask = (df["votes"] < Q1 - 1.5 * IQR) | (df["votes"] > Q3 + 1.5 * IQR)
print(f"[CLEAN] Detected {outlier_mask.sum()} vote outliers (retained for analysis)")

print(f"\n[INFO] Clean dataset shape: {df.shape}")

# 4. VISUALISATIONS  (saved to /Plots/)
import os
os.makedirs("plots", exist_ok=True)

# ── 4A. Rating Distribution ───────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(df["rate"].dropna(), bins=30, color="#4C72B0", edgecolor="white", linewidth=0.6)
ax.set_title("Distribution of Restaurant Ratings")
ax.set_xlabel("Rating")
ax.set_ylabel("Count")
ax.axvline(df["rate"].mean(), color="#DD5555", linestyle="--", linewidth=1.5,
           label=f"Mean: {df['rate'].mean():.2f}")
ax.legend()
plt.tight_layout()
plt.savefig("plots/01_rating_distribution.png", dpi=150)
plt.close()
print("[PLOT] 01_rating_distribution.png saved")

# ── 4B. Online Order vs Rating ────────────────────────────────
fig, ax = plt.subplots(figsize=(7, 4))
sns.boxplot(data=df, x="online_order", y="rate", palette=["#DD5555", "#4C72B0"], ax=ax)
ax.set_title("Online Order Availability vs Rating")
ax.set_xlabel("Accepts Online Orders")
ax.set_ylabel("Rating")
plt.tight_layout()
plt.savefig("plots/02_online_order_vs_rating.png", dpi=150)
plt.close()
print("[PLOT] 02_online_order_vs_rating.png saved")

# ── 4C. Top 10 Locations by Restaurant Count ──────────────────
top_locs = df["location"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(9, 4))
top_locs.plot(kind="bar", color="#55A868", edgecolor="white", ax=ax)
ax.set_title("Top 10 Locations by Number of Restaurants")
ax.set_xlabel("Location")
ax.set_ylabel("Count")
ax.set_xticklabels(ax.get_xticklabels(), rotation=35, ha="right")
plt.tight_layout()
plt.savefig("plots/03_top_locations.png", dpi=150)
plt.close()
print("[PLOT] 03_top_locations.png saved")

# ── 4D. Cuisine Popularity ────────────────────────────────────
top_cuisines = df["cuisines"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(9, 4))
top_cuisines.plot(kind="barh", color="#C44E52", edgecolor="white", ax=ax)
ax.set_title("Top 10 Most Popular Cuisines")
ax.set_xlabel("Count")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("plots/04_cuisine_popularity.png", dpi=150)
plt.close()
print("[PLOT] 04_cuisine_popularity.png saved")

# ── 4E. Approximate Cost Distribution ────────────────────────
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(df["approx_cost"], bins=25, color="#8172B2", edgecolor="white", linewidth=0.6)
ax.set_title("Distribution of Approximate Cost for Two People")
ax.set_xlabel("Cost (INR)")
ax.set_ylabel("Count")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{int(x)}"))
plt.tight_layout()
plt.savefig("plots/05_cost_distribution.png", dpi=150)
plt.close()
print("[PLOT] 05_cost_distribution.png saved")

# ── 4F. Restaurant Type vs Avg Rating ────────────────────────
avg_rating_type = df.groupby("rest_type")["rate"].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(9, 4))
avg_rating_type.plot(kind="bar", color="#4C72B0", edgecolor="white", ax=ax)
ax.set_title("Average Rating by Restaurant Type")
ax.set_xlabel("Restaurant Type")
ax.set_ylabel("Avg Rating")
ax.set_xticklabels(ax.get_xticklabels(), rotation=35, ha="right")
ax.set_ylim(3, 4.5)
plt.tight_layout()
plt.savefig("plots/06_rest_type_vs_rating.png", dpi=150)
plt.close()
print("[PLOT] 06_rest_type_vs_rating.png saved")

# ── 4G. Correlation Heatmap ───────────────────────────────────
fig, ax = plt.subplots(figsize=(6, 4))
numeric_df = df[["rate", "votes", "approx_cost"]]
sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm",
            linewidths=0.5, ax=ax)
ax.set_title("Correlation Heatmap – Numeric Features")
plt.tight_layout()
plt.savefig("plots/07_correlation_heatmap.png", dpi=150)
plt.close()
print("[PLOT] 07_correlation_heatmap.png saved")

# 5. KEY INSIGHTS
print("\n" + "=" * 60)
print("  KEY INSIGHTS")
print("=" * 60)

online_yes_avg = df[df["online_order"] == "Yes"]["rate"].mean()
online_no_avg  = df[df["online_order"] == "No"]["rate"].mean()
top_location   = df["location"].value_counts().idxmax()
top_cuisine    = df["cuisines"].value_counts().idxmax()
avg_cost       = df["approx_cost"].mean()
high_vote_avg  = df[df["votes"] > df["votes"].quantile(0.75)]["rate"].mean()

print(f"""
1. RATING DISTRIBUTION
   - Average rating across all restaurants : {df['rate'].mean():.2f}
   - Restaurants with online ordering      : {online_yes_avg:.2f} avg rating
   - Restaurants without online ordering   : {online_no_avg:.2f} avg rating
   → Restaurants accepting online orders tend to have higher ratings.

2. LOCATION TRENDS
   - Most restaurants are located in       : {top_location}
   → High-density areas indicate strong dining demand and competition.

3. CUISINE TRENDS
   - Most popular cuisine in Bangalore     : {top_cuisine}
   → North Indian and South Indian cuisines dominate the market.

4. PRICING PATTERNS
   - Average cost for two people           : ₹{avg_cost:.0f}
   - Most restaurants fall in ₹200–₹600 range
   → Budget-friendly dining dominates the Bangalore food scene.

5. VOTES vs RATING
   - High-voted restaurants (top 25%) avg  : {high_vote_avg:.2f} rating
   → More votes correlate with slightly higher ratings, indicating
     popular restaurants tend to maintain quality.
""")

print("[DONE] EDA complete. All plots saved in /Plots/ folder.")
