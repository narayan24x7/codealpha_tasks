Fibonacci Generator

This is a simple Python-based Fibonacci generator that generates Fibonacci numbers either up to a specified number of terms or indefinitely using a generator function.

---

Features

- Fibonacci Sequence: Generates Fibonacci numbers using the mathematical recurrence relation.
- Customizable Terms: Generate as many terms of the Fibonacci sequence as you need.
- Generator-Based: Uses Python's generator functionality for efficient and memory-friendly number generation.

---

Prerequisites

Before running the Fibonacci generator, make sure you have the following installed:

- Python 3.x

Installation

To use the Fibonacci generator, simply clone the repository or download the script to your local machine.

```bash
git clone https://github.com/your-username/fibonacci-generator.git
cd fibonacci-generator
```

No additional dependencies are needed for this script as it only relies on standard Python libraries.

---

How to Use

1. Clone the Repository:

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/fibonacci-generator.git
   cd fibonacci-generator
   ```

2. Run the Script:

   After cloning, open the terminal and run the `fibonacci_generator.py` script:

   ```bash
   python fibonacci_generator.py
   ```

3. Example Usage:

   You can modify the script to print the desired number of Fibonacci terms by adjusting the `num_terms` variable.

   ```python
   num_terms = 10  # Modify the number of terms you want
   fib = fibonacci_generator(num_terms)
   for number in fib:
       print(number)
   ```

   In this example, the first 10 Fibonacci numbers will be printed.

---

Fibonacci Generator Code Example

```python
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

Example usage: Print the first 10 Fibonacci numbers
num_terms = 10
fib = fibonacci_generator(num_terms)
for number in fib:
    print(number)
```

Explanation:

- The generator `fibonacci_generator` yields the Fibonacci numbers one by one up to the specified `n` terms.
- You can adjust `num_terms` to generate as many Fibonacci numbers as you wish.

---

Example Output

```text
0
1
1
2
3
5
8
13
21
34
```

---

Troubleshooting

1. Errors with Python Version:
   - Ensure you're using Python 3.x to run the script, as older versions may not support certain features used in the code.

2. Running the Script:
   - Make sure the Python script is located in the correct directory and that your terminal or command prompt is set to that directory.

---

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
