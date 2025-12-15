import streamlit as st
import os
import time
from dotenv import load_dotenv
from src.llm_handler import LLMHandler
from src.utils import is_info_complete, save_candidate_data
from src.prompts import SYSTEM_PROMPT
from langchain.schema import SystemMessage, HumanMessage, AIMessage

# Load environment variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Hiring Mate",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    .reportview-container {
        background: #0e1117;
    }
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
    }
    h1 {
        color: #00d4ff; /* Cyan accent */
        font-family: 'Inter', sans-serif;
    }
    .stButton>button {
        background-color: #00d4ff;
        color: #000000;
        border-radius: 5px;
        border: none;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00b8d9;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {
        "full_name": "Missing",
        "email": "Missing",
        "phone": "Missing",
        "experience": "Missing",
        "position": "Missing",
        "location": "Missing",
        "tech_stack": "Missing"
    }
if "phase" not in st.session_state:
    st.session_state.phase = "GATHERING" # GATHERING, TECHNICAL, ENDED
if "tech_questions" not in st.session_state:
    st.session_state.tech_questions = None

# Sidebar
with st.sidebar:
    st.title("TalentScout 🤖")
    st.write("Specialized Recruitment Assistant")
    
    api_key = st.text_input("Groq API Key", type="password", help="Enter your Groq API key to enable the chatbot.")
    if not api_key:
        api_key = os.getenv("GROQ_API_KEY")
    
    if api_key:
        api_key = api_key.strip()
    
    st.divider()
    st.subheader("Candidate Profile Status")
    
    # Progress Bar
    filled_fields = sum(1 for v in st.session_state.candidate_info.values() if v != "Missing")
    total_fields = len(st.session_state.candidate_info)
    progress = filled_fields / total_fields
    st.progress(progress)
    
    st.write("### Details Collected:")
    for key, value in st.session_state.candidate_info.items():
        status = "✅" if value != "Missing" else "❌"
        st.write(f"{status} **{key.replace('_', ' ').title()}**: {value if value != 'Missing' else ''}")

# Main Chat Interface
st.title("👩‍💻 Hiring Mate")
st.caption("Let's get your profile set up and check your technical skills!")

llm_handler = LLMHandler(api_key=api_key)

# Display Chat History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Initial Greeting
if not st.session_state.messages:
    greeting = "Hello! I'm the Hiring Assistant. I'm here to learn more about your professional background and find the perfect role for you. To get started, could you please tell me your full name?"
    st.session_state.messages.append({"role": "assistant", "content": greeting})
    st.rerun()

# User Input
if prompt := st.chat_input("Type your response here..."):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Process Logic
    if st.session_state.phase == "GATHERING":
        with st.spinner("Analyzing..."):
            # 1. Extract Info
            updated_info = llm_handler.extract_info(
                st.session_state.messages, 
                st.session_state.candidate_info, 
                prompt
            )
            
            # Update state if new info found
            if isinstance(updated_info, dict):
                # Handle potential exit intent from extraction
                if updated_info.get("intent") == "exit":
                    st.session_state.phase = "ENDED"
                    final_msg = "Thank you for your time. We have saved your current details. Good luck!"
                    st.session_state.messages.append({"role": "assistant", "content": final_msg})
                    st.rerun()

                st.session_state.candidate_info.update({
                    k: v for k, v in updated_info.items() 
                    if k in st.session_state.candidate_info and v != "Missing"
                })
            
            # 2. Check Completion
            if is_info_complete(st.session_state.candidate_info):
                st.session_state.phase = "TECHNICAL"
                save_candidate_data(st.session_state.candidate_info)
                
                # Generate Questions
                tech_stack = st.session_state.candidate_info['tech_stack']
                exp = st.session_state.candidate_info['experience']
                questions = llm_handler.generate_tech_questions(tech_stack, exp)
                st.session_state.tech_questions = questions
                
                response_text = f"Thank you! I have all your details. since you are proficient in **{tech_stack}**, let's move to a quick technical screening.\n\nHere are a few questions for you:\n\n{questions}\n\nPlease answer them to the best of your ability."
            else:
                # 3. Generate Next Question (Information Gathering)
                # We construct messages for the LLM to decide what to ask next
                sys_msg_content = SYSTEM_PROMPT.format(
                    phase="Information Gathering",
                    **st.session_state.candidate_info
                )
                
                # Context management: Pass recent history (last 4 messages)
                recent_history = [
                    msg for msg in st.session_state.messages[-4:] 
                    if msg["role"] != "system"
                ]
                lc_messages = [SystemMessage(content=sys_msg_content)]
                for m in recent_history:
                    if m["role"] == "user":
                        lc_messages.append(HumanMessage(content=m["content"]))
                    else:
                        lc_messages.append(AIMessage(content=m["content"]))
                
                response_text = llm_handler.get_response(lc_messages)

    elif st.session_state.phase == "TECHNICAL":
        # Simulating listening to answers and closing
        # In a full app, we would evaluate the answers.
        # For now, we thank them and end.
        response_text = "Thank you for your responses! Your application and technical screening results have been recorded. A recruiter will be in touch with you shortly. Have a great day!"
        st.session_state.phase = "ENDED"

    elif st.session_state.phase == "ENDED":
        response_text = "The conversation has ended. Please refresh to start a new application."

    # Assistant message
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    with st.chat_message("assistant"):
        st.markdown(response_text)
        
    # Force rerun to update sidebar
    st.rerun()
