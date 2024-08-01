# Python AI Assistant

## Overview

Python AI Assistant is a Streamlit-based web application that provides an interactive chat interface with an AI specialized in Python programming. This AI assistant is designed to help users with various Python-related tasks, including code writing, debugging, explaining concepts, and recommending best practices.

## Features

- Interactive chat interface
- AI responses tailored to Python programming
- Customizable AI model settings
- Code explanation and debugging assistance
- Python best practices and design pattern recommendations

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/dhava-gautama/chatbot-python-coding.git
   cd chatbot-python-coding
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install streamlit httpx
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

3. Use the chat interface to ask Python-related questions, share code for review, or seek explanations on Python concepts.

4. Adjust the AI model settings in the sidebar to customize the responses:
   - Select the AI model
   - Adjust frequency penalty, presence penalty, temperature, and top_p values

5. Use the "Clear Chat History" button to start a new conversation.

## AI Capabilities

The AI assistant is specialized in Python programming and can help with:

- Writing efficient and Pythonic code
- Debugging and troubleshooting existing code
- Explaining complex Python concepts
- Recommending best practices and design patterns
- Assisting with Python libraries and frameworks

The AI's knowledge encompasses:

- Core Python (versions 3.6+)
- Popular libraries and frameworks (e.g., NumPy, Pandas, Django, Flask, SQLAlchemy)
- Advanced Python features (e.g., decorators, generators, context managers)
- Object-oriented programming principles
- Functional programming concepts
- Asynchronous programming (asyncio)
- Testing frameworks (unittest, pytest)
- Performance optimization techniques

## Contributing

Contributions to improve the Python AI Assistant are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This application uses an AI model provided by a third-party API. While efforts have been made to ensure the AI provides accurate and helpful information, users should verify important information and use their judgment when applying AI suggestions in their code.
