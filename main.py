import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from catboost import CatBoostRegressor
from numpy.lib.stride_tricks import sliding_window_view


def settings():
    # Настройка заголовка и размеров активной области
    st.set_page_config(page_title="Серверок", layout="wide")
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
            width: 400px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
            width: 400px;
            margin-left: -400px;
        }
        """,
        unsafe_allow_html=True,
    )
    st.title("Веб-сервис холодного старта")


def main():
    settings()

    # Загрузка подготовленного файла и вывод датасета
    st.header("Источник данных")

    uploaded_file_1 = st.file_uploader("Выберите файл формата .xlsx для загрузки в веб-сервис", type="xlsx", key='123')
    if uploaded_file_1 is not None:
        df_input = pd.read_excel(uploaded_file_1, index_col=0)


if __name__ == "__main__":
    main()