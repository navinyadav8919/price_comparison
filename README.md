## 📅 E-Pharmacy Price Comparison System

A web-based application that helps users compare medicine prices across multiple e-pharmacies using **Google Shopping data**. Built with **Python**, **Streamlit**, and **SerpAPI** to offer a simple, interactive way to find the best deals on medicines in real time.

---

###  Features

*  Search for any medicine
*  Compare real-time prices across various platforms
*  Automatically highlights the best (lowest) price
*  Visualize price comparison using bar and pie charts
*  Responsive and clean Streamlit UI

---

###  Tech Stack

* **Frontend & UI:** Streamlit
* **Backend/Data:** Python, Pandas, Matplotlib
* **API:** [SerpAPI (Google Shopping)](https://serpapi.com/)
* **Hosting:** Streamlit Cloud

---

###  How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/navinyadav8919/price_comparison.git
   cd price_comparison
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your SerpAPI key**

   Create a `.streamlit/secrets.toml` file:

   ```toml
   serpapi_key = "YOUR_API_KEY_HERE"
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

### 📂 Project Structure

```
price_comparison/
│
├── app.py                   # Main Streamlit application
├── requirements.txt         # Required Python packages
├── logo.png                       
```

---

###  Acknowledgements

* [Streamlit](https://streamlit.io/)
* [SerpAPI](https://serpapi.com/)
* [Google Shopping](https://shopping.google.com/)

---

### 📬 Feedback

Feel free to open issues or reach out with ideas, improvements, or bugs.
If you find this useful, give the repo a ⭐!
