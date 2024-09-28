import streamlit as st 
import pandas as pd
#import numpy as np
import sys
import streamlit_scrollable_textbox as stx
import emoji


def settings():
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


class Page():
    def __init__(self, placeholder, df, page):
        self.placeholder = placeholder
        self.df = df
        self.page = page
        self.sliders = []
        self.likes = []
        self.dislikes = []


    def change_df(self, new_df):
        self.df = new_df


    def update_values(self):
        self.page += 1
        self.sliders = []
        self.likes = []
        self.dislikes = []


    def show_number(self):
        with st.container():
            st.metric(f"Page: ", value=f"{st.session_state.page}/20")


    def show_titles(self):
        with st.container(height=50, border=False):
            #col1, col2, col3, col4, col5, col6 = st.columns(6, gap="large")
            col2, col3, col4, col5, col6 = st.columns(5, gap="large")
            # with col1:
            #     st.write(r"$\textsf{\normalsize ID видео}$")
            with col2:
                st.write(r"$\textsf{\normalsize Название}$")
            with col3:
                st.write(r"$\textsf{\normalsize Категория}$")
            with col4:
                st.write(r"$\textsf{\normalsize Описание}$")
            with col5:
                st.write(r"$\textsf{\normalsize Дата публикации}$")
            with col6:
                st.write(r"$\textsf{\normalsize Процент просмотра и оценка}$")
                # col6_1, col6_2 = st.columns(2, gap="medium")
                # with col6_1:
                    
                # with col6_2:
                #     st.write(r"$\textsf{\small Оценка}$")


    def show_videos(self):
        with st.container():
            col2, col3, col4, col5, col6 = st.columns(5, gap='large')
            # with col1:
            #     for i in range(df.shape[0]):
            #         with st.container(height=100):
            #             st.write(df.iloc[i, 1])

            with col2:
                #st.subheader(df.columns[1])
                #st.write(r"$\textsf{\normalsize Название}$")
                #st.markdown("##### **_" + df.columns[1] + "_**")
                for i in range(self.df.shape[0]):
                    with st.container(height=100):
                        st.write(self.df.iloc[i, 1])
                        #stx.scrollableTextbox(df.iloc[i, 1], height=50, key=1*df.shape[0]+i)
                
            with col3:
                for i in range(self.df.shape[0]):
                    with st.container(height=100):
                        st.write(self.df.iloc[i, 2])

            with col4:
                for i in range(self.df.shape[0]):
                    with st.container(height=100):
                        st.write(self.df.iloc[i, 3])

            with col5:
                for i in range(self.df.shape[0]):
                    with st.container(height=100):
                        st.write(self.df.iloc[i, 4])

            with col6:
                col6_1, col6_2 = st.columns(2, gap='small')

                with col6_1:
                    for i in range(self.df.shape[0]):
                        with st.container(height=100):
                            self.sliders.append(st.slider(label="", min_value=0, max_value=100, value=0, key=self.page*100 + self.df.shape[0]+i))

                with col6_2:
                    for i in range(self.df.shape[0]):
                        with st.container(height=100):
                            self.likes.append(st.checkbox(label=emoji.emojize("L :thumbs_up:"), key=self.page*100 + 2*self.df.shape[0]+i))
                            self.dislikes.append(st.checkbox(label=emoji.emojize("D :thumbs_down:"), key=self.page*100 + 3*self.df.shape[0]+i))     


def nextpage(): 
    st.session_state.page += 1


def restart(): 
    st.session_state.page = 1


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
    settings()

    df = change_columns_df(init_df())
    df_1 = change_columns_df(init_df("новый датасет"))
    placeholder = st.empty()

    if "page" not in st.session_state:
        st.session_state.page_elem = Page(placeholder, df, 1)
        st.session_state.sliders = []
        st.session_state.likes = []
        st.session_state.dislikes = []
        st.session_state.model = None
        st.session_state.page = 1
        st.session_state.is_change = [False for i in range(21)]

   # button_next = st.button("Next", disabled=(st.session_state.page > 3))

    st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 21))

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
