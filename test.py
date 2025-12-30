import streamlit as st
import requests


url = "https://service.safar724.com/buses/api/bus/route"

params = {
    "Date": '1404-10-08',
    "Origin": 'kermanshah',
    "Destination": 'tehran'
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://safar724.com/"
}

response = requests.get(url, params=params, headers=headers)
data = response.json()

st.write(response.status_code)

