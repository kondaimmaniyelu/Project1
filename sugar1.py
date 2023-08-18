import pickle
import streamlit as st
import numpy as np
pickle_in=open('c:/ML app/sugar.pkl','rb')
model=pickle.load(pickle_in)

def main():
    html_temp='''
    <div style="background-color:green;padding:13px">
    <h1 style="color:black;text-align:center;">DIABETIES PREDICTION</h1>
    </div>'''

    st.markdown(html_temp,unsafe_allow_html=True)
    preg=st.number_input("Pregnancies")
    glucose=st.number_input('Glucose')
    bp=st.number_input('BloodPressure')
    st=st.number_input("SkinTheckness")
    i=st.number_input("Insulin")
    bmi=st.number_input('BMI')
    dpf=st.number_input('DiabetesPedigreeFunction')
    age=st.number_input('Age')
    result=''

    if st.button('PREDICT'):
        result=prediction(preg,glucose,bp,st,i,bmi,dpf,age)
        st.success('RISK IS {}'.format(result))

def prediction(preg,glucose,bp,st,i,bmi,dpf,age):
    s=clf.predict([[preg,glucose,bp,st,i,bmi,dpf,age]])
    if s==1:
        p='HAD DIABETIES'
    else:
        p='U R SAFE'
    return p

if __name__=='__main__':
    main()



#Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	Outcome
