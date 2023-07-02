# Voice Controlled AI Assistant

Voice Controlled AI Assistant is an early-stage proof of concept that will eventually be a mobile app allowing users to listen to bot responses related to the voices and dialog around them. The assistant utilizes the ChatGPT engine ("text-davinci-003"), which can be modified according to requirements.

## How to Use

1. Enter your OPEN AI API key in the `.env` file.
2. Run `Voice_Enabled_AI_Assistant.py`.
3. The app will start in listening mode with the wake word activated. The default wake word is "oracle," but you can modify it in the script.
4. When you say the wake word, the bot is ready to answer your question.
5. After answering your question, the conversation is stored in an ongoing JSON file, and the app returns to its initial state.
6. Both audio from the user and the bot are also stored as separate individual WAV files for each question and response.

## Changing Modes

To deactivate the wake word mode:

1. Use the wake word ("oracle").
2. Say "deactivate".
3. This changes the mode to "Always Listening."
4. In this mode, the wake word is disabled, and every question or statement receives a bot response.
5. The user can listen to bot responses related to the dialog around them.
6. To switch back to wake word mode, say "activate," and the mode will revert to its initial state with the wake word enabled.

## Code Explanation

This code implements a voice-controlled AI assistant with wake word functionality and introduces the capability to control the wake word mode dynamically.

### Defining the Wake Word and Wake Word Mode Control Commands

- `WAKE_WORD = "oracle"`: Specifies the wake word that triggers the assistant.
- `DISABLE_WAKE_WORD_COMMAND = "deactivate"`: Defines the command to disable wake word mode.
- `ENABLE_WAKE_WORD_COMMAND = "activate"`: Defines the command to enable wake word mode.

### Initializing the Wake Word Mode

- `wake_word_mode = True`: Keeps track of whether the assistant is currently in wake word mode or not.

### Modifying the Main Loop

The main loop is split into two parts to handle wake word mode and non-wake word mode separately.

In wake word mode:

- If the wake word is detected using `listen_for_wake_word()`, the assistant proceeds to listen for a user prompt using `listen()`.
- If the prompt is not None, it checks if the user has issued the command to disable wake word mode.
- If so, it disables wake word mode and continues listening for the wake word.
- If the prompt is not a wake word mode control command, it generates a response and handles it as before.

In non-wake word mode:

- The assistant listens for a user prompt using `listen()` without checking for the wake word.
- If the prompt is not None, it checks if the user has issued the command to enable wake word mode.
- If so, it enables wake word mode and continues listening for the wake word.
- If the prompt is not a wake word mode control command, it generates a response and handles it as before.

By introducing wake word mode control commands, users can dynamically enable or disable the wake word functionality based on their preferences. This provides greater flexibility in how the assistant operates.
