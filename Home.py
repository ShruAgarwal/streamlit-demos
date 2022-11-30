import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
    page_title="Fun Streamlit Demos",
    page_icon="🤹‍♀️",)

st.title('👀 Demos for components & fun hacks')

st.markdown("""I'll walk you through the demo for each **component** and the **fun stuff** that I have built so far!
                \nGo ahead and browse available demos in the left-hand side menu 👈""")

def load_lottie_url(url: str):
 r = requests.get(url)
 if r.status_code != 200:
     return None
 return r.json()

animate = "https://assets8.lottiefiles.com/packages/lf20_8CeqKMzpWz.json"
lottie_animate = load_lottie_url(animate)

st.write("")
st_lottie(lottie_animate, key = "demos", width=450, height=380) 