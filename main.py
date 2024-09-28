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
    st.subheader("_Cписок видео_")
    st.subheader("")


def init_df(new=""):
    df = pd.DataFrame(data={
        'video_id': [f'1{new}', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
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


class Page():
    def __init__(self, placeholder, df):
        self.placeholder = placeholder
        self.df = df
        self.sliders = []
        self.likes = []
        self.dislikes = []
        self.show_number()
        self.show_titles()
        self.show_videos()


    def show_number(self):
        with self.placeholder.container():
            st.metric("Page: ", value=st.session_state.page)


    def show_titles(self):
        with self.placeholder.container(height=50, border=False):
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
        with self.placeholder.container():
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
                #st.write(r"$\textsf{\normalsize Категория}$")
                #st.markdown("##### **_" + df.columns[2] + "_**")
                for i in range(self.df.shape[0]):
                    with st.container(height=100):
                        st.write(self.df.iloc[i, 2])
                        #stx.scrollableTextbox(df.iloc[i, 2], height=50, key=2*df.shape[0]+i)

            with col4:
                #st.write(r"$\textsf{\normalsize Описание}$")
                #st.markdown("##### **_" + df.columns[3] + "_**")
                for i in range(self.df.shape[0]):
                    with st.container(height=100):
                        st.write(self.df.iloc[i, 3])
                        #stx.scrollableTextbox(df.iloc[i, 3], height=50, key=3*df.shape[0]+i)

            with col5:
                #st.write(r"$\textsf{\normalsize Дата публикации}$")
                #st.markdown("##### **_" + df.columns[4] + "_**")
                for i in range(self.df.shape[0]):
                    with st.container(height=100):
                        st.write(self.df.iloc[i, 4])
                        #stx.scrollableTextbox(df.iloc[i, 4], height=50, key=4*df.shape[0]+i)

            with col6:
                #st.write(r"$\textsf{\normalsize Оценка}$")
                col6_1, col6_2 = st.columns(2, gap='small')

                with col6_1:
                    for i in range(self.df.shape[0]):
                        with st.container(height=100):
                            self.sliders.append(st.slider(label="", min_value=0, max_value=100, value=0, key=5*self.df.shape[0]+i))

                with col6_2:
                    for i in range(self.df.shape[0]):
                        with st.container(height=100):
                            self.likes.append(st.checkbox(label="Like", key=6*self.df.shape[0]+i))
                            self.dislikes.append(st.checkbox(label="Dislike", key=7*self.df.shape[0]+i))
                            #dislikes.append(st.checkbox(label="Dislike", key=i+1))

                #with col6_2:
                #    for i in range(df.shape[0]):
                #        with st.container(height=50):
                #            dislikes.append(st.checkbox(label="Dislike", key=6*df.shape[0]+i))
                            #likes.append(st.checkbox(label="Like", key=i))        


def nextpage(): 
    st.session_state.page += 1
    
def restart(): 
    st.session_state.page = 0


def main():
    settings()

    df = change_columns_df(init_df())
    df_1 = change_columns_df(init_df("новый датасет"))
    
    sliders = []
    likes = []
    dislikes = []

    if "page" not in st.session_state:
        st.session_state.page = 0

    placeholder = st.empty()
    st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 2))

    if st.session_state.page == 0:
        page = Page(placeholder, df)

    if st.session_state.page == 1:
        page = Page(placeholder, df_1)

    if st.session_state.page == 2:
        page = Page(placeholder, df)

        # Replace the placeholder with some text:
        #page.show_titles()

    # elif st.session_state.page == 2:
    #     # Replace the text with a chart:
    #     page.change_df(df_1)
    #     page.show_videos()
    #     #page.show_titles()

    else:
        with placeholder:
            st.write("This is the end")
            st.button("Restart",on_click=restart)
    
    #page = Page(df)
    #page.show_titles()

    # first = st.container(height=50, border=False)
    # with first:
    #     #col1, col2, col3, col4, col5, col6 = st.columns(6, gap="large")
    #     col2, col3, col4, col5, col6 = st.columns(5, gap="large")
    #     # with col1:
    #     #     st.write(r"$\textsf{\normalsize ID видео}$")
    #     with col2:
    #         st.write(r"$\textsf{\normalsize Название}$")
    #     with col3:
    #         st.write(r"$\textsf{\normalsize Категория}$")
    #     with col4:
    #         st.write(r"$\textsf{\normalsize Описание}$")
    #     with col5:
    #         st.write(r"$\textsf{\normalsize Дата публикации}$")
    #     with col6:
    #         st.write(r"$\textsf{\normalsize Процент просмотра и оценка}$")
    #         # col6_1, col6_2 = st.columns(2, gap="medium")
    #         # with col6_1:
                
    #         # with col6_2:
    #         #     st.write(r"$\textsf{\small Оценка}$")


    #col1, col2, col3, col4, col5, col6 = st.columns(6, gap='large')
    # col2, col3, col4, col5, col6 = st.columns(5, gap='large')
    # # with col1:
    # #     for i in range(df.shape[0]):
    # #         with st.container(height=100):
    # #             st.write(df.iloc[i, 1])

    # with col2:
    #     #st.subheader(df.columns[1])
    #     #st.write(r"$\textsf{\normalsize Название}$")
    #     #st.markdown("##### **_" + df.columns[1] + "_**")
    #     for i in range(df.shape[0]):
    #         with st.container(height=100):
    #             st.write(df.iloc[i, 1])
    #             #stx.scrollableTextbox(df.iloc[i, 1], height=50, key=1*df.shape[0]+i)
        
    # with col3:
    #     #st.write(r"$\textsf{\normalsize Категория}$")
    #     #st.markdown("##### **_" + df.columns[2] + "_**")
    #     for i in range(df.shape[0]):
    #         with st.container(height=100):
    #             st.write(df.iloc[i, 2])
    #             #stx.scrollableTextbox(df.iloc[i, 2], height=50, key=2*df.shape[0]+i)

    # with col4:
    #     #st.write(r"$\textsf{\normalsize Описание}$")
    #     #st.markdown("##### **_" + df.columns[3] + "_**")
    #     for i in range(df.shape[0]):
    #         with st.container(height=100):
    #             st.write(df.iloc[i, 3])
    #             #stx.scrollableTextbox(df.iloc[i, 3], height=50, key=3*df.shape[0]+i)

    # with col5:
    #     #st.write(r"$\textsf{\normalsize Дата публикации}$")
    #     #st.markdown("##### **_" + df.columns[4] + "_**")
    #     for i in range(df.shape[0]):
    #         with st.container(height=100):
    #             st.write(df.iloc[i, 4])
    #             #stx.scrollableTextbox(df.iloc[i, 4], height=50, key=4*df.shape[0]+i)

    # with col6:
    #     #st.write(r"$\textsf{\normalsize Оценка}$")
    #     col6_1, col6_2 = st.columns(2, gap='small')

    #     with col6_1:
    #         for i in range(df.shape[0]):
    #             with st.container(height=100):
    #                 sliders.append(st.slider(label="", min_value=0, max_value=100, value=0, key=5*df.shape[0]+i))

    #     with col6_2:
    #         for i in range(df.shape[0]):
    #             with st.container(height=100):
    #                 likes.append(st.checkbox(label="Like", key=6*df.shape[0]+i))
    #                 dislikes.append(st.checkbox(label="Dislike", key=7*df.shape[0]+i))
    #                 #dislikes.append(st.checkbox(label="Dislike", key=i+1))

    #     #with col6_2:
    #     #    for i in range(df.shape[0]):
    #     #        with st.container(height=50):
    #     #            dislikes.append(st.checkbox(label="Dislike", key=6*df.shape[0]+i))
    #                 #likes.append(st.checkbox(label="Like", key=i))


if __name__ == "__main__":
    main()
