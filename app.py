import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

from config.globals import SPEAKER_TYPES, initial_prompt
from services.model.generative_ai import StudentModelChat

chat_conversation = StudentModelChat()

# Set up the streamlit app
st.set_page_config(
  page_title="Deep Neural Network",
  page_icon="🤖",
  layout="wide",
  initial_sidebar_state="expanded",
)

# Initialize a session state to hold the chat history
if 'chat_history' not in st.session_state:
  st.session_state.chat_history = [initial_prompt]

# Define output array
output_array = []

def clear_chat_history():
  st.session_state.chat_history = [initial_prompt]

def display_home():
  st.title('Home')
  prompt = st.chat_input("Ask me any question...", key="user_input")

  # Show the welcome prompt
  with st.chat_message(SPEAKER_TYPES.BOT, avatar="🤖"):
    st.write(initial_prompt['content'])

  if prompt:
    st.session_state['chat_history'].append({'role': SPEAKER_TYPES.USER, 'content': prompt})
    
    # Display chat messages
    for message in st.session_state.chat_history[1:]:
      with st.chat_message(message["role"], avatar="👤" if message['role'] == SPEAKER_TYPES.USER else "🤖"):
        st.write(message["content"])
    
    response_stream = chat_conversation.get_response(prompt, stream=True)
    response_text = ''
    with st.chat_message(SPEAKER_TYPES.BOT, avatar="🤖"):
      placeholder = st.empty()
      with st.spinner(text='Generating response...'):
        for chunk in response_stream:
          response_text += chunk.text
          replaced_text = response_text.replace("language model, trained by Google", "language model, trained by Yahweh Tech").replace("I am Gemini", "I am Gemini Yahweh Tech").replace("I am Gemini Yahweh Tech, a multimodal AI language model developed by Google.", "I am Yahweh Tech bot, a multimodal AI language model developed by Yahweh Tech.")
          placeholder.markdown(f'<div class="animated-text">{replaced_text}</div>', unsafe_allow_html=True)
          output_array.append(replaced_text)
        placeholder.markdown(f'<div class="animated-text">{replaced_text}</div>', unsafe_allow_html=True)
    
    st.session_state['chat_history'].append({'role': SPEAKER_TYPES.BOT, 'content': response_text})

def display_about():
    st.title('About')
    st.write('This application is developed by Adebayo Adetayo .')
    
    st.write("""
    **Adebayo Adetayo ** is a dedicated student from Gateway ICT Polytechnic Saapade, located in Ogun State, Nigeria. He is currently pursuing a National Diploma (ND) in Computer Science, showcasing his commitment to understanding and excelling in the field of technology.
    
    ### Educational Background
    Adebayo is enrolled in the Computer Science program at Gateway ICT Polytechnic, where he is gaining foundational knowledge and practical skills in various aspects of computing. His coursework includes programming, software development, data structures, algorithms, and computer systems, among other subjects. This rigorous curriculum is designed to prepare students for careers in the fast-evolving tech industry.
    
    ### Skills and Interests
    Throughout his studies, Adebayo has developed a strong interest in several key areas within computer science, including:
    
    - **Programming Languages**: He is proficient in languages such as Python, Java, and C++, which are essential for software development and algorithm implementation.
    - **Web Development**: Adebayo has explored web technologies, including HTML, CSS, JavaScript, and frameworks like React or Django, enabling him to create dynamic and responsive web applications.
    - **Data Analysis**: With a growing interest in data science, he has learned to use tools like NumPy, Pandas, and Matplotlib to analyze and visualize data, providing valuable insights.
    - **Artificial Intelligence and Machine Learning**: He is fascinated by AI and ML technologies and has started to delve into these areas, understanding how they can be applied to solve real-world problems.
    
    ### Projects and Experience
    As part of his academic journey, Adebayo has worked on various projects that highlight his skills and knowledge. These projects include:
    
    - **Chatbot Development**: Creating intelligent chatbots using natural language processing (NLP) techniques, enhancing user interaction and providing automated assistance.
    - **Web Applications****: Developing full-stack web applications that demonstrate his ability to integrate front-end and back-end technologies.
    - **Data Analysis Projects**: Conducting data analysis projects to extract meaningful patterns and trends from datasets, improving decision-making processes.
    
    ### Personal Attributes
    Adebayo is known for his:
    
    - **Dedication and Hard Work**: He is committed to his studies and consistently strives for excellence in all his academic endeavors.
    - **Curiosity and Eagerness to Learn**: Adebayo has a natural curiosity and a strong desire to learn new technologies and concepts, staying updated with the latest trends in computer science.
    - **Problem-Solving Skills**: He enjoys tackling complex problems and finding innovative solutions, a key trait for success in the tech industry.
    - **Teamwork and Collaboration**: Adebayo values teamwork and has experience working collaboratively on projects, understanding the importance of effective communication and cooperation.
    
    ### Future Aspirations
    Looking ahead, Adebayo aims to further his education and gain more experience in the tech industry. He aspires to become a software developer or data scientist, contributing to the development of innovative technologies and solutions. His long-term goal is to leverage his skills and knowledge to make a positive impact in the field of technology and society at large.
    """)

def display_chart_performance():
  st.title('Chart Performance')
  
  # Simulate some data for chart performance
  effectiveness_data = np.random.rand(10, 3)  # 10 data points, 3 dimensions
  fig, ax = plt.subplots()
  ax.plot(effectiveness_data)
  ax.set_title('User Chat Effectiveness')
  ax.set_xlabel('Interaction')
  ax.set_ylabel('Effectiveness')
  st.pyplot(fig)

def display_contact():
    st.title('Contact')
    st.write('For more information, contact:')
    st.write("""
    **Adebayo Adetayo **  
    **📞 +2347066253101**  
    **📧 adebayoadetayo284@gmail.com**
    """)

# Custom CSS for sidebar and text animation
custom_css = """
<style>
  .sidebar .sidebar-content {
    background-color: #f4f4f4;
    padding: 20px;
    border-radius: 10px;
  }
  .sidebar .sidebar-content h1, .sidebar .sidebar-content h2, .sidebar .sidebar-content h3 {
    color: #2e3b4e;
  }
  .sidebar .sidebar-content p {
    color: #5c677d;
  }
  .sidebar .sidebar-content .stButton>button {
    background-color: #2e3b4e;
    color: #ffffff;
  }
  .sidebar .sidebar-content .stRadio>div>div>div>div {
    background-color: #2e3b4e;
    color: #ffffff;
  }
  .animated-text {
    animation: fadeIn 2s ease-in-out;
  }
  @keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
  }
</style>
"""

# Inject the custom CSS
components.html(custom_css, height=0)

with st.sidebar:
  st.title('♊💬 Deep Neural Network to optimize Student Revision Classes')
  st.write('Developed by Adebayo Adetayo ')
  st.sidebar.button('Clear Chat', on_click=clear_chat_history, type='secondary')
  
  choice = st.radio('Navigation', ['HOME', 'ABOUT', 'CHART PERFORMANCE', 'CONTACT'])

# Display the chosen page
if choice == 'HOME':
  display_home()
elif choice == 'ABOUT':
  display_about()
elif choice == 'CHART PERFORMANCE':
  display_chart_performance()
elif choice == 'CONTACT':
  display_contact()
