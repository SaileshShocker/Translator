# app.py
from langchain.prompts import PromptTemplate
import os
from properties import *
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import streamlit as st

# Adding styles to make text bold
st.markdown("""
<style>
    .main {
        background-image: url('https://github.com/SaileshShocker/Images-for-projects/blob/main/Background.png');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .bold-text {
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# for background image
st.markdown('<div class="main">', unsafe_allow_html=True)

def language_translator():
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    llm = OpenAI(temperature=0.7)

    template = '''In an easy way, translate the following sentence '{sentence}' into {target_language}'''
    language_prompt = PromptTemplate(
        input_variables=["sentence", "target_language"],
        template=template,
    )

    # Get user input for sentence and target language
    sentence = st.text_input("**Enter the sentence to translate:**")
    target_language = st.text_input("**Enter the target language:**")

    # Create the LLMChain object
    translator = LLMChain(llm=llm, prompt=language_prompt)

    # Check if the "Translate" button is clicked
    if st.button("Translate"):
        # Use the LLMChain object to generate the output
        translated_output = translator({'sentence': sentence, 'target_language': target_language})

        # Display the output in the app with bold text
        st.markdown("**Input Sentence:** {}".format(translated_output['sentence']), unsafe_allow_html=True)
        st.markdown("**Target Language:** {}".format(translated_output['target_language']), unsafe_allow_html=True)
        st.markdown("**Translated Text:** {}".format(translated_output['text'].lstrip()), unsafe_allow_html=True)

# Streamlit app
def main():
    
    # Hide Streamlit's default footer
    st.markdown('<style>footer{visibility:hidden;}</style>',unsafe_allow_html=True)

    st.title("Language Translator App")
    language_translator()

if __name__ == "__main__":
    main()
