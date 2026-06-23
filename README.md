# ⚽ Football Expert AI

An intelligent football chatbot built with **LangChain**, **OpenAI/Gemini**, **Pydantic Structured Output**, and **Streamlit**. It provides conversational football knowledge, player profiles, achievements, and contextual memory in an interactive UI.

---

## 🚀 Features

* ⚽ Football-focused AI assistant
* 🧠 Conversational memory
* 📋 Structured responses using Pydantic
* 👤 Player profiles with:

  * Club
  * Position
  * Achievements
* 💬 Natural football conversations
* 🎨 Interactive Streamlit UI
* ⚡ Fast response generation
* 🔄 Session-based chat history
* 🌍 Ready for Tavily Search integration for live information

---

## 🏗 Project Structure

```text
football_expert_ai/
│
├── app.py                 # Streamlit UI
├── llm.py                 # LLM configuration
├── template.py            # Prompt template
├── schema.py              # Pydantic schema
├── chain_builder.py       # LangChain pipeline
├── .env                   # API keys
├── requirements.txt
└── README.md
```

---

## 🛠 Tech Stack

* Python
* LangChain
* OpenAI / Gemini
* Pydantic
* Streamlit
* dotenv

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/football-expert-ai.git
cd football-expert-ai
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

or

```env
GOOGLE_API_KEY=your_api_key
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## Example Queries

### General Chat

```
Hello
Who will win the World Cup?
Which young players should I watch?
```

### Player Queries

```
Tell me about Lionel Messi
Who is Lamine Yamal?
Tell me about Cristiano Ronaldo
Who is Endrick?
```

---

## Example Output

### Player Profile

```
⚽ Player: Cristiano Ronaldo
🏟 Club: Al-Nassr
📍 Position: Forward

🏆 Achievements
• 5 Ballon d'Or Awards
• UEFA Euro 2016
• UEFA Nations League

📝 Summary
Cristiano Ronaldo is widely regarded as one of the greatest footballers in history...
```

---

## Future Improvements

* 🌐 Tavily Search Integration
* 📊 Player statistics cards
* 📰 Transfer news
* 🖼 Player images
* ⚽ Live scores and fixtures
* 🏆 Trophy timelines
* 📈 Performance charts
* Database-backed memory
* Multi-agent architecture

---


## Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a pull request

---

## License

MIT License

---

### Built with ❤️ using LangChain, Streamlit, and Large Language Models.
