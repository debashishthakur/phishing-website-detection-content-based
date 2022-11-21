import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as re
import matplotlib.pyplot as plt

# col1, col2 = st.columns([1, 3])
[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
textColor="#000000"
font="sans serif"

st.title('Phishing Website Detection using Machine Learning Algorithms')

choice = st.selectbox("Please select a machine learning model",
                 [
                     'Gaussian Naive Bayes', 'Support Vector Machine', 'Decision Tree', 'Random Forest',
                     'AdaBoost', 'Neural Network', 'K-Neighbours'
                 ]
                )

model = ml.nb_model

if choice == 'Gaussian Naive Bayes':
    model = ml.nb_model
elif choice == 'Support Vector Machine':
    model = ml.svm_model
elif choice == 'Decision Tree':
    model = ml.dt_model
elif choice == 'Random Forest':
    model = ml.rf_model
elif choice == 'AdaBoost':
    model = ml.ab_model
elif choice == 'Neural Network':
    model = ml.nn_model
else:
    model = ml.kn_model
    st.write('KN model is selected!')


url = st.text_input('Enter the URL')
# check the url is valid or not
if st.button('Check'):
    try:
        response = re.get(url, verify=False, timeout=4)
        if response.status_code != 200:
            print(". HTTP connection was not successful for the URL: ", url)
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





