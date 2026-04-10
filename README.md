# Gapminder Analytics: Interactive Life Expectancy Dashboards

**Developed by:** Halyna Yurkova  
**Role:** Senior Data Analyst / Python Developer  

---

## 🚀 Project Overview
This project transforms raw demographic data from the Gapminder dataset into a series of interactive analytical dashboards.  
The goal is to provide high-level insights into global life expectancy trends using the Dash framework.

---

## 📂 Project Structure

- **Module 01:** Distribution of Life Expectancy (Histogram)  
- **Module 02:** Yearly Regional Comparison (Grouped Bar Chart)  
- **Module 03:** Deep-Dive Analytics with TOP-5 Country Hover (Advanced Tooltips)  

---

## 🛠 Tech Stack & PEP 8 Standards

The following libraries are required to run these dashboards.  
Imports are structured according to PEP 8 guidelines (standard → third-party).

```python
import dash_daq as daq
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, callback, dcc, html
```

---

## 📊 Module 01: Life Expectancy Distribution

**File:** `01_dash_life_expectancy_histogram.py`

### Task Description
- **Objective:** Visualize the distribution of life expectancy within a selected continent  
- **Method:** Histogram showing density across age ranges  
- **Interactive Feature:** Dropdown for continent selection  

### Analytical Insight
Helps identify regional inequality.  
A wide distribution indicates a large gap between less and more developed countries.

---

## 📊 Module 02: Yearly Comparative Analysis

**File:** `02_dash_life_expectancy_yearly_comparison.py`

### Task Description
- **Objective:** Compare average life expectancy across years (1952–2007)  
- **Method:** Aggregated bar charts by continent  
- **Interactive Feature:** Global vs. continent-level filtering  

### Analytical Insight
Shows historical growth trends and allows benchmarking regions against the global average.

---

## 📊 Module 03: Advanced Hover Insights (TOP-5 Countries)

**File:** `03_dash_life_expectancy_top_countries_hover.py`

### Task Description
- **Objective:** Provide detailed insights without overloading the interface  
- **Method:** Use `customdata` to inject TOP-5 countries into hover tooltips  
- **Interactive Feature:** Custom HTML hover templates  

### Analytical Insight
Explains continent-level averages by highlighting top-performing countries for each year.

---

## ⚙️ Execution Instructions

### 1. Navigate to project folder
```bash
cd ~/Documents/IT_Career_Hab/Python/Python_AD/Dash
```

### 2. Run a specific module
```bash
python3 01_dash_life_expectancy_histogram.py
```

---

## 🛠 Troubleshooting (Port in use)

If you see: **Address already in use**

```bash
lsof -i :8053
kill -9 [PID_NUMBER]
```

---

## 🌐 Accessing the Dashboard

After launching, open in your browser:

```
http://127.0.0.1:8055
```

(or another port specified in the file)

---

## 📌 Notes
- Dashboards run locally as standalone applications  
- Data is based on the Gapminder dataset  
- Interactive visualizations are built with Plotly and Dash  

---

## 👩‍💻 Author
Halyna Yurkova
