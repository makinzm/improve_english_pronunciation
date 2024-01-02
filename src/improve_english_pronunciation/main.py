"""Check pronunciation differences between two sentences.
- Input: answer with using text, user's answer with using voice
    - Mac: [Use Voice Control on your Mac - Apple Support](https://support.apple.com/en-us/102225)
- Output: pronunciation differences
"""

import eng_to_ipa as ipa
import Levenshtein
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

description = """
Check pronunciation differences between two sentences.
- Input: answer with using text and user's answer with using voice
    - Mac: [Use Voice Control on your Mac - Apple Support](https://support.apple.com/en-us/102225)
- Output: pronunciation differences

## How to use
1. Input answer with using text.
2. Input user's answer with using voice.
3. Check pronunciation differences.
"""
st.set_page_config(page_title="Improve English Pronunciation", layout="wide")
st.markdown("# Improve English Pronunciation")
with st.expander("See description"):
    st.markdown(description, unsafe_allow_html=True)

source = st.selectbox("Select source", ["Weblio", "Cambridge"])

col1, col2 = st.columns(2)

def display_input_text(col: DeltaGenerator, title: str, height: int=200) -> str:
    """display_input_text with link and ipa"""
    with col:
        st.header(title)
        text = st.text_area(title, height=height)
        text = text.replace("\n", " ")
        text_lst = text.split(" ")
        if source == "Weblio":
            st.write(f"    {" ".join([f"[{word}](https://ejje.weblio.jp/content/{word})" for word in text_lst])}")
        if source == "Cambridge":
            st.write("    "," ".join([f"[{word}](https://dictionary.cambridge.org/dictionary/english/{word})" for word in text_lst]))
        st.write("IPA   :", ipa.convert(text))

        return text

answer = display_input_text(col1, "Answer")

user_answer = display_input_text(col2, "Your Voice")

# Check pronunciation differences
st.header("Check pronunciation differences")
st.write("Distance(text): ", Levenshtein.distance(answer, user_answer))

