Voice Assistant Project

This is a custom voice assistant built using Python. It leverages various libraries for speech recognition, text-to-speech, and automation tasks like searching Wikipedia, playing YouTube videos, and providing the current time and date. This assistant is a simple implementation but can be extended with additional features and functionalities to make it more intelligent and versatile.
Features

- Speech Recognition: Convert spoken commands into text.
- Text-to-Speech: Respond back to the user with spoken responses.
- Time and Date: Tell the current time and date.
- Wikipedia Search: Search Wikipedia for queries.
- YouTube Search: Play videos on YouTube.
- Open Applications: Open applications or websites based on voice commands.
- Exit Command: Shut down the assistant gracefully when you say "exit" or "quit."

Prerequisites

Before running the voice assistant, make sure you have the following installed:

- Python 3.x
- Pip (Python's package installer)

Dependencies

Install the required libraries using `pip`:

```bash
pip install SpeechRecognition pyttsx3 pywhatkit wikipedia
```

How to Use

1. Clone the Repository:

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/voice-assistant.git
   cd voice-assistant
   ```

2. Run the Script:

   Make sure you have a working microphone. Then run the Python script:

   ```bash
   python voice_assistant.py
   ```

3. Commands:

   - Tell Time: "What is the time?"
   - Tell Date: "What is the date?"
   - Search Wikipedia: "Search Wikipedia for Python programming."
   - Play on YouTube: "Play Shape of You on YouTube."
   - Open Application: "Open Chrome" or "Open Notepad."
   - Exit: "Exit" or "Quit."

 Example Interaction

```text
User: "What is the time?"
Assistant: "The current time is 14:45:30."

User: "Search Wikipedia for Python programming."
Assistant: "Searching Wikipedia for Python programming... Python is a high-level programming language that emphasizes code readability."

User: "Play Shape of You on YouTube."
Assistant: "Playing Shape of You on YouTube."

User: "Exit"
Assistant: "Goodbye!"

Troubleshooting

1. Speech Recognition Issues:
   - Ensure your microphone is properly configured and working.
   - If the assistant doesn't understand your speech, try speaking clearly and avoid background noise.

2. Missing Libraries:
   - Ensure all the required dependencies are installed by running the `pip install` command above.

Contributions

Feel free to fork this project, submit pull requests, and suggest improvements. Contributions are welcome!

License

This project is open-source and available under the MIT License
Author

[Your Name]  
[Your GitHub Profile URL]  
[Your Email Address (optional)]
