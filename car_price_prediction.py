import pandas as pd
import datetime
import xgboost as xgb
import streamlit as st
import os

def main():
    model_path = os.path.join("C:\\Users\\USER\\Desktop\\Machine Learning", "xgb_model.json")  
    model = xgb.XGBRegressor()
    model.load_model(model_path)
    
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:center;">Car Price Prediction Using ML</h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    st.write('')
    st.write('')

    st.markdown("##### PLANNING TO SELL YOUR CAR?\n##### Let's Evaluate it!")

    p1 = st.number_input("Current RETAIL PRICE of the vehicle(In Philippine Peso)",10000.0,10000000.0,step=1.0)
    p2 = st.number_input("Distance of the vehicle in KILOMETERS",100,500000,step=100)
    s1 = st.selectbox("FUEL TYPE",('Gasoline','Diesel','CNG','LPG','Electric'))

    if s1 == "Gasoline":
        p3=0
    elif s1 =="Diesel":
        p3=1
    elif s1 =="CNG":
        p3=2
    elif s1 =="LPG":
        p3=3
    elif s1 =="Electric":
        p3=4
    s2 = st.selectbox("Selling as a DEALER or INDIVIDUAL",('DEALER','INDIVIDUAL'))

    if s2 == "DEALER":
        p4=0
    elif s2 =="INDIVIDUAL":
        p4=1
    s3 = st.selectbox("VEHICLE TRANSMISSION",('MANUAL','AUTOMATIC'))

    if s3 == "MANUAL":
        p5=0
    elif s3 =="AUTOMATIC":
        p5=1

    p6 = st.slider("How many OWNERS did the vehicle previously had",0,5)

    date_time = datetime.datetime.now()
    
    years = st.number_input("What YEAR was the vehicle purchased",1980,date_time.year)
    p7 = date_time.year - years

    data_new = pd.DataFrame({
    'year': p7,
    'selling_price': p1,
    'km_driven': p2,
    'fuel': p3,
    'seller_type': p4,
    'transmission': p5,
    'owner': p6
}, index=[0])

    if st.button('Predict'):
        pred = model.predict(data_new)
        st.success("VEHICLE SELLING PRICE {} PHP".format(pred[0]))

if __name__ == '__main__':
    main()
    