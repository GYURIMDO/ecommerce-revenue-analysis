# **📝 Data Cleaning Report: E-Commerce Superstore Dataset**

## **1️⃣ Dataset Overview**
- **Source:** Google Sheets CSV file  
- **Total Rows:** 10,090  
- **Total Columns:** 19  
- **Key Fields:** `Order Date`, `Sales`, `Profit`, `Quantity`, `Discount`, `Region`, etc.  

---

## **2️⃣ Data Quality Issues Identified & Fixes**  

| **Issue** | **Fix Applied** | **Reasoning** |
|-----------|---------------|--------------|
| **Date Format Incorrect** (`Order Date`, `Ship Date` were strings) | Converted to `datetime` format | Enables time-based analysis & trends |
| **Unnecessary Columns** (`Customer Name`, `Postal Code`) | Dropped from dataset | Not required for revenue analysis |
| **Duplicate Records Found** | Removed duplicates | Ensures accuracy & avoids data inflation |
| **Outliers in Sales** (top 1%) | Removed values above the `99th percentile` | Prevents extreme values from skewing results |
| **Missing Values Check** | None found, so no imputation needed | Ensured dataset completeness |

---

## **3️⃣ Summary Statistics**  

### **Numerical Data Overview**  

| Metric | Order Date | Ship Date | Discount | Profit | Quantity | Sales |
|--------|------------|------------|----------|--------|----------|--------|
| **Count** | 10,090 | 10,090 | 10,090 | 10,090 | 10,090 | 10,090 |
| **Mean** | 2023-04-30 | 2023-05-04 | 0.156 | 20.04 | 3.77 | 184.88 |
| **Min** | 2021-01-03 | 2021-01-07 | 0.00 | -3701.89 | 1.00 | 0.44 |
| **25%** | 2022-05-17 | 2022-05-21 | 0.00 | 1.73 | 2.00 | 17.01 |
| **50%** | 2023-06-26 | 2023-06-29 | 0.20 | 8.51 | 3.00 | 51.97 |
| **75%** | 2024-05-14 | 2024-05-19 | 0.20 | 28.41 | 5.00 | 199.98 |
| **Max** | 2024-12-30 | 2025-01-05 | 0.80 | 1114.51 | 14.00 | 2453.43 |
| **Std Dev** | N/A | N/A | 0.21 | 119.73 | 2.21 | 321.05 |

- **Sales & Profit Distribution:** Highly skewed, requiring outlier treatment.  
- **Discount Impact:** Some transactions had **80% discounts**, which could indicate potential profitability concerns.

---

## **4️⃣ Exploratory Insights**  

### **📌 Sales Distribution**  
- Majority of sales are in the **lower range**, but a few **high-value orders** were present.  
- Outliers removed using the **99th percentile threshold**.

### **📌 Sales Trends Over Time**  
- Sales follow an **increasing trend** with seasonal fluctuations.  
- Certain months show spikes, possibly due to **holiday seasons or promotions**.

### **📌 Regional Sales Performance**  
- **Highest Revenue Regions:** 🏆 `West` & `East`  
- **Lower Revenue Regions:** `South` & `Central`  
- Possible reason: Larger customer base or higher average order values in top-performing regions.

---

## **5️⃣ Missing Values Summary**  
All columns have **0 missing values**, so no imputation was required.

---

## **6️⃣ Next Steps**  
✅ **Deep Dive Analysis:**  
- How do discounts impact profit margins?  
- Do repeat customers spend more than new customers?  
- Which product categories generate the most revenue?  

✅ **Tableau Dashboard:**  
- Visualizing **top-performing products, regions, and trends**.  

✅ **Customer Segmentation:**  
- Identify **high-value customers** for targeted marketing.  

---

## **Conclusion**  
📌 The dataset is **cleaned & ready for analysis**, with unnecessary columns dropped, duplicates removed, and sales outliers handled. Now, we can move into **customer behavior analysis & business insights!**  

🚀 **Next Steps:** Begin revenue and profitability analysis!  

---
