import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie


# loading the saved models

diabetes_model = pickle.load(open('models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('models/parkinsons_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('HealthPal',
                          
                          ['Home',
                           'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'About Us'],
                          icons=['house','activity','heart','person','people-fill'],
                          default_index=0)

#home
if (selected == 'Home'):
    st.markdown(""" <style> .font {
                font-size:90px ; text-align:center; font-weight: bold; font-family: 'Courier New'; color:#A0D6B4;} 
                </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">HealthPal</p>', unsafe_allow_html=True)

    coli1,coli2=st.columns([2,2])
    
    coli1.image("https://cdn0.iconfinder.com/data/icons/medical-services-2-1/256/Doctor_on_Duty-512.png")

    coli2.write("<p style='color:grey; font-size:18px; font-family: 'Georgia';font-weight: bold;'>Our web application stands at the intersection of healthcare and technology, empowered by cutting-edge Python models that predict a spectrum of health conditions. The realm of modern healthcare confronts numerous complex challenges, such as limited accessibility to comprehensive health data, potential inaccuracies in diagnostics, and the need for personalized treatment plans. </p>",unsafe_allow_html=True)

    coli2.write("<p style='color:grey; font-size:18px; font-family: 'Georgia';font-weight: bold;'>At the core of our mission is the goal to democratize healthcare. We aspire to mitigate disparities in healthcare access and empower individuals by leveraging technology. Our app embodies this vision, emphasizing the transformative role of technology in the medical landscape. Through our initiative, we envision a future where informed and proactive healthcare decisions are within reach of all.</p>",unsafe_allow_html=True)

    st.write('---')







# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.write("<p style='color:Lightgreen; font-size:45px; font-family: 'Courier New';font-weight: bold;'>Diabetes Prediction</p>",unsafe_allow_html=True)

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col2:
        Insulin = st.text_input('Insulin Level')
    
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.write("<p style='color:Lightgreen; font-size:45px; font-family: 'Courier New';font-weight: bold;'>Heart Disease Prediction</p>",unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.write("<p style='color:Lightgreen; font-size:45px; font-family: 'Courier New';font-weight: bold;'>Parkinson's Disease Prediction</p>",unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


if (selected == 'About Us'):
    
    # page title
    st.markdown(""" <style> .font {
font-size:50px ; text-align:center; font-weight: bold; font-family: 'Courier New'; color:#98FF98;} 
</style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About Us</p>', unsafe_allow_html=True)

    #desc
    st.write("<p style='color:green ;text-align:center; font-size: 20px;font-family:'Courier New'; font-weight: bold;'>We are a committed team of developers who have crafted a web application employing Python models to predict various health conditions. Our objective is to offer precise forecasts, enabling individuals to take proactive measures in managing their well-being effectively.</p>",unsafe_allow_html=True)
    st.write("---")
    st.write("<p style='color:lightGreen; font-size:40px; font-family:'Courier New';font-weight: bold;'>Our team</p>",unsafe_allow_html=True)
    
    coli3,coli1,coli2=st.columns([1,2,2])

    #shelly-----------------------------------------
    coli1.image("pp4.jpg",width=120)
    coli1.write("<p style='color:lightgreen; font-size: 25px; font-family: 'Georgia';font-weight: bold;'>Shelly Bhalla</p>",unsafe_allow_html=True)
    
    linkedin_url="https://www.linkedin.com/in/shelly-bhalla-58a7271b6"
    github_url="https://github.com/Shellybhalla13"
    twitter_url="https://twitter.com/ShellyBhalla13?t=1cMosdgxkkk2bug_bT1Wxw&s=09"
    
    linkedin_icon="https://static.vecteezy.com/system/resources/previews/017/339/624/original/linkedin-icon-free-png.png"
    github_icon="https://cdn0.iconfinder.com/data/icons/shift-logotypes/32/Github-512.png"
    twitter_icon="https://th.bing.com/th/id/OIP.mjoG94zAqNefzlni3m2hRgHaHa?pid=ImgDet&rs=1"

    coli1.write("<p style='color:green; font-size:20px; font-family: 'Georgia';font-weight: bold;'>Connect with me</p>",unsafe_allow_html=True)
    coli1.markdown(f'<a href="{github_url}"><img src="{github_icon}" width="40" height="35"></a>'
            f'<a href="{linkedin_url}"><img src="{linkedin_icon}" width="60" height="60"></a>'
            f'<a href="{twitter_url}"><img src="{twitter_icon}" width="40" height="38"></a>',unsafe_allow_html=True)

    #riya-----------
    coli2.image("pp5.jpg",width=110)
    coli2.write("<p style='color:Lightgreen; font-size: 25px; font-family: 'Georgia';font-weight: bold;'>Riya Gupta</p>",unsafe_allow_html=True)
    
    linkedin_url2="https://www.linkedin.com/in/riya-gupta-16b51b239"
    github_url2="https://github.com/Riyagupta0204"
    twitter_url2="https://mobile.twitter.com/riyagup56989166"

    linkedin_icon="https://static.vecteezy.com/system/resources/previews/017/339/624/original/linkedin-icon-free-png.png"
    github_icon="https://cdn0.iconfinder.com/data/icons/shift-logotypes/32/Github-512.png"
    twitter_icon="https://th.bing.com/th/id/OIP.mjoG94zAqNefzlni3m2hRgHaHa?pid=ImgDet&rs=1"

    coli2.write("<p style='color:green; font-size:20px; font-family: 'Georgia';font-weight: bold;'>Connect with me</p>",unsafe_allow_html=True)
    coli2.markdown(f'<a href="{github_url2}"><img src="{github_icon}" width="40" height="35"></a>'
            f'<a href="{linkedin_url2}"><img src="{linkedin_icon}" width="60" height="60"></a>'
            f'<a href="{twitter_url2}"><img src="{twitter_icon}" width="40" height="38"></a>',unsafe_allow_html=True)

    