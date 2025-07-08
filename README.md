▶️ YouTube Demo: [Watch Here](https://www.youtube.com/watch?v=G18bM5At4F0&ab_channel=Jatin)  
# 🔍 AI Web Assistant with LangChain + Tavily + Groq

This project is an **improved real-time search chatbot** built using:

- 🧠 [LangChain](https://www.langchain.com/)
- ⚡ [Groq’s LLaMA3-70B](https://groq.com/)
- 🔎 [Tavily Search](https://www.tavily.com/)
- 📚 Wikipedia + Arxiv for research
- 🧵 [Streamlit](https://streamlit.io/) for the user interface

> ✅ **Project Title:** Real-Time Web Search Chatbot with Tavily, LangChain & Groq

---

## 🚀 Why I Built This

After building a DuckDuckGo-powered chatbot, I faced issues like:
- 🌐 Irrelevant or generic results
- ⛔ Rate limits
- 🧵 Lack of citations or structured context

So I upgraded to **Tavily**, a focused web search API built for LLMs — delivering better and more relevant results.  
Now paired with **Groq's ultra-fast LLaMA3-70B**, the chatbot gives structured, smart, and fast answers.

---

## ✨ Key Features

- 🔎 Real-time web search with **Tavily**
- 📚 Scientific and factual grounding using **Wikipedia** + **Arxiv**
- ⚡ Powered by **Groq LLaMA3-70B** for blazing-fast reasoning
- 🧠 LangChain **Agent** logic for tool-based responses
- 🖥️ Clean chat interface using **Streamlit**
- 🛡️ All keys managed securely using `.env`

---

## 🧠 How It Works

1. User enters a prompt → “Latest updates on AI agents”
2. LangChain Agent chooses which tools to call:
   - Tavily → Web search
   - Wikipedia → Definitions
   - Arxiv → Scientific papers
3. Groq’s LLaMA3-70B processes all returned context
4. Final answer is generated and shown in a nice UI

---

## 💬 Example Prompts

- “Give me recent news on generative AI”
- “Who proposed the transformer architecture?”
- “Find a research paper on vision-language models”
- “Explain what RAG is using Wikipedia”

---

## 📁 Project Structure

```bash
.
├── app.py               # Streamlit-based chatbot app
├── .env                 # API keys (Tavily + Groq)
├── requirements.txt     # All Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/jatinydav557/improved-search-engine-tavily.git
cd improved-search-engine-tavily
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add `.env` File

```env
TAVILY_API_KEY=your_tavily_key
GROQ_API_KEY=your_groq_key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 📦 Dependencies

```txt
streamlit
python-dotenv

# LangChain core + integrations
langchain
langchain-core
langchain-community
langchain-openai
langchain-groq
langchain-text-splitters

# Tool APIs
tavily-python
arxiv
wikipedia

# Optional: Embeddings + HF hub
sentence-transformers
huggingface_hub
```

---

## 🙋‍♂️ About Me

Hi, I’m **Jatin**, a final-year **MCA student** passionate about building real-world AI tools with:
- 🔍 LLM Agents
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚙️ MLOps & GenAI Apps

I've built 20+ GenAI projects — each helping me get closer to my dream role in applied AI and product-driven AI engineering.

📌 Actively looking for:
- 🤖 LLM & RAG Engineering Roles
- 🧠 NLP / Conversational AI Research
- ⚙️ AI Tooling / MLOps Roles

---

## 🌐 Connect With Me

- 🔗 [LinkedIn](https://www.linkedin.com/in/jatin557)
- 🖥️ [GitHub](https://github.com/jatinydav557)
- 📧 [jatinydav557@gmail.com](mailto:jatinydav557@gmail.com)
- 📱 +91-7340386035
- 🎥 [YouTube Projects](https://www.youtube.com/@jatinML/playlists)

---

## 🧭 Roadmap / Improvements

- [ ] Add multi-turn memory with LangChain `ConversationBufferMemory`
- [ ] Save chat logs & export to PDF/Markdown
- [ ] Add fallback to DuckDuckGo or SerpAPI
- [ ] Deploy on Hugging Face Spaces or GCP Cloud Run

---

⭐ If this project helped you, consider giving it a **star** and **fork it** to build your own assistant!

> “I don’t just use AI — I build it.”

