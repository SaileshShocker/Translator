from langchain.prompts import PromptTemplate
import os
from properties import *
from langchain.llms import OpenAI
from langchain.chains import LLMChain



def language_translator():
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    llm = OpenAI(temperature=0.7)

    template = '''In an easy way, translate the following sentence '{sentence}' into {target_language}'''
    language_prompt = PromptTemplate(
        input_variables=["sentence", "target_language"],
        template=template,
    )
    
    # Get user input for sentence and target language
    sentence = input("Enter the sentence to translate: ")
    target_language = input("Enter the target language: ")
    print("_________________________________________________")

    # Create the LLMChain object
    translator = LLMChain(llm=llm, prompt=language_prompt)

    # Use the LLMChain object to generate the output
    translated_output = translator({'sentence': sentence, 'target_language': target_language})

    # Print the output in a readable format
    print("Input Sentence:", translated_output['sentence'])
    print("Target Language:", translated_output['target_language'],"\n")
    print("Translated Text:", translated_output['text'].lstrip())  # Remove leading and trailing whitespace
    
# Call the function
language_translator()

