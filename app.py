

# import streamlit as st
# import pandas as pd
# import joblib


# # PAGE CONFIG

# st.set_page_config(page_title="Multi Disease Prediction", layout="wide")


# # CUSTOM CSS

# st.markdown("""
# <style>

# /* Background */
# .stApp{
#     background:
#     linear-gradient(rgba(0,0,0,0.65),
#     rgba(0,0,0,0.65)),
#     url("https://images.unsplash.com/photo-1584515933487-779824d29309");
#     background-size: cover;
#     background-position: center;
#     background-attachment: fixed;
# }

# /* Hide Streamlit Branding */
# #MainMenu {visibility:hidden;}
# footer {visibility:hidden;}
# header {visibility:hidden;}

# /* Text */
# h1,h2,h3,h4,p,label,span{
#     color:white !important;
# }

# /* Sidebar */
# section[data-testid="stSidebar"]{
#     background: rgba(0,0,0,0.55);
#     backdrop-filter: blur(15px);
# }

# section[data-testid="stSidebar"] *{
#     color:white !important;
# }

# /* Glass Card */
# .glass{
#     background: rgba(255,255,255,0.08);
#     backdrop-filter: blur(15px);
#     padding: 30px;
#     border-radius: 20px;
#     border: 1px solid rgba(255,255,255,0.1);
#     box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
# }

# /* Inputs */
# .stNumberInput,
# .stSelectbox{
#     border-radius: 10px;
# }

# /* Button */
# .stButton > button{
#     width:100%;
#     height:55px;
#     border:none;
#     border-radius:12px;
#     background:linear-gradient(
#         90deg,
#         #ff5f6d,
#         #ffc371
#     );
#     color:white;
#     font-size:18px;
#     font-weight:600;
# }

# /* Success */
# .success-box{
#     background:rgba(0,255,0,0.15);
#     padding:20px;
#     border-radius:12px;
#     border-left:5px solid #00ff88;
# }

# /* Warning */
# .warning-box{
#     background:rgba(255,255,0,0.15);
#     padding:20px;
#     border-radius:12px;
#     border-left:5px solid orange;
# }

# /* Danger */
# .danger-box{
#     background:rgba(255,0,0,0.15);
#     padding:20px;
#     border-radius:12px;
#     border-left:5px solid red;
# }

# </style>
# """, unsafe_allow_html=True)


# # LOAD MODELS + METRICS

# heart_model = joblib.load("Heart/heart_pipeline.sav")
# cancer_model = joblib.load("Breast_cancer/cancer_model.sav")
# diabetes_model = joblib.load("diabetes/diabetes_model.sav")

# # (optional metrics file - if exists)
# try:
#     heart_metrics = joblib.load("Heart/heart_metrics.sav")
# except:
#     heart_metrics = None


# # TITLE

# st.markdown("<h1 style='text-align:center;'> Multi Disease Prediction System</h1>", unsafe_allow_html=True)


# # SIDEBAR

# st.sidebar.markdown("##  About This App")
# st.sidebar.markdown("""
# ###  Multi Disease Prediction System
# with st.sidebar:

    

# Predict:
# -  Heart Disease  
# -  Breast Cancer  
# - Diabetes  

# ---

# ### ⚙️ How to Use
# 1. Select disease  
# 2. Enter details  
# 3. Click Predict  



# ###  Risk Levels
# 🟢 Low (0–40%)  
# 🟡 Medium (40–70%)  
# 🔴 High (70–100%)

# ###  Disclaimer
# This is an AI-based prediction system, not a medical diagnosis.

#  Zainab Fatima  
# FYP (AI/ML)
# """)

# # REPORT FUNCTION

# def generate_report(data, prediction, prob, disease):
#     return f"""
# Medical Prediction Report 

# Disease: {disease}

# Input Data:
# {data}

# Prediction:
# {"High Risk" if prediction == 1 else "Low Risk"}

# Probability:
# {prob:.2f}%


# """


# # SELECT DISEASE

# disease = st.selectbox("Select Disease", ["Heart Disease", "Breast Cancer", "Diabetes"])

# # ❤️ HEART

# if disease == "Heart Disease":

#     # st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.header(" Heart Disease Prediction")

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         age = st.number_input("Age", 1, 120, 30)
#         sex = st.selectbox("Sex", ["M", "F"])
#         cp = st.selectbox("Chest Pain Type", ["TA", "ATA", "NAP", "ASY"])
#         bp = st.number_input("Resting BP", value=120)

