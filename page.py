import streamlit as st 
import pandas as pd
import emoji
#import streamlit_scrollable_textbox as stx


class Page:
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
