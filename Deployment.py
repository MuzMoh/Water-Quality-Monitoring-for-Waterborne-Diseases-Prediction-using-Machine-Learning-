import streamlit as st
import numpy as np
import pickle
import sklearn
import tensorflow as tf
import keras

print('The scikit-learn version is {}.'. format(sklearn. __version__))
print('The scikit-learn version is {}.'. format(tf. __version__))
print('The scikit-learn version is {}.'. format(keras. __version__))

model = pickle.load(open('C://Users/hglor/OneDrive/Desktop/FYP Submission/best_model.pkl','rb'))

def classify_water(DO, PH, cond, bod, ni, fec_col, tot_col):
    #Taking in values as float
    input_raw = np.array([DO, PH, cond, bod, ni, fec_col, tot_col]).astype(float)
    
    #MinMaxScaler Alternative Calculation
    DO_trans = (input_raw[0] - 2.5) / (10 - 2.5)
    PH_trans = (input_raw[1] - 0) / (9.01 - 0)
    cond_trans = (input_raw[2] - 11) / (18291 - 11)
    bod_trans = (input_raw[3] - 0.1) / (7.8 - 0.1)
    ni_trans = (input_raw[4] - 0) / (11 - 0)
    fec_col_trans = (input_raw[5] - 0) / (2367 - 0)
    tot_col_trans = (input_raw[6]- 0) / (66382 - 0)
    input_trans = [[DO_trans, PH_trans, cond_trans, bod_trans, ni_trans, fec_col_trans, tot_col_trans]]
    
    #Model classifcation
    classify = model.predict(input_trans)
    return classify[0]
    

    
    
def main():
    st.title("Water Quality Classification")
    st.subheader("FYP Assignment")
    st.markdown("The application below is used to classify water sources and determine whether they are safe for usage or not based on 7 variables which are pH, dissolved oxygen (mg/l), conductivity (umhos/cm), biological oxygen demand (mg/l), fecal coliform (mpn/100 ml) and the total coliform, which is the average fecal coliform measure over a period of time.")


    do = st.text_area("Select the water's dissolved oxygen (mg/l) ")    
    ph = st.text_area("Select the water's pH ")    
    cond = st.text_area("Select the water's conductivity (umhos/cm) ")    
    bod = st.text_area("Select the water's biological oxygen demand (mg/l) ")    
    ni = st.text_area("Select the water's nitratenan (mg/l) ")    
    fec_col = st.text_area("Select the water's fecal coliform (mpn/100ml) ")    
    tot_col = st.text_area("Select the water's total coliform (mpn/100ml mean) ")
    
    
    if st.button("Classify"):
        classi = classify_water(do, ph, cond, bod, ni, fec_col, tot_col)
        if classi == 1:
            st.success('The water is safe for usage')
        if classi == 0:
            st.error('The water is unsafe for usage')
        

#RUN MAIN
main()