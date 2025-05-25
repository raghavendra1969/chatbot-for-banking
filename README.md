
# 🏦 AI Banking Chatbot with Voice Support (MongoDB-ready)

An AI-powered chatbot built for banking websites. This assistant responds to banking-related queries such as loans, Aadhaar linking, credit cards, mobile banking, pensions, and more. It supports both voice and text input/output, with a clean user interface and machine learning-based intent classification.

> **Note:** MongoDB database connection is **prepared but not yet integrated**.

---

## 🔑 Features

- 💬 Text and 🎤 voice input/output using Web Speech API
- 🧠 Intent classification using NLTK and scikit-learn
- 📚 Trained on custom banking FAQs (`intents.json`)
- 📅 Time-aware dynamic responses (e.g., “How many days until Christmas?”)
- 🎨 Responsive and interactive web UI
- 🚫 Handles unknown input gracefully
- 🔧 MongoDB ready for future use (e.g., storing user info, session history)

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **NLP/ML**: NLTK, scikit-learn, pickle
- **Voice**: Web Speech API
- **Planned DB**: MongoDB with `pymongo`

---

## 📁 Project Structure

```
chatbot_ml_project/
├── app.py                # Flask application
├── chatbot.py            # Handles ML model and responses
├── train.py              # Script to train the model
├── intents.json          # Banking questions and answers
├── templates/
│   └── index.html        # Web UI for the chatbot
├── static/
│   └── style.css         # UI styling (optional)
├── requirements.txt      # Python dependencies
```

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/yourusername/chatbot_ml_project.git
cd chatbot_ml_project
pip install -r requirements.txt
python train.py
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🧠 Future Improvements

- ✅ MongoDB integration to store user info and chat history
- 🌍 Multilingual support (Hindi, Kannada, etc.)
- 🤖 GPT-3/4 fallback for unmatched queries
- 📊 Admin dashboard for analytics
- 🔐 OTP/Verification simulation for real-world banking flow

---

## 👨‍💻 Developer

**Raghavendra**  
3rd-year B.Tech Student  
Passionate about AI, Web Development & Banking Technology

---

## 📄 License

MIT License - free to use and modify.
