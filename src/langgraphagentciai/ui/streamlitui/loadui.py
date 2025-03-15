import streamlit as st 
import os 
from datetime import date 
from src.langgraphagentciai.ui.uiconfigfile import Config


from langchain_core.messages import AIMessage, HumanMessage

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config() # Config
        self.user_controls = {}
    
    def initialize_session(self):
        return {
            "cureent_step": "requirements",
            "requirements": "",
            "user_stories": "",
            "po_feedback": "",
            "generated_code": "",
            "review_feedback": "",
            "decision": None
        }

    # def render_requirements(self):
    #     st.markdown("## Requirements Submission")
    #     st.session_state.state["requirements"] = st.text_area(
    #         "Enter your requirements",
    #         height=200,
    #         key="req_input"
    #     )

    #     if st.button("Submit Requirements", key="submit_req"):
    #         st.session_state.state["current_state"] = "generate user stories"
    #         st.session_state.IsSDLC = True

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False

        with st.sidebar:
            # Get options from config
            llm_options =  self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM Selection 
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == "Groq":
                # Model Selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)

                # API Key Input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key", type="password")

                # Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                     st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
                    
            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()

            # self.render_requirements()
        return self.user_controls