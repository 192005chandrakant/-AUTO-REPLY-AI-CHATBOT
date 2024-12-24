# -AUTO-REPLY-AI-CHATBOT
 AUTO-REPLY AI CHATBOT
 This repository demonstrates an automated system for interacting with a chat application using the Gemini API. The system retrieves chat history, analyzes messages, and generates responses based on the last message.

Features
Initialization and Setup

Launches the chat application by clicking the Chrome icon.
Waits briefly to ensure the application is ready for interaction.
Chat History Retrieval

Periodically selects and copies chat history by dragging the mouse over the chat area.
Retrieves the copied text from the clipboard for further processing.
Message Analysis

Analyzes the retrieved chat history to identify if the last message is from a specific user (e.g., "Rohan Das").
If a match is found, the chat history is sent to the Gemini API for response generation.
Response Generation

Processes the chat history with the Gemini API to generate an appropriate response.
Copies the generated response to the clipboard.
Send Response

Pastes the response into the chat input field and sends it by pressing 'Enter'.
Ensures the application is ready for the next cycle of interaction.
Continuous Workflow

The system repeats the cycle of chat history retrieval, analysis, response generation, and sending.
How It Works
Clipboard Integration: Automates copying and pasting chat history and responses.
Targeted Message Analysis: Identifies messages from a specific user to trigger responses.
API Integration: Leverages the Gemini API for intelligent and contextual response generation.
Installation
Clone this repository.
Ensure dependencies for clipboard access and browser automation are installed.
Set up your Gemini API key in the configuration file.
Run the script and follow the instructions.
Usage
This system is ideal for automating responses in chat applications, making it efficient for tasks such as customer support or interactive bots.
