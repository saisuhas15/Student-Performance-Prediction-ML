import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("student_model.joblib")

st.title("Student Performance Prediction")

st.write(
    "Predict student examination marks "
    "using Machine Learning."
)

studytime = st.selectbox(
    "Weekly Study Time",
    [1, 2, 3, 4]
)

failures = st.selectbox(
    "Previous Failures",
    [0, 1, 2, 3, 4]
)

absences = st.number_input(
    "Number of Absences",
    min_value=0,
    max_value=93,
    value=4
)

G1 = st.slider(
    "First Examination Marks",
    0, 20, 15
)

G2 = st.slider(
    "Second Examination Marks",
    0, 20, 16
)

if st.button("Predict Final Marks"):

    input_data = pd.DataFrame(
        [[studytime, failures, absences, G1, G2]],
        columns=[
            "studytime",
            "failures",
            "absences",
            "G1",
            "G2"
        ]
    )

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Final Marks: {prediction[0]:.2f}/20"
    )