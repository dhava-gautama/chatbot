import streamlit as st
import httpx
import asyncio

# Show title and description
st.title("💬 Python AI Assistant")
st.write(
    "This is an advanced AI chatbot specialized in Python programming. "
    "Ask questions about Python, get help with code, or discuss best practices!"
)

# Create a session state variable to store the chat messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are an advanced AI assistant specialized in Python programming. Your primary function is to assist users with Python-related tasks, including but not limited to:\n\n1. Writing efficient and Pythonic code\n2. Debugging and troubleshooting existing code\n3. Explaining complex Python concepts\n4. Recommending best practices and design patterns\n5. Assisting with Python libraries and frameworks\n\nWhen responding to queries:\n\n- Prioritize writing clean, efficient, and readable code\n- Adhere to PEP 8 style guidelines\n- Provide detailed explanations of your code and reasoning\n- Suggest alternative approaches when appropriate\n- Highlight potential pitfalls or edge cases\n- Recommend relevant Python libraries or tools when applicable\n\nYour knowledge encompasses:\n\n- Core Python (versions 3.6+)\n- Popular libraries and frameworks (e.g., NumPy, Pandas, Django, Flask, SQLAlchemy)\n- Advanced Python features (e.g., decorators, generators, context managers)\n- Object-oriented programming principles\n- Functional programming concepts\n- Asynchronous programming (asyncio)\n- Testing frameworks (unittest, pytest)\n- Performance optimization techniques\n\nWhen asked to write code:\n\n1. Begin with a brief explanation of your approach\n2. Write the code, including appropriate comments\n3. Explain key parts of the code after presenting it\n4. Suggest possible improvements or variations\n\nIf a user's code contains errors:\n\n1. Identify and explain the error(s)\n2. Provide a corrected version of the code\n3. Explain why the correction resolves the issue\n\nAlways strive to educate the user and promote good coding practices. If a user's approach is suboptimal, suggest improvements while explaining the benefits of the suggested changes.\n\nRemember to tailor your responses to the user's perceived skill level, providing more detailed explanations for beginners and more advanced insights for experienced developers."}
    ]

# Sidebar for model and parameter selection
st.sidebar.title("Model Settings")
model = st.sidebar.selectbox("Select Model", ['gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo'])
frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 2.0, 0.0, 0.1)
presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 2.0, 0.0, 0.1)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5, 0.1)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.95, 0.05)

# Display existing chat messages
for message in st.session_state.messages[1:]:  # Skip the system message
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Proxy function
async def proxy_request(messages):
    url = st.secrets["url"]
    headers = {
        'x-device-platform': 'android',
        'x-device-version': '9',
        'x-device-brand': 'samsung',
        'x-device-id': 'SM-S906N',
        'x-app-build-number': '13',
        'x-app-version': '1.0',
        'x-app-default-lang': 'en',
        'content-type': 'application/json',
        'user-agent': 'okhttp/4.12.0',
    }
    data = {
        'messages': messages,
        'model': model,
        'frequency_penalty': frequency_penalty,
        'presence_penalty': presence_penalty,
        'stream': False,
        'temperature': temperature,
        'top_p': top_p,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

# Chat input field
if prompt := st.chat_input("Ask about Python or share your code here"):
    # Store and display the current prompt
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send request to the proxy function
    with st.spinner("Thinking..."):
        try:
            result = asyncio.run(proxy_request(st.session_state.messages))
            
            # Extract the assistant's message from the response
            assistant_message = result.get('message', '')
            
            # Display and store the assistant's response
            with st.chat_message("assistant"):
                st.markdown(assistant_message)
            st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        
        except httpx.HTTPStatusError as e:
            st.error(f"An error occurred: HTTP {e.response.status_code} - {e.response.text}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")

# Add a button to clear the chat history
if st.button("Clear Chat History"):
    st.session_state.messages = [st.session_state.messages[0]]  # Keep only the system message
    st.rerun()
