
# New-Plant-Disease-Prediction

## Plant Disease Prediction Using AI

This project focuses on detecting plant diseases from leaf images using machine learning and deep learning techniques. The goal is to help farmers, gardeners, and researchers identify plant health issues at an early stage so that timely treatment can be applied and crop loss can be minimized.

The system uses Convolutional Neural Networks (CNNs) along with image preprocessing to improve prediction accuracy and provide useful disease insights.

---

## Features

* Predicts plant diseases from leaf images
* Supports multiple crops such as tomato, potato, corn, and more
* Deep learning model based on CNN architecture
* Image preprocessing and normalization
* Displays predicted disease name
* Provides brief treatment or management suggestions
* Simple web interface for easy interaction

---

## Dataset

Source: Kaggle – New Plant Diseases Dataset
[https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

---

## Tech Stack

**Machine Learning / Deep Learning**

* TensorFlow / Keras
* Scikit-learn

**Data Processing**

* NumPy
* Pandas

**Visualization**

* Matplotlib
* Seaborn

**Web Application**

* Streamlit

---

## Project Structure

```
New-Plant-Disease-Prediction/
│
├── main/                # Streamlit application
├── models/              # Trained model files
├── notebooks/           # Experiments / training
├── data/                # Dataset (if stored locally)
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/New-Plant-Disease-Prediction.git
cd New-Plant-Disease-Prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

(Or install manually from the list below.)

---

## Requirements

* tensorflow==2.10.0
* scikit-learn==1.3.0
* numpy==1.24.3
* matplotlib==3.7.2
* seaborn==0.13.0
* pandas==2.1.0
* streamlit
* librosa==0.10.1

---

## Running the Web Application

```bash
cd main
streamlit run main.py
```

After running, open your browser and go to:

```
http://localhost:8501
```

---

## How It Works

1. User uploads a leaf image.
2. The image is resized and preprocessed.
3. The CNN model analyzes patterns and features.
4. The system predicts the disease class.
5. The result along with basic treatment guidance is displayed.

---

## Future Goals

* Extend support to additional crops and disease categories
* Improve model performance and reduce inference time
* Build a mobile-friendly application
* Integrate IoT or sensor-based real-time monitoring
* Enhance fertilizer and treatment recommendations
* Collaborate with agricultural experts for better validation
* Deploy using scalable cloud infrastructure

---

## Author

Developed and maintained by **Suhani Kumari**.

---