#     with col2:
#         chol = st.number_input("Cholesterol", value=200)
#         fbs = st.selectbox("Fasting BS", [0, 1])
#         restecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
#         hr = st.number_input("Max HR", value=150)

#     with col3:
#         exang = st.selectbox("Exercise Angina", ["Y", "N"])
#         oldpeak = st.number_input("Oldpeak", value=1.0)
#         slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

#     # Encoding
#     sex = 1 if sex == "M" else 0
#     exang = 1 if exang == "Y" else 0
#     cp = {"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3}[cp]
#     restecg = {"Normal": 0, "ST": 1, "LVH": 2}[restecg]
#     slope = {"Up": 0, "Flat": 1, "Down": 2}[slope]

#     input_df = pd.DataFrame([[age, sex, cp, bp, chol, fbs,
#                               restecg, hr, exang, oldpeak, slope]])

#     if st.button(" Predict Heart Disease"):
#         result = heart_model.predict(input_df)
#         prob = heart_model.predict_proba(input_df)[0][1] * 100

#         st.subheader(f" Risk Probability: {prob:.2f}%")

#         if prob > 70:
#             st.error("🔴 High Risk")
#         elif prob > 40:
#             st.warning("🟡 Medium Risk")
#         else:
#             st.success("🟢 Low Risk")

#         # Report
#         report = generate_report(input_df, result[0], prob, "Heart Disease")
#         st.download_button("📄 Download Report", report, "heart_report.txt")

#     # Metrics display
#     if heart_metrics:
#         st.subheader(" Model Performance")
#         st.dataframe(pd.DataFrame(heart_metrics).T)

#     st.markdown('</div>', unsafe_allow_html=True)


# # 🎗️ CANCER

# elif disease == "Breast Cancer":

#     # st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.header(" Breast Cancer Prediction")

#     radius = st.number_input("Radius", 14.0)
#     texture = st.number_input("Texture", 20.0)
#     perimeter = st.number_input("Perimeter", 90.0)
#     area = st.number_input("Area", 600.0)
#     smoothness = st.number_input("Smoothness", 0.1)

#     input_data = pd.DataFrame([[radius, texture, perimeter, area, smoothness] + [0]*25])

#     if st.button(" Predict Cancer"):
#         result = cancer_model.predict(input_data)
#         prob = cancer_model.predict_proba(input_data)[0][1] * 100

#         st.subheader(f" Cancer Probability: {prob:.2f}%")

#         if prob > 70:
#             st.error("🔴 Malignant")
#         elif prob > 40:
#             st.warning("🟡 Medium Risk")
#         else:
#             st.success("🟢 Benign")

#         report = generate_report(input_data, result[0], prob, "Breast Cancer")
#         st.download_button("📄 Download Report", report, "cancer_report.txt")

#     st.markdown('</div>', unsafe_allow_html=True)

# # 🩸 DIABETES

# elif disease == "Diabetes":

#     # st.markdown('<div class="card">', unsafe_allow_html=True)
#     st.header(" Diabetes Prediction")

#     gender = st.selectbox("Gender", ["Male", "Female"])
#     age = st.number_input("Age", 30)
#     hypertension = st.selectbox("Hypertension", [0,1])
#     heart_disease = st.selectbox("Heart Disease", [0,1])
#     smoking = st.selectbox("Smoking", ["never", "former", "current"])
#     bmi = st.number_input("BMI", 25.0)
#     hba1c = st.number_input("HbA1c", 5.5)
#     glucose = st.number_input("Glucose", 100)

#     gender = 1 if gender == "Male" else 0
#     smoking = {"never":0, "former":1, "current":2}[smoking]

#     input_data = pd.DataFrame([[gender, age, hypertension, heart_disease,
#                                 smoking, bmi, hba1c, glucose]],
#                               columns=["gender","age","hypertension","heart_disease",
#                                        "smoking_history","bmi","HbA1c_level","blood_glucose_level"])

#     if st.button(" Predict Diabetes"):
#         result = diabetes_model.predict(input_data)
#         prob = diabetes_model.predict_proba(input_data)[0][1] * 100

#         st.subheader(f" Diabetes Probability: {prob:.2f}%")

#         if prob > 70:
#             st.error("🔴 High Risk")
#         elif prob > 40:
#             st.warning("🟡 Medium Risk")
#         else:
#             st.success("🟢 Low Risk")

#         report = generate_report(input_data, result[0], prob, "Diabetes")
#         st.download_button("📄 Download Report", report, "diabetes_report.txt")

