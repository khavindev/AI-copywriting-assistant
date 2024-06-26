import streamlit as st
import google.generativeai as genai

# Configure API key (replace with your own)
genai.configure(api_key='AIzaSyAqkVyZJY6ON-LWx6YbHMgWbwOOPjYiOoo')

# Model configuration
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

# Load generative model
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="You are an AI copywriter assistant tasked with creating compelling marketing copy with a focus on SEO and originality. Given a topic, your role involves:\n\n1. Generating creative and engaging content based on provided prompts while optimizing for search engines (SEO).\n2. Conducting keyword research to identify relevant keywords and phrases for SEO integration.\n3. Crafting clear, concise, and persuasive copy that incorporates SEO best practices such as meta tags, headers, and keyword density.\n4. Ensuring the accuracy, credibility, and originality of the information presented.\n5. Avoiding plagiarism by providing proper attribution and referencing sources when necessary.\n6. Adhering to a professional tone and style in all communications.\n7. Collaborating with users to refine and optimize the generated content as needed.\n8. Providing suggestions and improvements to enhance the quality and SEO performance of the final copy.\n\nYour objective is to assist users in generating high-quality marketing materials that not only resonate with their target audience but also rank well in search engine results through effective SEO strategies and ethical content practices."  # Same system instruction as before
)

def generate_copy(prompt):
  chat_session = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          "Hi\n",
        ],
      },
      {
        "role": "model",
        "parts": [
          "Hi! \n\nI'm ready to help you create compelling marketing copy that gets results.  \n\nTell me more about your project:  \n",
        ],
      },
    ]
  )
  response = chat_session.send_message(prompt)
  return response.text

# Streamlit app



def wide_space_default():
  st.set_page_config(layout="wide")   #function to set base page to wide

wide_space_default()

backgroundColor="#ececde"
secondaryBackgroundColor="#dddde0"
textColor="#2f2b2b"


#sidebar
with st.sidebar:
        st.header("🪄")
        st.subheader("*Made by khavindev✨*")
        st.write("Copyright @ **TextFusion**")
        st.write("[My LinkedIn](https://www.linkedin.com/in/s-khavin73/)")
        st.write("[Github](https://github.com/khavindev)")
        st.write("[Instagram](https://instagram.com/curiosity.ai_)")
        st.write("if you have any issues ping me on linkedin or instagram")
        st.write("[Powered by gemini-1.5]")

#Main page TITLE and subheader

st.write(" ")
st.write(" ")
st.write(" ")
st.write("")
st.title("**TextFusion Copywriter Assistant📝:**")
st.subheader("*Craft a irresistable marketing copy that captivates and converts🌹🌙*")
st.write(" ")
# User input
user_input = st.text_input("💬Enter your marketing content type and desired tone (e.g., website copy - informative, blog post - engaging):✍️")

if st.button("Get Response✨"):
    if user_input:
        chat_session = model.start_chat(  #starting model chat
            history=[]                    #initialize history for state remembering
        )

        response = chat_session.send_message(user_input)
        st.write(response.text)
    else:
        st.write("Please enter a question.")