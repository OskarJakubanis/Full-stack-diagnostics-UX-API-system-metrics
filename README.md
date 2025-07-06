# 📊 E-commerce Behavior & System Monitoring Suite

This project provides a modular analytics pipeline to help digital teams understand user behavior, system reliability, and support effectiveness using simulated front office and backend data.

---

## 🎯 Objectives

- Analyze front office data such as user clicks, abandoned carts, and page load times to understand customer engagement and friction points.  
- Monitor backend system performance, including API errors, server response times, and service availability.  
- Track support ticket volume, resolution times, and common issues to evaluate customer service effectiveness.  
- Generate dashboards and automated reports (Power BI dashboards, PDF summaries) for stakeholders such as managers, UX teams, IT, and support staff.  
- Provide actionable insights that help improve customer experience, optimize system reliability, and enhance support operations.

---

## 🧾 Data Sources

- `clickstream.csv`: Simulated user click data on website elements  
- `cart_abandonment.csv`: Records of abandoned shopping carts  
- `page_load_times.csv`: Measurements of page loading durations  
- `api_logs.csv`: Backend API call logs with status codes and response times  
- `user_feedback.csv`: Free-text feedback with numerical ratings  
- `session_tracking.csv`: Session-level browsing behavior with entry and exit points  

---

## ⚙️ Technologies Used

- Python 3.9+
- `pandas` for data manipulation and analysis  
- `textblob` for sentiment analysis (`analyze_feedback.py`)  
- `matplotlib.pyplot` for basic visualizations

📁 Required libraries are listed in [`requirements.txt`](./requirements.txt)  
📖 Function-level usage is documented in [`used_functions.md`](./used_functions.md)

---

## 📁 Script Overview

Each script targets a specific part of the data pipeline:

- `analyze_api_logs.py` – API performance, error rates, and slow services  
- `analyze_feedback.py` – Sentiment vs rating consistency  
- `analyze_sessions.py` – Session durations and drop-off pages  
- `analyse_cart_abandonment.py` – Abandonment patterns and lost revenue  
- `analyse_clickstream.py` – User interaction intensity and most clicked elements  
- `analyse_page_load_times.py` – Frontend speed and slowest URLs

---

## 🧪 Project Workflow

1. Clone the repository.
2. Review the available CSV files in the data/ directory.
3. Run each analysis script (.py) to generate KPIs, summary statistics, and plots.
4. Check the console output for insights.
5. Refer to used_functions.md for an overview of key Python and library functions used.

---

## 📬 Contact

For questions, suggestions, or collaboration proposals, please [open an issue](https://github.com/your-repo/issues) or contact me directly.
