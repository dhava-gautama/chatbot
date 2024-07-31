import streamlit as st
import httpx
import asyncio

# Show title and description
st.title("💬 LLM Chatbot")
st.write(
    "This is a simple chatbot that uses a custom LLM server to generate responses. "
    "You can interact with the chatbot by typing your messages in the input field below."
)

# Create a session state variable to store the chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar for model and parameter selection
st.sidebar.title("Model Settings")
model = st.sidebar.selectbox("Select Model", ['gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo'])
frequency_penalty = st.sidebar.slider("Frequency Penalty", 0.0, 2.0, 0.0, 0.1)
presence_penalty = st.sidebar.slider("Presence Penalty", 0.0, 2.0, 0.0, 0.1)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5, 0.1)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.95, 0.05)

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Proxy function
async def proxy_request(messages):
    url = "https://api.amigochat.io/v1/chat/completions"
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
if prompt := st.chat_input("What would you like to know?"):
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
    st.session_state.messages = []
    st.rerun()  # Changed from st.experimental_rerun() to st.rerun()