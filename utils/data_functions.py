import streamlit as st
import pandas as pd

@st.cache
def loadDataFrames(scrape_url: str) -> [pd.DataFrame]:
    url = scrape_url
    return pd.read_html(url, header = 0)