 🧾 Fakebills Prediction Using K-Nearest Neighbors (KNN)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)]()

## 📌 Overview
This project uses **K-Nearest Neighbors (KNN)** to predict whether a bill is genuine or counterfeit 💰 based on features like dimensions 📏, weight ⚖️, and print quality 🖨️.  
It includes:
- 🔹 Data preprocessing
- 🔹 Feature scaling
- 🔹 Model training & evaluation
- 🔹 A **Flask** web app for real-time predictions

---

## ✨ Features
✅ **Data Preprocessing** – Cleans, scales, and prepares datasets 📊  
✅ **Model Training** – Implements KNN for classification 🤖  
✅ **Web Interface** – Flask app for live predictions 💻  
✅ **Exploratory Analysis** – Visual insights 📈

---

## 📂 Table of Contents
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [📁 Project Structure](#-project-structure)
- [📊 Results](#-results)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [📬 Contact](#-contact)

---

## ⚙️ Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/Srinithimahalakshmi/Fakebills_prediction.git
    cd Fakebills_prediction
    ```

2. **Set up virtual environment & install dependencies**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

---

## 🚀 Usage

### 📓 Notebook Mode
Run the notebook for model training & evaluation:
```bash
jupyter notebook model_training.ipynb
````

### 🌐 Flask App Mode

Run the web app for predictions:

```bash
python app.py
```

Visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** and enter bill details to get a result 🏦.

---

## 📁 Project Structure

| File / Folder             | Description                          |
| ------------------------- | ------------------------------------ |
| 📒 `model_training.ipynb` | EDA, training, evaluation, and plots |
| 📂 `fake_bills.csv`       | Dataset                              |
| 🖥️ `app.py`              | Flask web app                        |
| 📂 `templates/`           | HTML files                           |
| 🎨 `static/`              | CSS/JS files                         |
| 💾 `model/`               | Trained model files                  |

---

## 📊 Results

* **Accuracy**: `XX%` 📈
* Includes confusion matrix, classification report, and graphs 📉📊
  *(Update with actual metrics from your training)*

---

## 🤝 Contributing

Contributions are welcome!
You can:

* 🚀 Improve accuracy
* 🎨 Enhance UI
* 🐞 Fix bugs
* 📚 Add documentation

To contribute:

1. Fork the repo 🍴
2. Create a new branch 🌿
3. Commit your changes 💾
4. Open a Pull Request 📬

---

## 📜 License

This project is licensed under the **MIT License**.
See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com]
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

💡 *If you like this project, don’t forget to ⭐ the repo!*

```

---

If you want, I can make this into a **ready-to-download README.md file** so you can directly push it to your repo without copy-pasting. Would you like me to prepare that?
```
