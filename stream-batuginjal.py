
import pickle
import streamlit as st

#Membaca Model
ginjal_model = pickle.load(open('penyakit_batu_ginjal.sav', 'rb'))

#Judul Web
st.title('DATA MINING PREDIKSI BATU GINJAL')

st.subheader('NAMA : HERMAN KURNIAWAN GULO')
st.subheader('NIM : 191351036')

Gravity = st.text_input(' Input Nilai Gravity')

Ph = st.text_input ('Input Nilai Ph')

Osmo = st.text_input (' Input Nilai Osmo')

Cond = st.text_input ('Input Nilai Cond')

Urea = st.text_input (' Input Nilai Urea')

Calc = st.text_input (' Input Nilai Calc')

#code untuk prediksi
ginjal_diagnosis = ''

#membuat tombol
if st.button('Test') :
    ginjal_prediction = ginjal_model.predict([[Gravity, Ph, Osmo, Cond, Urea, Calc]])
    
    if  (ginjal_prediction[0] == 1):
           ginjal_diagnosis = 'Pasien terkena Batu Ginjal'
    else :
           ginjal_diagnosis = ' Pasien tidak terkena Batu Ginjal'

    st.success(ginjal_diagnosis)