#     st.markdown('</div>', unsafe_allow_html=True)


import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


# PAGE CONFIG

st.set_page_config(page_title="Multi Disease Prediction", layout="wide")


# CUSTOM CSS

st.markdown("""
<style>

/* Background */
.stApp{
    background:
    linear-gradient(rgba(0,0,0,0.65),
    rgba(0,0,0,0.65)),
    url("https://images.unsplash.com/photo-1584515933487-779824d29309");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Text */
h1,h2,h3,h4,p,label,span{
    color:white !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background: rgba(0,0,0,0.55);
    backdrop-filter: blur(15px);
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

/* Glass Card */
.glass{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0px 8px 32px rgba(0,0,0,0.3);
}

/* Inputs */
.stNumberInput,
.stSelectbox{
    border-radius: 10px;
}

/* Button */
.stButton > button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:linear-gradient(
        90deg,
        #ff5f6d,
        #ffc371
    );
    color:white;
    font-size:18px;
    font-weight:600;
}

/* Success */
.success-box{
    background:rgba(0,255,0,0.15);
    padding:20px;
    border-radius:12px;
    border-left:5px solid #00ff88;
}

/* Warning */
.warning-box{
    background:rgba(255,255,0,0.15);
    padding:20px;
    border-radius:12px;
    border-left:5px solid orange;
}

/* Danger */
.danger-box{
    background:rgba(255,0,0,0.15);
    padding:20px;
    border-radius:12px;
    border-left:5px solid red;
}

</style>
""", unsafe_allow_html=True)


# LOAD MODELS + METRICS

heart_model = joblib.load("heart_pipeline.sav")
cancer_model = joblib.load("cancer_model.sav")

# Train diabetes model inline (no .sav file needed)
@st.cache_resource
def train_diabetes_model():
    np.random.seed(42)
    n = 2000
    gender        = np.random.randint(0, 2, n)
    age           = np.random.randint(20, 80, n)
    hypertension  = np.random.randint(0, 2, n)
    heart_disease = np.random.randint(0, 2, n)
    smoking       = np.random.randint(0, 3, n)
    bmi           = np.random.uniform(18, 45, n)
    hba1c         = np.random.uniform(4.0, 9.0, n)
    glucose       = np.random.randint(70, 300, n)

    # Rules based on known diabetes risk factors
    risk = (
        (age > 45).astype(int) +
        hypertension +
        heart_disease +
        (bmi > 30).astype(int) +
        (hba1c > 6.5).astype(int) +
        (glucose > 140).astype(int)
    )
    y = (risk >= 3).astype(int)

    X = pd.DataFrame({
        "gender": gender, "age": age,
        "hypertension": hypertension, "heart_disease": heart_disease,
        "smoking_history": smoking, "bmi": bmi,
        "HbA1c_level": hba1c, "blood_glucose_level": glucose
    })

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    pipeline.fit(X, y)
    return pipeline

diabetes_model = train_diabetes_model()

# (optional metrics file - if exists)
try:
    heart_metrics = joblib.load("heart_metrics.sav")
except:
    heart_metrics = None


# TITLE

st.markdown("<h1 style='text-align:center;'> Multi Disease Prediction System</h1>", unsafe_allow_html=True)


# SIDEBAR

st.sidebar.markdown("##  About This App")
st.sidebar.markdown("""
###  Multi Disease Prediction System
with st.sidebar:

    

Predict:
-  Heart Disease  
-  Breast Cancer  
- Diabetes  

---

### ⚙️ How to Use
1. Select disease  
2. Enter details  
3. Click Predict  



###  Risk Levels
🟢 Low (0–40%)  
🟡 Medium (40–70%)  
🔴 High (70–100%)

###  Disclaimer
This is an AI-based prediction system, not a medical diagnosis.

 Zainab Fatima  
FYP (AI/ML)
""")

# REPORT FUNCTION

def generate_report(data, prediction, prob, disease):
    return f"""
Medical Prediction Report 

Disease: {disease}

Input Data:
{data}

Prediction:
{"High Risk" if prediction == 1 else "Low Risk"}

Probability:
{prob:.2f}%


"""


# SELECT DISEASE

disease = st.selectbox("Select Disease", ["Heart Disease", "Breast Cancer", "Diabetes"])

# ❤️ HEART

