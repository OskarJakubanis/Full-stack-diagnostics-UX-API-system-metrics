# 📊 Full stack diagnostics: UX, API, system-metrics


This project provides a modular analytics pipeline to help teams understand user behavior, system reliability, and support effectiveness using simulated front office and backend data.

---

## 🎯 Objectives

- Analyze front office data such as user clicks, abandoned carts, and page load times to understand customer engagement and friction points.  
- Monitor backend system performance, including API errors, server response times, and service availability.  
- Track support ticket volume, resolution times, and common issues to evaluate customer service effectiveness.  
- Generate PDF summaries for stakeholders.  
- Provide actionable insights that help improve customer experience, optimize system reliability, and enhance support operations.

---

## ⚙️ Technologies Used

- Python 3.9+
- `pandas` for data manipulation and analysis  
- `textblob` for sentiment analysis (`analyze_feedback.py`)  
- `matplotlib.pyplot` for basic visualizations

📁 Required libraries are listed in [`requirements.txt`](./requirements.txt)  
📖 Function-level usage is documented in [`used_functions.md`](./used_functions.md)

---

## 🧪 Project Workflow

1. Review the data `data_description.md` to understand the structure and content of the CSV files.  
2. Clone the repository.  
3. Run each analysis script (.py) to generate KPIs, summary statistics, and plots.  
4. Check the console output for insights

*In `.py` files, `#` comments show step-by-step procedures.*  
*Refer to `used_functions.md` for an overview of key Python and library functions used.*  

---

## 📬 Contact

For questions, suggestions, or collaboration proposals, please [open an issue](https://github.com/your-repo/issues) or contact me directly.
