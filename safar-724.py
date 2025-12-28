import streamlit as st
from ps752 import SearcherBus

st.image('buses.png')

st.title('🚐 SAFAR 724 🚌')

com1 , com2 = st.columns(2)
origin = com1.selectbox('enter origin 🗺️ ' , ('tehran' , 'kermanshah'))

com3 , com4 = st.columns(2)
destination = com3.selectbox('enter destination 🗺️ ' , ('tehran' , 'kermanshah'))

' now choice which datd you want'

com5 , com6 = st.columns(2)
com5 = st.selectbox('select the day 📅' , ( '01' , '02' , '03' , '04' , '05' , '06' , '07' , '08' , '09' , '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19' , '20' , '21' , '22' , '23' , '24' , '25' ,'26' , '27' , '28' , '29' , '30' , '31') )

com7 , com8 = st.columns(2)
com7 = st.selectbox('select the month 📅' , ( '01' , '02' , '03' , '04' , '05' , '06' , '07' , '08' , '09' , '10' , '11' , '12' ) )

date = f'1404-{com7}-{com5}'
service = SearcherBus( origin , destination , date )
result = service.print_services()
st.subheader("🎫 نتایج جستجو")
st.markdown(f"```\n{result}```")