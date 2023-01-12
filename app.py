import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt

# col1, col2 = st.columns([1, 3])
st.title('Phishing Website Detection using Machine Learning Algorithms')

choice = st.selectbox("Please select a machine learning model",
                 [
                     'Gaussian Naive Bayes', 'Decision Tree', 'Random Forest',
                     'K-Neighbours', 'SVM'
                 ]
                )

model = ml.nb_model

if choice == 'Gaussian Naive Bayes':
    model = ml.nb_model
    st.write('Naive Bayes model is selected!')

elif choice == 'Decision Tree':
    model = ml.dt_model
    st.write('Decision Tree model is a selected!')

elif choice == 'Random Forest':
    model = ml.rf_model
    st.write('Random Forest model is selected!')

elif choice == 'SVM':
    model = ml.svm_model
    st.write('SVM model is selected!')


url = st.text_input('Enter the URL')
if st.button('Check'):
    try:
        response = re.get(url, verify=False, timeout=4)
        if response.status_code != 200:
            st.warning("Attention! This website is a potential PHISHING!")
            st.warning('Phishing alert', icon="⚠️")
        else:
            soup = BeautifulSoup(response.content, "html.parser")
            vector = [fe.create_vector(soup)]
            result = model.predict(vector)
            if result[0] == 0:
                st.success("This website is legitimate!")
                st.success('Real Website!', icon="✅")
            else:
                st.warning("Attention! This website is a potential PHISHING!")
                st.warning('Phishing alert', icon="⚠️")

    except re.exceptions.RequestException as e:
        print("--> ", e)





