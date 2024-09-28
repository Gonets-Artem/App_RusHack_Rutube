import streamlit as st 
import pandas as pd
from page import Page
#import numpy as np


def settings_params():
    # Настройка заголовка и размеров активной области
    st.set_page_config(page_title="Обратная связь для новых пользователей RuTube", layout="wide")
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
    st.title("Решение проблемы :blue['холодного старта'] у новых пользователей")
    st.header("")
    st.subheader("Пожалуйста, оцените нижепредложенные видео")
    st.subheader("")


def init_df(new=""):
    df = pd.DataFrame(data={
        'video_id': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
        'title': [f'Название 1{new}', 'Название 2', 'Название 3', 'Название 4', 'Название 5', 'Название 6', 'Название 7', 'Название 8', 'Название 9', 'Название 10'],
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


def nextpage(): 
    st.session_state.page += 1


def restart(): 
    st.session_state.page = 1


def start(placeholder, df):
    if "page" not in st.session_state:
        st.session_state.page_elem = Page(placeholder, df, 1)
        st.session_state.sliders = []
        st.session_state.likes = []
        st.session_state.dislikes = []
        st.session_state.model = None
        st.session_state.page = 1
        st.session_state.is_change = [False for i in range(21)]


def reboot(new_df):
    if st.session_state.is_change[st.session_state.page-1] == True:
        st.session_state.likes = st.session_state.page_elem.likes
        st.session_state.dislikes = st.session_state.page_elem.dislikes
        st.session_state.sliders = st.session_state.page_elem.sliders
        st.session_state.model = None
        st.session_state.page_elem.change_df(new_df)
        st.session_state.page_elem.update_values()
        st.session_state.is_change[st.session_state.page-1] = False


def show_page():
    st.session_state.page_elem.show_number()
    st.session_state.page_elem.show_titles()
    st.session_state.page_elem.show_videos()
    st.session_state.is_change[st.session_state.page] = True    


def main():
    settings_params()

    df = change_columns_df(init_df())
    df_1 = change_columns_df(init_df("новый датасет"))

   # button_next = st.button("Next", disabled=(st.session_state.page > 3))

    placeholder = st.empty()
    
    start(placeholder, df)

    st.button("Next", on_click=nextpage, disabled=(st.session_state.page > 21))

    if st.session_state.page == 1:
        show_page()

    elif st.session_state.page <= 20:
        reboot(df_1)
        show_page()

    else:
        with placeholder:
            st.write("This is the end")
            st.button("Restart",on_click=restart)


if __name__ == "__main__":
    main()
