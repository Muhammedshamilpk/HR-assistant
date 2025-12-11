# HR-assistant


The TalentScout Hiring Assistant is an AI-powered conversational system built using Python, Streamlit, and Groq Llama 3.1 models.
It assists recruitment teams by collecting essential candidate information and generating technical interview questions tailored to a candidate’s skill set.

This project was developed as part of the AI/ML Intern Assignment.

🚀 Features

✅ 1. Smart Greeting & Purpose Introduction

The chatbot automatically greets the user and briefly explains its role in the hiring workflow.

✅ 2. Candidate Information Collection

The assistant gathers all key candidate details, including:

Full Name

Email Address

Phone Number

Years of Experience

Desired Position

Current Location

Tech Stack (programming languages, frameworks, tools, databases)

✅ 3. Tech Stack–Driven Interview Questions

Based on the declared tech stack, the chatbot generates 3–5 relevant technical questions for each skill.

Example:
If the candidate lists Python and Django, the bot produces questions for both technologies.

✅ 4. Context-Aware Interaction

The chatbot maintains context throughout the conversation, remembering:

What information is already collected

Which details are missing

User responses across turns

✅ 5. Intelligent Fallback Mechanism

When the chatbot cannot interpret an input, it responds politely:

“Sorry, I didn’t understand that. Can you rephrase?”

✅ 6. Graceful Exit Handling

If the user types:

exit, quit, bye, stop, end


The assistant politely ends the conversation.

✅ 7. Simulated Backend Storage

Completed candidate profiles are stored in a local JSON file (candidates_store.json), serving as a simulated database.

📂 Project Structure

talentscout-hiring-assistant/

│

├── app.py                 # Streamlit UI

├── bot.py                 # Chatbot engine & workflow logic

├── prompts.py             # System + generation prompts

├── storage.py             # JSON-based simulated storage

│

├── requirements.txt       # Dependencies

├── README.md              # Documentation

├── .env                   # GROQ_API_KEY (excluded from GitHub)

│

├── assets/                # Optional screenshots

└── utils/                 # Optional helper modules

🧠 Technologies Used

|Component	  |Technology                |
-----------------------------------------
|Frontend UI  |	Streamlit                |

|LLM Provider |	Groq API                 |

|Model Used	  | Llama-3.1–8B-Instant     |

|Language	    | Python                   |

| Storage	    | Local JSON (simulated DB)|

-----------------------------------------

🛠️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/your-username/talentscout-hiring-assistant

cd talentscout-hiring-assistant

2️⃣ Create and activate a virtual environment

python -m venv venv

venv\Scripts\activate        # Windows

source venv/bin/activate     # Mac/Linux

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Add your Groq API Key

Create a file named .env.example and add:

GROQ_API_KEY=your_groq_api_key_here

5️⃣ Run the application

streamlit run app.py

🧩 How to Use the Chatbot

1) Start the conversation

Simply type:

Hi

2) Provide the requested details (step-by-step or together)

Example:

My name is Shamil.

Email: demo@gmail.com

Phone: 1247854552

3 years experience

Backend Developer

Location: Kochi

Tech stack: Python, Django, MySQL

3) The bot confirms the collected details
4) It generates 3–5 questions per technology
5) The conversation ends gracefully
6) You can load saved candidate records by clicking “Load Records”
   
🧠 Prompt Engineering Strategy

🔹 System Prompt

Defines the assistant’s behavior, tone, and boundaries.

🔹 Information Extraction Prompt

Instructs the model to extract structured candidate data in JSON format.

🔹 Technical Question Generation Prompt

Tells the model to produce 3–5 interview questions for each technology.

🔹 Fallback & Exit Handling

Ensures smooth, controlled dialogue flow.

🗂️ Data Privacy & Security

No real personal data is stored

All information is saved only in a local JSON file

API key is stored securely using .env

No cloud-based personal data storage is used
