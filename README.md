# 🎓 Student Performance Prediction Using Machine Learning

## 📌 Project Overview

The Student Performance Prediction System is a Machine Learning project that predicts students' final examination marks based on their academic performance and study habits.

The system uses the Random Forest Regression algorithm to analyze student data and estimate final grades. An interactive web application is developed using Streamlit, allowing users to enter student details and view predicted results.

This project demonstrates the practical application of Machine Learning in the education domain.

## 🎯 Objectives

- Predict students' final examination marks using Machine Learning.
- Analyze the relationship between study habits and academic performance.
- Build an interactive web application for predictions.
- Understand the complete ML workflow, from data preprocessing to model deployment.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Pandas | Data Processing |
| NumPy | Numerical Computation |
| Scikit-learn | Machine Learning |
| Random Forest Regression | Prediction Algorithm |
| Streamlit | Web Application |
| Joblib | Model Serialization |
| VS Code | Development Environment |
| Git & GitHub | Version Control |

## 🧠 Machine Learning Algorithm

**Random Forest Regression**

Random Forest Regression is an ensemble learning algorithm that combines multiple decision trees to predict continuous values.

In this project, it predicts the final examination grade using the following features:

- Study Time
- Previous Failures
- Number of Absences
- First Examination Grade (G1)
- Second Examination Grade (G2)

The target variable is the final examination grade (G3).

## 📊 Dataset

**Dataset:** Student Performance Dataset

**Source:** UCI Machine Learning Repository

[Download Dataset](https://archive.ics.uci.edu/dataset/320/student+performance)

The dataset contains student academic, demographic, and social information.

This project uses selected academic features for training the prediction model.

## 📂 Project Structure

```text
Student-Performance-Prediction-ML/
│
├── train.py
├── app.py
├── student_model.joblib
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Student-Performance-Prediction-ML.git
```

### 2. Navigate to the Project Folder

```bash
cd Student-Performance-Prediction-ML
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Train the Machine Learning Model

```bash
python train.py
```

This step downloads the dataset, trains the Random Forest model, evaluates its performance, and saves the trained model as `student_model.joblib`.

### 5. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🚀 Application Features

- Interactive student input form
- Study time selection
- Previous failure information
- Attendance information
- Previous examination marks
- Final examination marks prediction
- User-friendly Streamlit interface

## 📈 Model Evaluation

The model is evaluated using the following metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

These metrics help measure the prediction performance of the trained model.

## 🔮 Future Enhancements

- Compare multiple Machine Learning algorithms.
- Add data visualization and performance graphs.
- Provide personalized study recommendations.
- Integrate a MySQL database.
- Add student login and registration.
- Deploy the application using Streamlit Community Cloud.
- Improve prediction performance using additional features.

## ⚠️ Disclaimer

This project is developed for educational purposes.

The predictions are estimates based on the dataset used for training. They should not be considered as guaranteed academic results.

## 👨‍💻 Author

**Your Name**

B.Tech – Computer Science and Engineering (AI & ML)

GitHub: [saisuhas15](https://github.com/saisuhas15/Student-Performance-Prediction-ML.git)

---

⭐ If you find this project useful, consider giving it a star!

## 🌐 Live Demo

🚀 Try the application here:

[Student Performance Prediction – Live App](https://student-performance-prediction-ml-cbftglvrpiwt7bttmmejw7.streamlit.app/)