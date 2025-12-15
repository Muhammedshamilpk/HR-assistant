import os
import json
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain.prompts import PromptTemplate

class LLMHandler:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        if self.api_key:
            self.llm = ChatGroq(
                groq_api_key=self.api_key, 
                model_name="llama-3.3-70b-versatile", 
                temperature=0.7
            )
        else:
            self.llm = None

    def get_response(self, messages):
        if not self.llm:
            return "Error: LLM API Key not found. Please configure it in the sidebar."
        try:
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            import traceback
            traceback.print_exc()
            return f"Error communicating with LLM: {str(e)}"

    def extract_info(self, history, current_info, user_input):
        """
        Uses LLM to extract info from the conversation.
        """
        if not self.llm:
            return current_info
        
        # We simplify strictly for extraction to avoid context bloat, 
        # but passing some history helps if user refers to previous turn.
        # For this assignment, we'll try a direct extraction prompt.
        
        from src.prompts import ANALYSIS_SYSTEM_PROMPT
        
        prompt = ANALYSIS_SYSTEM_PROMPT.format(
            current_info=json.dumps(current_info, indent=2),
            user_input=user_input
        )
        
        messages = [
            SystemMessage(content=prompt),
            HumanMessage(content=user_input)
        ]
        
        try:
            response = self.llm.invoke(messages)
            content = response.content
            # Attempt to parse JSON
            # Sometimes LLM adds markdown backticks or extra text, clean them with regex
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                updated_info = json.loads(json_str)
                return updated_info
            else:
                # If no JSON found, return current info
                return current_info
        except Exception as e:
            print(f"Extraction error: {e}")
            return current_info

    def generate_tech_questions(self, tech_stack, experience):
        if not self.llm:
            return ["Error: No API Key"]
            
        from src.prompts import TECH_QUESTION_PROMPT
        prompt = TECH_QUESTION_PROMPT.format(tech_stack=tech_stack, experience=experience)
        
        messages = [HumanMessage(content=prompt)]
        
        try:
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            return f"Error generating questions: {str(e)}"