if disease == "Heart Disease":

    # st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header(" Heart Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", 1, 120, 30)
        sex = st.selectbox("Sex", ["M", "F"])
        cp = st.selectbox("Chest Pain Type", ["TA", "ATA", "NAP", "ASY"])
        bp = st.number_input("Resting BP", value=120)

    with col2:
        chol = st.number_input("Cholesterol", value=200)
        fbs = st.selectbox("Fasting BS", [0, 1])
        restecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
        hr = st.number_input("Max HR", value=150)

    with col3:
        exang = st.selectbox("Exercise Angina", ["Y", "N"])
        oldpeak = st.number_input("Oldpeak", value=1.0)
        slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    # Encoding
    sex = 1 if sex == "M" else 0
    exang = 1 if exang == "Y" else 0
    cp = {"TA": 0, "ATA": 1, "NAP": 2, "ASY": 3}[cp]
    restecg = {"Normal": 0, "ST": 1, "LVH": 2}[restecg]
    slope = {"Up": 0, "Flat": 1, "Down": 2}[slope]

    input_df = pd.DataFrame([[age, sex, cp, bp, chol, fbs,
                              restecg, hr, exang, oldpeak, slope]])

    if st.button(" Predict Heart Disease"):
        result = heart_model.predict(input_df)
        prob = heart_model.predict_proba(input_df)[0][1] * 100

        st.subheader(f" Risk Probability: {prob:.2f}%")

        if prob > 70:
            st.error("🔴 High Risk")
        elif prob > 40:
            st.warning("🟡 Medium Risk")
        else:
            st.success("🟢 Low Risk")

        # Report
        report = generate_report(input_df, result[0], prob, "Heart Disease")
        st.download_button("📄 Download Report", report, "heart_report.txt")

    # Metrics display
    if heart_metrics:
        st.subheader(" Model Performance")
        st.dataframe(pd.DataFrame(heart_metrics).T)

    st.markdown('</div>', unsafe_allow_html=True)


# 🎗️ CANCER

elif disease == "Breast Cancer":

    # st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header(" Breast Cancer Prediction")

    radius = st.number_input("Radius", 14.0)
    texture = st.number_input("Texture", 20.0)
    perimeter = st.number_input("Perimeter", 90.0)
    area = st.number_input("Area", 600.0)
    smoothness = st.number_input("Smoothness", 0.1)

    input_data = pd.DataFrame([[radius, texture, perimeter, area, smoothness] + [0]*25])

    if st.button(" Predict Cancer"):
        result = cancer_model.predict(input_data)
        prob = cancer_model.predict_proba(input_data)[0][1] * 100

        st.subheader(f" Cancer Probability: {prob:.2f}%")

        if prob > 70:
            st.error("🔴 Malignant")
        elif prob > 40:
            st.warning("🟡 Medium Risk")
        else:
            st.success("🟢 Benign")

        report = generate_report(input_data, result[0], prob, "Breast Cancer")
        st.download_button("📄 Download Report", report, "cancer_report.txt")

    st.markdown('</div>', unsafe_allow_html=True)

# 🩸 DIABETES

elif disease == "Diabetes":

    # st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header(" Diabetes Prediction")

    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", 30)
    hypertension = st.selectbox("Hypertension", [0,1])
    heart_disease = st.selectbox("Heart Disease", [0,1])
    smoking = st.selectbox("Smoking", ["never", "former", "current"])
    bmi = st.number_input("BMI", 25.0)
    hba1c = st.number_input("HbA1c", 5.5)
    glucose = st.number_input("Glucose", 100)

    gender = 1 if gender == "Male" else 0
    smoking = {"never":0, "former":1, "current":2}[smoking]

    input_data = pd.DataFrame([[gender, age, hypertension, heart_disease,
                                smoking, bmi, hba1c, glucose]],
                              columns=["gender","age","hypertension","heart_disease",
                                       "smoking_history","bmi","HbA1c_level","blood_glucose_level"])

    if st.button(" Predict Diabetes"):
        result = diabetes_model.predict(input_data)
        prob = diabetes_model.predict_proba(input_data)[0][1] * 100

        st.subheader(f" Diabetes Probability: {prob:.2f}%")

        if prob > 70:
            st.error("🔴 High Risk")
        elif prob > 40:
            st.warning("🟡 Medium Risk")
        else:
            st.success("🟢 Low Risk")

        report = generate_report(input_data, result[0], prob, "Diabetes")
        st.download_button("📄 Download Report", report, "diabetes_report.txt")

    st.markdown('</div>', unsafe_allow_html=True)