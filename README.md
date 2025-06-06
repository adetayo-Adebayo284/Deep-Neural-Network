# Deep Neural Network to Optimize Student Revision Classes

A Streamlit web application that leverages Google Generative AI to provide an interactive chatbot for student revision, performance charting, and developer information.

## Features

- 🤖 Chatbot powered by Google Generative AI
- 📈 Chart performance visualization
- ℹ️ About and contact information pages
- 🎨 Custom sidebar and animated responses

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Set your Google Generative AI API key**  
   Create a `.env` file in the `config` directory and add:
   ```
   get='YOUR_API_KEY'
   ```
4. **Run the app**
   ```
   streamlit run app.py
   ```

## Directory Structure

```
DeepNeural/
├── app.py
├── config/
│   └── globals.py
├── services/
│   └── model/
│       └── generative_ai.py
└── README.md
```

## Developer

**Adebayo Adetayo**  
Gateway ICT Polytechnic Saapade, Ogun State, Nigeria  
📧 adebayoadetayo284@gmail.com

## Requirements

- Python 3.8+
- Streamlit
- google-generativeai
- python-dotenv