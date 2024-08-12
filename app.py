import streamlit as st
import pickle
import numpy as np
from scipy.sparse import hstack

# Load the trained model and encoders
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('location_ohe.pkl', 'rb') as loc_file:
    location_ohe = pickle.load(loc_file)

with open('work_type_ohe.pkl', 'rb') as work_type_file:
    work_type_ohe = pickle.load(work_type_file)

with open('experience_level_ohe.pkl', 'rb') as exp_level_file:
    experience_level_ohe = pickle.load(exp_level_file)

with open('tfidf_vectorizer_title.pkl', 'rb') as title_vectorizer_file:
    tfidf_vectorizer_title = pickle.load(title_vectorizer_file)

with open('tfidf_vectorizer_skills.pkl', 'rb') as skills_vectorizer_file:
    tfidf_vectorizer_skills = pickle.load(skills_vectorizer_file)

# Streamlit UI
st.title("Salary Prediction")

# Collect user input
title = st.text_input("Job Title")
location = st.text_input("Location")
work_type = st.selectbox("Work Type", ["Full-time", "Part-time", "Contract", "Temporary", "Other"])
experience_level = st.selectbox("Experience Level", ["Entry-level", "Mid-level", "Senior-level", "Manager", "Executive"])
skills = st.text_area("Skills Required")
views = st.number_input("Number of Views", min_value=0)
applies = st.number_input("Number of Applies", min_value=0)

if st.button("Predict Salary"):
    # Transform the input data
    title_tfidf = tfidf_vectorizer_title.transform([title])
    skills_tfidf = tfidf_vectorizer_skills.transform([skills])
    location_encoded = location_ohe.transform([[location]])
    work_type_encoded = work_type_ohe.transform([[work_type]])
    experience_level_encoded = experience_level_ohe.transform([[experience_level]])
    numerical_features = np.array([[views, applies]])

    # Combine all features
    combined_features = hstack([
        title_tfidf,
        skills_tfidf,
        location_encoded,
        work_type_encoded,
        experience_level_encoded,
        numerical_features
    ])

    # Predict the salary
    predicted_salary = model.predict(combined_features)
    st.write(f"Predicted Salary: ${predicted_salary[0]:,.2f}")
