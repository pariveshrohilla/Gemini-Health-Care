## Gemini Health Assistant

A simple Streamlit-based chatbot that uses **Google's Gemini 1.5 Flash** model to provide general health and wellness advice.

### Features

* Chatbot powered by **Gemini AI** for health-related queries
* Provides advice on **nutrition**, **exercise**, **lifestyle**, and **OTC remedies**
* Uses **Streamlit Secrets** for securely storing API keys
* Remembers your conversation history across interactions
* Built using `gemini-1.5-flash` for fast and efficient responses

---

### Tech Stack

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Google Generative AI (Gemini)](https://ai.google.dev/)

---

### Getting Started

#### 1. Clone the Repository

```bash
git clone https://github.com/pariveshrohilla/Gemini-Health-Care.git
cd Gemini-Health-Care
```

#### 2. Install Dependencies

> streamlit
> google-generativeai
> ```

#### 3. Set Up Your API Key

Create a file at `.streamlit/secrets.toml` and add your Gemini API key:

```toml
GOOGLE_API_KEY = "your_api_key_here"
```

> You can obtain an API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

#### 4. Run the App

```bash
streamlit run main.py
```

---

### Usage

* Open the app in your browser (usually at `http://localhost:8501`)
* Ask health-related questions like:

  * "What are some healthy breakfast options?"
  * "What can I take for a headache?"
  * "How much water should I drink daily?"

The assistant will provide helpful information and always include a clear disclaimer about not being a medical professional.

---

### Demo

![feet cold](https://github.com/user-attachments/assets/87c8ee60-0845-4b44-b983-d5d014b7c61f)



## Live 

https://gemini-health-care-vorux4qb7pbtqmcgcapufw.streamlit.app/

Use this link to see how this works 
