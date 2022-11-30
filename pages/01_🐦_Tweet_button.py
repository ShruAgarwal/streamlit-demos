import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Tweet Button",
    page_icon="🐦",)

st.title('🐦Twitter Share Button')
st.write("")
st.write('An easy to embed share button that can directly tweet about Streamlit apps on Twitter!')

st.write("")
st.header('Usage')
st.caption('Input code')

image = Image.open('pages/button.png')
st.write("")
st.image(image)
st.markdown('You can copy the source code of this page on GitHub.')

st.write("")
st.caption('Output')

def tweet_button(tag: str, 
                 link: str, 
                text: str, 
                user: str):
  tweet = f"""
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.css">
  <script src="https://cdn.jsdelivr.net/npm/semantic-ui@2.4.2/dist/semantic.min.js"></script>
  <a href="https://twitter.com/intent/tweet?url={link}&text={text}&via={user}&hashtags={tag}">
  <button class="ui twitter button large ui button">
   <i class="twitter icon"></i>
    Tweet
  </button></a>
    """
  st.markdown(tweet, unsafe_allow_html=True)

st.write("")
tweet_button(tag='streamlit, share', 
             link='https://30days.streamlit.app/', 
             text='Streamlit share button', 
             user='streamlit')

st.write("")
st.write('📌 NOTE: This button only works if you have a valid Twitter account.')