# 🩺 MediTalk – AI-Powered Medical Assistant Chatbot

**MediTalk** is a multilingual AI-powered chatbot designed to answer basic medical questions in natural language. It uses **LLM models served via Ollama**, supports **language translation**, and offers a simple **Streamlit web interface**. Users can ask questions in their native language and get translated, medically relevant answers.

> ⚠️ **Disclaimer**: MediTalk is not a substitute for professional medical advice. Always consult a licensed healthcare provider.

---

## 🚀 Features

- 💬 Text-only interaction (no speech input/output)
- 🌐 Supports multiple languages with auto-translation
- 🧠 Uses locally hosted models via [Ollama](https://ollama.com/)
- 📜 Chat history display
- 🧹 Clear history button
- 🎨 Lottie animation-enhanced UI

---

## 🖼️ Demo Screenshot

![screenshot](assets/meditalk_demo.png) <!-- optional: add your screenshot -->

---

## 🧰 Tech Stack

| Component        | Description                            |
|------------------|----------------------------------------|
| **Frontend**     | Streamlit                              |
| **Backend Model**| LLM via Ollama (`llama3`, `gemma`, etc.) |
| **Translation**  | Custom `translate()` module using Google Translate API / offline models |
| **Language Support** | English, Hindi, Bengali, French, Tamil, and more |

---

## 🌍 Supported Languages

- English (`en`)
- Hindi (`hi`)
- Bengali (`bn`)
- French (`fr`)
- German, Spanish, Tamil, Telugu, Kannada, and more

---


# MediTalk – Project Setup Guide (with Conda Environment)

This guide helps you set up the **MediTalk** chatbot (no speech I/O) using **Ollama + Streamlit**, with a **Conda environment**.


## 1) Clone the Repository

```bash
git clone https://github.com/sumansamui/LLM_projects.git
cd LLM_projects/meditalk
```

---

## 2) Create & Activate Conda Environment

```bash
# Create environment with Python 3.10 (or desired version)
conda create -n meditalk python=3.10 -y

# Activate environment
conda activate meditalk
```

To deactivate later:
```bash
conda deactivate
```

---

## 3) Install Python Dependencies

If you have a `requirements.txt`:
```bash
pip install -r requirements.txt
```

Otherwise install manually:
```bash
pip install streamlit requests streamlit-lottie python-dotenv langdetect
```

> You can also use `conda install` for some packages, but `pip` ensures latest versions for Streamlit.

---

## 4) Install Ollama

Download & install from: https://ollama.com/download

After installation, pull a model (choose one):
```bash
ollama pull llama3
# or
ollama pull gemma:2b
```

Check installed models:
```bash
ollama list
```

---

## 5) Run the App

```bash
streamlit run app_text.py
```

---

## 👤 Author

**Suman Samui**  
Department of Electronics and Communication Engineering  
National Institute of Technology Durgapur  
📧 Email: ssamui.ece@nitdgp.ac.in  
🔗 [GitHub](https://github.com/sumansamui)
