import streamlit as st 
import pandas as pd
from page import Page
#import numpy as np


def settings_params() -> None:
    """
    Set page config, title and headers.

    :return: None
    """
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
    return None


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


def nextpage() -> None: 
    """
    Move to next page of videos.

    :return: None
    """
    st.session_state.page += 1
    return None


def restart(): 
    """
    Return to first page of videos.

    :return: None
    """
    st.session_state.page = 1
    return None


def init(placeholder: st.empty, df: pd.DataFrame) -> bool:
    """
    Initialization elements of veb-site.

    :param placeholder: place for restart button
    :param df: table about first top ten videos (title, category, description, date) 
    :return: status for debugging (True - init, False - not init)
    """
    if "page" not in st.session_state:
        st.session_state.page = 1
        st.session_state.sliders = []
        st.session_state.likes = []
        st.session_state.dislikes = []
        st.session_state.obj = Page(placeholder, df, st.session_state.page)
        st.session_state.model = None
        st.session_state.is_change = [False for i in range(21)]
        return True
    return False


def update(new_df: pd.DataFrame) -> bool:
    """
    Updating elements of veb-site.

    :param new_df: table about new top ten videos (title, category, description, date)
    :return: status for debugging (True - update, False - not update) 
    """
    if st.session_state.is_change[st.session_state.page-1] == True:
        st.session_state.likes = st.session_state.obj.likes
        st.session_state.dislikes = st.session_state.obj.dislikes
        st.session_state.sliders = st.session_state.obj.sliders
        st.session_state.model = None
        st.session_state.obj.change_df(new_df)
        st.session_state.obj.update_values()
        st.session_state.is_change[st.session_state.page-1] = False
        return True
    return False


def show_page() -> None:
    """
    Show page number, title of table and information about video.

    :return: None
    """
    st.session_state.obj.show_number()
    st.session_state.obj.show_titles()
    st.session_state.obj.show_videos()
    st.session_state.is_change[st.session_state.page] = True 
    return None   


def main() -> None:
    """
    Main function of streamlit application.

    :return: None
    """
    settings_params()

    df = change_columns_df(init_df())
    df_1 = change_columns_df(init_df("новый датасет"))

   # button_next = st.button("Next", disabled=(st.session_state.page > 3))

    placeholder = st.empty()

    init(placeholder=placeholder, df=df)

    st.button(label="Next", on_click=nextpage, disabled=(st.session_state.page > 21))

    if st.session_state.page == 1:
        show_page()

    elif st.session_state.page <= 20:
        update(new_df=df_1)
        show_page()

    else:
        with placeholder:
            st.write("This is the end")
            st.button("Restart", on_click=restart)



if __name__ == "__main__":
    main()
