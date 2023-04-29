from st_on_hover_tabs import on_hover_tabs
import time
import streamlit as st
import pickle
import streamlit.components.v1 as components
from bokeh.models.widgets import Div # version 2.4.1




st.set_page_config(page_title='The Movie Recommender', page_icon = 'favicon.png', layout = 'wide', initial_sidebar_state = 'auto')

def title(url):
    st.markdown(f'<h3 style=" font-family: cursive; text-align: center;background-color:rgb(54 130 117) ; color:rgb(177 191 109);height:81px;font-weight: 900;font-size:49px;border-radius:5px;">{url}</h3>', unsafe_allow_html=True)


st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


from st_on_hover_tabs import on_hover_tabs
import streamlit as st

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
import streamlit as st
import requests
with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'About the Project', 'Connect with me', 'Source Code', 'The Balloon show'], 
                         iconName=['home', 'info', 'hub','code', 'celebration'], default_choice=0,
                         styles = {'navtab': {'background-color':'#111',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': '#96be25',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}},
                             key="1")



def fetch_poster(movie_id):
    api_response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=63647f967ad9c913ceb8edfe45ced818&language=en-US'.format(movie_id))
    data= api_response.json()
    return "https://image.tmdb.org/t/p/w200/" + str(data['poster_path'])

def copywrite_picsum(text):
    st.markdown(f'<a href="https://picsum.photos/" target=_blank, style="display: flex;flex-direction: column;justify-content: center;text-align: center; text-decoration: none; color: olive; font-weight:700">{text}</a>', unsafe_allow_html=True)

def balloon_emoji(text):
    st.markdown(f'<p style="display: flex;flex-direction: column;justify-content: center;text-align: center; text-decoration: none; font-weight:400">{text}</p>', unsafe_allow_html=True)

if tabs =='Home':
    title("Movie Recommendation System")
    st.write('\n')
    def recommend_movies(movie_name):
        this_movie_index= movies_data[movies_data['title']==movie_name].index[0] #fetchs the position(index) of the given movie
        CS_Movie= cosine_similarities[this_movie_index] # its a 1-D vector that contains the similarities between the given movie with all the movies present in dataframe
        CS_Movie= list(enumerate(CS_Movie)) # This is to make a tuple of similarities with the index of the movie as in the next step when we ll sort the vector hence we want to retain the index so that we can get the details of the movie
        CS_Movie.sort(reverse=True, key=lambda item: item[1]) # reverse sorting on the basis of similarity score to get higest similarities at top
        temp_tuples=CS_Movie[1:6] # tuple to store the first five similar movies
        movie_indexes=[]
        for item in temp_tuples:
            movie_indexes.append(item[0]) # getting the index of each movie
        recommended_movies=[]
        recommend_movies_posters=[]
        for indx in movie_indexes:
            recommended_movies.append(movies_data['title'][indx]) # appending the title of each movie
            # fetching poster from tmdb api
            movie_id=movies_data['movie_id'][indx]
            recommend_movies_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommend_movies_posters
    
    movies_data = pickle.load(open('movies_data.pkl', 'rb'))
    movies_name_data = movies_data['title'].values

    cosine_similarities= pickle.load(open('cosine_similarities.pkl', 'rb'))

    selected_movie = st.selectbox(
        'Search for Movies 🎬',
        movies_name_data)
    
    st.write('You selected:', selected_movie)
    if st.button('Get Recommendations'):
        with st.spinner('Getting Recommendations...Relax a bit'):
            time.sleep(2)
        st.success('Enjoy!')

        st.balloons()
        
        recommended_movies, recommended_posters= recommend_movies(selected_movie)
        m1,m2,m3,m4,m5 = st.columns(5)
        with m1:
            st.write('\n')
            st.write(recommended_movies[0])
            st.write('\n')
            st.image(recommended_posters[0])

        with m2:
            st.write('\n')
            st.write(recommended_movies[1])
            st.write('\n')
            st.image(recommended_posters[1])

        with m3:
            st.write('\n')
            st.write(recommended_movies[2])
            st.write('\n')
            st.image(recommended_posters[2])

        with m4:
            st.write('\n')
            st.write(recommended_movies[3])
            st.write('\n')
            st.image(recommended_posters[3])

        with m5:
            st.write('\n')
            st.write(recommended_movies[4])
            st.write('\n')
            st.image(recommended_posters[4])


elif tabs == 'About the Project':
    title("Movie Recommendation System")
    st.write('\n')
    st.balloons()
    st.write("**About the Project 💫**")
    st.write('\n\n')
    st.write("""
        Welcome!\n
    A Recommendation system is a subclass of information filtering system that seeks to predict the *preference* a user would give to an item.\n\n
    ***Value of Recommendation:***\n
    \tNetflix: 2/3 of movies watched are recommended\n
    \tGoogle news: recommendation generates 38% clickthrough\n
    \tAmazon: 35% sales from recommendation\n
    
    ***Typically, Machine Learning Algorithms are fit into 3 categories of the Recommendation System.***\n
    \tContent-Based Recommendation Systems\n
    \tCollaborative Filtering Recommendation Systems\n
    \tHybrid Recommendation System\n
    This Project is a *Content-Based Recommendation System*, which means the system suggest similar items based on a particular item. This system uses item metadata, such as Genre, Director, overview, Cast, various keywords, etc. for movies, to make the recommendations. The general idea behind these recommendation systems is that if a person likes a particular item, he or she will also like an item that is similar to it.\n
    In this Project, the dataset is taken from **TMDB**. The App is made using the Python's Streamlit Library. Complete Code as well as the detailed description is available in the project's GitHub repository. There's always an open room for corrections and advices. Happy Coding!\n
    For me, the best part of this project is **The Balloon Show**😄\n
    Special credits to **Faisal Jawed** for the amazing Raining and Lightning effect Snippet.\n
    **Note:** Some missing posters are result of the *NULL* Value in *Poster_Path* provided by the **TMDB API**.\n

    Made with ❤ by **Sanket**

    """)

elif tabs == 'Connect with me':
    title("Movie Recommendation System")
    st.write('\n')
    st.balloons()
    st.write("**Connect With Me 📧**")
    if st.button('GitHub'):
        js = "window.open('https://github.com/imsanketsingh')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
    if st.button('LinkTree'):
        js = "window.open('https://www.linktree.com/imsanketsingh/')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
    if st.button('LinkedIn'):
        js = "window.open('https://www.linkedin.com/in/sanket-kumar-singh-b698191b8/')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

elif tabs == 'Source Code':
    title("Movie Recommendation System")
    st.write('\n')
    st.balloons()
    st.write("**Source Code ©**")
    if st.button('GitHub'):
        js = "window.open('https://github.com/imsanketsingh/Movie-Recommendation-System')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
elif tabs == 'The Balloon show':
    balloon_emoji('😊🤗😇')
    HtmlFile = open("picsum_component.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    st.components.v1.html(source_code, width=1280, height=720,scrolling=False)
    copywrite_picsum('© Picsum')
    for i in range(1):
        time.sleep(1)
    for i in range(100):
        time.sleep(2)
        st.balloons()


