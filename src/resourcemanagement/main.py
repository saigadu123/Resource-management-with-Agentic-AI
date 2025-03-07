import streamlit as st
import json
from src.resourcemanagement.ui.streamlitui.loadui import LoadStreamlitUI
from src.resourcemanagement.LLMS.groqllm import GroqLLM

def load_resourcemanagement_app():

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    
    if not user_input:
        st.error("Error:Failed to load user input from UI")

    #Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")

     # Initializing the LLM
    if user_message:
        
        obj_llm_config = GroqLLM(user_controls_input=user_input)
        model = obj_llm_config.get_llm_model()

        if not model:
            st.error("Error: LLM model could not be initialized.")
            return 
        
        usecase = user_input.get("selected_usecase")
        if not usecase:
            st.error("Error: Usecase not selected.")
            return

    

