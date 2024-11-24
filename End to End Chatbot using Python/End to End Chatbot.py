# Streamlit app
def main():
    st.title("Chatbot")
    st.write("Welcome! Type your message below to chat with the bot.")

    # Chat input
    user_input = st.text_input("You:", key="user_input")

    if user_input:
        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=100, max_chars=None, key="chatbot_response")

        # End the conversation on "bye"
        if user_input.lower() in ["bye", "exit", "quit"]:
            st.write("Thank you for chatting! Goodbye!")
            st.stop()

if __name__ == "__main__":
    main()