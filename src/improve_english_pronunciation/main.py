"""Check pronunciation differences between two sentences.
- Input: answer with using text, user's answer with using voice
    - Mac: [Use Voice Control on your Mac - Apple Support](https://support.apple.com/en-us/102225)
- Output: pronunciation differences
"""
from __future__ import annotations

from typing import TYPE_CHECKING

import eng_to_ipa as ipa
import Levenshtein
import streamlit as st

if TYPE_CHECKING:
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

source = st.selectbox("Select source", ["Cambridge", "Weblio"])

col1, col2 = st.columns(2)

def display_input_text(col: DeltaGenerator, title: str, height: int=200) -> tuple[str,str]:
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
        st.write("Sentences :", " ".join([f"[{word}]( https://sentence.yourdictionary.com/search/result?q={word.replace(" ","%20")})" for word in text_lst]))

        return text, ipa.convert(text)

answer, answer_ipa = display_input_text(col1, "Answer")

user_answer, user_ipa = display_input_text(col2, "Your Voice")

# Check pronunciation differences
st.header("Check pronunciation differences")
st.write("Distance(ipa) : ", Levenshtein.distance(answer_ipa, user_ipa))
