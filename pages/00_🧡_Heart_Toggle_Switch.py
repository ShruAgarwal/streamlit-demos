import streamlit as st
from streamlit_custom_toggle import st_custom_toggle

st.set_page_config(
    page_title="Heart Toggle Switch",
    page_icon="🧡",)

st.title('💜 Heart Toggle Switch')

st.write('A Streamlit custom component to load heart-shaped Toggle Switch widget')

"""
[![Star](https://img.shields.io/github/stars/ShruAgarwal/streamlit-custom-toggle.svg?logo=github&style=social)](https://github.com/ShruAgarwal/streamlit-custom-toggle)
[![PyPI](https://img.shields.io/pypi/v/streamlit-custom-toggle?color=brightgreen)](https://pypi.org/project/streamlit-custom-toggle/0.1.1/)
"""

st.header('Installation')
st.code("pip install streamlit-custom-toggle")

st.header('Usage')
st.caption('Input code')
st.markdown("""
```python
import streamlit as st
from streamlit_custom_toggle import st_custom_toggle

st.subheader('Music Choices 🎵')
col1, col2, col3 = st.columns(3, gap="small")

with col1:
    # Disabled toggle switch
    calm = st_custom_toggle('Calm', active_track_fill="#EAE4E4", active_thumb_color="#EAE4E4", value="true", key="toggle1")

with col2:
    fun = st_custom_toggle('Fun', active_track_fill="#57FD6E", active_thumb_color="#EAE4E4", key="toggle2")

with col3:
    music_toggle = st_custom_toggle('Rock', active_track_fill="#FF5733", active_thumb_color="#900C3F", key="toggle3")
    music = st.radio(
    "Select your favorite artist",
    ('The Beatles', 'AC/DC', 'Pink Floyd', 'Elvis Presley', 'MÃ¥neskin'), disabled=music_toggle)
    st.markdown(f"You choose {music}")

# Checking the toggle state
st.code(f"Calm = {calm}, Fun = {fun}, Rock = {music_toggle}")
```""")

st.write("")
st.caption('Output')
def toggle():
    st.subheader('Music Choices 🎵')
    
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        # Disabled toggle switch
        calm = st_custom_toggle('Calm', active_track_fill="#EAE4E4", active_thumb_color="#EAE4E4", value="true", key="toggle1")

    with col2:
        fun = st_custom_toggle('Fun', active_track_fill="#57FD6E", active_thumb_color="#EAE4E4", key="toggle2")

    with col3:
        music_toggle = st_custom_toggle('Rock', active_track_fill="#FF5733", active_thumb_color="#900C3F", key="toggle3")
        music = st.radio(
            "Select your favorite artist",
            ('The Beatles', 'AC/DC', 'Pink Floyd', 'Elvis Presley', 'MÃ¥neskin'), disabled=music_toggle)
        st.markdown(f"You choose {music}")
        
    # Checking the toggle state
    st.code(f"Calm = {calm}, Fun = {fun}, Rock = {music_toggle}")

toggle()
