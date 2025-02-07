import streamlit as st
import nltk
from transformers import pipeline

# Optimized Model for Fast and Accurate Responses
chatbot = pipeline("text-generation", model="gpt2-medium")  # Consider upgrading to GPT-4 or BioGPT for professional accuracy

# Healthcare Chatbot Logic Focused on Speed, Accuracy, and Medical Relevance
def healthcare_chatbot(user_input):
    user_input = user_input.lower()

    # Emergency Response Handling
    emergency_keywords = ["chest pain", "shortness of breath", "severe bleeding", "unconscious", "stroke symptoms"]
    if any(keyword in user_input for keyword in emergency_keywords):
        return ("🚨 **URGENT:** Your symptoms could indicate a medical emergency. **Seek immediate medical attention** by calling emergency services or going to the nearest hospital. Do NOT wait for symptoms to worsen.")

    if "symptom" in user_input:
        return ("Please describe your symptoms (e.g., duration, severity). "
                "For urgent conditions like chest pain, seek immediate medical help. I recommend consulting a doctor for an accurate diagnosis.")

    elif "appointment" in user_input:
        return ("Would you like to schedule an appointment with a specialist? Please provide your preferred date and time.")

    elif "medication" in user_input:
        return ("Are you asking about a specific medication? It's crucial to follow your doctor's prescription. "
                "Let me know if you'd like information on side effects or interactions.")

    elif "fever" in user_input:
        return ("For fever, stay hydrated and monitor your temperature. "
                "If it exceeds 102°F (39°C) or persists for more than 3 days, consult a doctor immediately.")

    else:
        # General AI Response for Non-Emergency Queries
        response = chatbot(user_input, max_length=100, num_return_sequences=1)
        return response[0]['generated_text']

# Streamlit App

def main():
    st.title("🩺 Healthcare Assistant Chatbot")
    st.write("I am here to assist you with health-related queries. **Always consult a doctor for professional medical advice.**")

    user_input = st.text_area("How can I assist you today?")

    if st.button("Submit"):
        if user_input:
            st.write(f"**You:** {user_input}")
            with st.spinner("Processing your query, please wait..."):
                response = healthcare_chatbot(user_input)
            st.write(f"**Healthcare Assistant:** {response}")
        else:
            st.warning("Please enter your message to receive a response.")

    # Informational User Profile (No Impact on Responses)
    if st.checkbox("Enter Profile Information (Optional)"):
        name = st.text_input("Name:")
        age = st.number_input("Age:", min_value=0, max_value=120)
        conditions = st.text_area("Medical History/Conditions:")
        if st.button("Save Information"):
            st.success(f"Profile information saved: {name}, Age: {age}, Conditions: {conditions}")

if __name__ == "__main__":
    main()
