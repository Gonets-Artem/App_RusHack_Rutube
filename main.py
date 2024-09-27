import streamlit as st 
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
import sys
import streamlit_scrollable_textbox as stx
#from catboost import CatBoostRegressor
#from numpy.lib.stride_tricks import sliding_window_view


def settings():
    # Настройка заголовка и размеров активной области
    st.set_page_config(page_title="Обратная связь для новых пользователей", layout="wide")
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
    st.title("Веб-приложение решения проблемы :blue['холодного старта'] у новых пользователей")
    st.header("")


def init_df():
    df = pd.DataFrame(data={
        'video_id': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'title': ['Название 1', 'Название 2', 'Название 3', 'Название 4', 'Название 5', 'Название 6', 'Название 7', 'Название 8', 'Название 9', 'Название 10'],
        'category_id': ['Мультфильм', 'Мультфильм', 'Хобби', 'Равлечение', 'Юмор', 'Юмор', 'Наука', 'Здоровье', 'Красота', 'Аудиокниги'],
        'description': ['', 'Описание', 'Описание 2', 'рурурруруруруурурруурурруруурурруруруруруурурурур', '', '', '', '', '', ''],
        'v_pub_datetime': ['2024-06-15 22:58:03', '2024-06-15 22:58:03', '2024-06-15 22:58:03', '2024-06-15 22:58:03', '2024-06-15 22:58:03', '2024-06-15 22:58:03', '2024-06-15 22:58:03', '2024-06-15 22:58:03', '2024-06-15 22:58:03', '2024-06-15 22:58:03']
    })
    return df


def change_columns_df(df):
    return df.rename(columns={
        'video_id': 'ID видео', 
        'title': 'Название',
        'category_id': 'Категория',
        'description': 'Описание',
        'v_pub_datetime': 'Дата публикации'
    })


def main():
    settings()
    
    st.subheader("_Первичный список видео_")
    st.subheader("")

    df = change_columns_df(init_df())
    likes = []
    dislikes = []

    col1, col2, col3, col4, col5, col6 = st.columns(6, gap='medium')
    with col1:
        #st.markdown("##### **_" + df.columns[0] + "_**")
        st.write(r"$\textsf{\normalsize ID видео}$")
        for i in range(df.shape[0]):
            with st.container(height=50):
                st.write(df.iloc[i, 1])
                #stx.scrollableTextbox(df.iloc[i, 0], height=50, key=0*df.shape[0]+i)

    with col2:
        #st.subheader(df.columns[1])
        st.write(r"$\textsf{\normalsize Название}$")
        #st.markdown("##### **_" + df.columns[1] + "_**")
        for i in range(df.shape[0]):
            with st.container(height=50):
                st.write(df.iloc[i, 1])
                #stx.scrollableTextbox(df.iloc[i, 1], height=50, key=1*df.shape[0]+i)
    
    with col3:
        st.write(r"$\textsf{\normalsize Категория}$")
        #st.markdown("##### **_" + df.columns[2] + "_**")
        for i in range(df.shape[0]):
            with st.container(height=50):
                st.write(df.iloc[i, 2])
                #stx.scrollableTextbox(df.iloc[i, 2], height=50, key=2*df.shape[0]+i)

    with col4:
        st.write(r"$\textsf{\normalsize Описание}$")
        #st.markdown("##### **_" + df.columns[3] + "_**")
        for i in range(df.shape[0]):
            with st.container(height=50):
                st.write(df.iloc[i, 3])
                #stx.scrollableTextbox(df.iloc[i, 3], height=50, key=3*df.shape[0]+i)

    with col5:
        st.write(r"$\textsf{\normalsize Дата публикации}$")
        #st.markdown("##### **_" + df.columns[4] + "_**")
        for i in range(df.shape[0]):
            with st.container(height=50):
                st.write(df.iloc[i, 4])
                #stx.scrollableTextbox(df.iloc[i, 4], height=50, key=4*df.shape[0]+i)

    with col6:
        st.write(r"$\textsf{\normalsize Оценка}$")
        col6_1, col6_2 = st.columns(2, gap='medium')
        
        with col6_1:
            for i in range(df.shape[0]):
                with st.container(height=50):
                    likes.append(st.checkbox(label="Like", key=5*df.shape[0]+i))
                    #dislikes.append(st.checkbox(label="Dislike", key=i+1))

        with col6_2:
            for i in range(df.shape[0]):
                with st.container(height=50):
                    dislikes.append(st.checkbox(label="Dislike", key=6*df.shape[0]+i))
                    #likes.append(st.checkbox(label="Like", key=i))
    #st.write(df)


if __name__ == "__main__":
    main()
