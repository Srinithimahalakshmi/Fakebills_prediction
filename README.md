
#  Fake Bills Prediction Using K-Nearest Neighbors (KNN)

##  Overview
This project detects counterfeit currency using a **K-Nearest Neighbors (KNN)** model. It includes data preprocessing, feature scaling, model training, evaluation, and a simple web interface for real-time predictions. Designed for quick experimentation and clarity.

---

##  Table of Contents
- [⚙️ Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📁 Project Structure](#-project-structure)  
- [📊 Results](#-results)  
- [🤝 Contributing](#-contributing)  
- [📬 Contact](#-contact)  

---

##  Installation
```bash
git clone https://github.com/Srinithimahalakshmi/Fakebills_prediction.git
cd Fakebills_prediction

python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
pip install -r requirements.txt
````

---

## Usage

### Notebook for Model Training

Launch the Jupyter notebook to explore data, train the model, and visualize performance:

```bash
jupyter notebook model_training.ipynb
```

### Run Flask Web App

Start the app for interactive predictions:

```bash
python app.py
```

Navigate to **[http://127.0.0.1:5000](http://127.0.0.1:5000)** and input features such as length, width, and texture to receive a KNN-based authenticity prediction.

---

## Project Structure

```
Fakebills_prediction/
├── fake_bills.csv                  # Dataset with features and labels
├── model_training.ipynb           # Data exploration & model development
├── app.py                         # Flask application script
├── templates/
│   └── index.html                 # Web-based input form
├── static/
│   └── style.css                  # CSS for the web interface
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
```

---

## Results

* **Model Accuracy**: `XX%`
* **Visuals**: Confusion matrix, classification report, feature impact plots are generated within the notebook (or `results/` folder if available).

*(Update with actual values and reference any saved report files.)*

---

## Contributing

Your help is welcome! You can:

* Add support for other models (e.g., SVM, Random Forest)
* Improve the UI with better input forms or result displays
* Include model explainability (e.g., feature importance or SHAP)
* Enhance data preprocessing or testing datasets

To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m "Add <feature>"`
4. Push your branch and open a Pull Request

---

## Contact

👤 **Maintainer**: Srinithi Mahalakshmi
📧 **Email**: [srinithiarumugam2003@gmail.com](mailto:srinithiarumugam2003@gmail.com)
🔗 **GitHub**: [Srinithimahalakshmi](https://github.com/Srinithimahalakshmi)

---

⭐ *If this project was helpful or interesting, feel free to give it a star!*

