import google.generativeai as genai

from config.globals import get


# Configure GenAI
genai.configure(api_key=get)


class GenetatetiveInputs:
  def __init__(self, model_name:str):
    """
      model_name: str - The name of the model to initialise. enum: ["Deep Neural Network", "Developed by Adetayo Adebayo Abdulrasaki"]
    """
    self.model_name = model_name
    self.api_key = get
    
    # Initialise the model
    self.model = genai.GenerativeModel(self.model_name)
    

class StudentModelChat(GenetatetiveInputs):
  def __init__(self):
    super().__init__("gemini-pro") # Deep_Neural_network
    
    # Start a chat
    self.chat = self.model.start_chat(history=[])
    
  def get_response(self, prompt:str, stream:bool=False):
    # Generate a response
    response = self.chat.send_message(prompt, stream=stream)
    if not stream:
      return response.text
    return response

