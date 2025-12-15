<div align="center">

# 🤖 TalentScout Hiring Assistant

### AI-Powered Recruitment Automation

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-00D4AA?style=for-the-badge)](https://www.langchain.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**An intelligent chatbot that automates candidate screening and generates personalized technical questions based on their tech stack.**

[Quick Start](#-quick-start) • [Features](#-features) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [How It Works](#-how-it-works)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**TalentScout** streamlines your hiring process by automating initial candidate screening. The AI chatbot:

- 💬 Conducts natural conversations with candidates
- 📝 Collects essential information (name, email, experience, tech stack, etc.)
- 🧠 Generates custom technical questions based on their skills
- 💾 Saves candidate data automatically
- ⏱️ Reduces screening time by 70%

---

## ✨ Features

### 🔍 Smart Information Gathering
- Automatically collects candidate details through conversation
- Validates email and phone number formats
- Real-time progress tracking

### 🧠 AI-Powered
- Context-aware conversations using Llama 3.3 (via Groq)
- Dynamic technical question generation
- Intelligent information extraction from free-form text

### 🎨 Modern Interface
- Clean, dark-themed UI
- Interactive chat experience
- Progress indicators
- Mobile-friendly design

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/TalentScout_HiringAssistant.git
   cd TalentScout_HiringAssistant
   ```

2. **Create virtual environment**
   ```bash
   python -m venv envi
   
   # Windows
   envi\Scripts\activate
   
   # macOS/Linux
   source envi/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   
   Navigate to `http://localhost:8501`

---

## 💻 Usage

### For Candidates

1. Start chatting with the bot
2. Answer questions about your background:
   - Name
   - Email
   - Phone number
   - Years of experience
   - Desired position
   - Location
   - Tech stack
3. Answer the generated technical questions
4. Done! Your information is saved

### For Recruiters

- Monitor candidate progress in the sidebar
- View collected data in `candidates_db.json`
- Review technical question responses

---

## 📁 Project Structure

```
TalentScout_HiringAssistant/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (API keys)
├── candidates_db.json        # Candidate data storage
│
└── src/
    ├── llm_handler.py       # LLM interaction logic
    ├── prompts.py           # System prompts
    └── utils.py             # Utility functions
```

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key | Yes |

### Getting Your Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key
5. Copy to your `.env` file

---

## 🔄 How It Works

### 1. Information Gathering Phase
- Bot greets the candidate
- Asks for essential information one field at a time
- Validates and extracts data using AI
- Tracks progress in real-time

### 2. Technical Screening Phase
- Generates 3-5 questions based on tech stack
- Questions are tailored to experience level
- Collects candidate responses

### 3. Data Storage
- Saves complete candidate profile to JSON
- Each record includes all collected information
- Ready for recruiter review

### Example Conversation

```
Bot: Hello! I'm the TalentScout Hiring Assistant. What's your name?
User: John Doe

Bot: Great! What's your email address?
User: john@example.com

Bot: And your phone number?
User: +1-555-123-4567

...

Bot: What's your primary tech stack?
User: React, Node.js, PostgreSQL

Bot: Perfect! Let's move to technical questions:
     1. Explain React's Virtual DOM...
     2. How would you optimize a Node.js API...
```

---

## 🐛 Troubleshooting

### Common Issues

**API Key Error**
```bash
# Check your .env file exists and has the correct format
GROQ_API_KEY=gsk_your_key_here
```

**Module Not Found**
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
```

**Port Already in Use**
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

**Need More Help?**
- [Open an issue](https://github.com/yourusername/TalentScout_HiringAssistant/issues)
- Check [Streamlit docs](https://docs.streamlit.io/)
- Review [Groq documentation](https://console.groq.com/docs)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Guidelines
- Follow PEP 8 style guide
- Add comments for complex logic
- Update documentation as needed
- Test your changes thoroughly

---

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 TalentScout

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## 🙏 Acknowledgments

- **Groq** - Fast LLM inference
- **Streamlit** - Web framework
- **LangChain** - LLM orchestration
- **Meta AI** - Llama 3.3 model

---

<div align="center">

**Made with ❤️ by the TalentScout Team**

⭐ Star this repo if you find it helpful!

[Report Bug](https://github.com/yourusername/TalentScout_HiringAssistant/issues) • 
[Request Feature](https://github.com/yourusername/TalentScout_HiringAssistant/issues) • 
[Documentation](https://github.com/yourusername/TalentScout_HiringAssistant/wiki)

</div>
