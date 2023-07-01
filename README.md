# Voice Controlled AI Assistant
Voice Controlled AI Assistant with wake word on/off (uses ChatGPT engine="text-davinci-003" which can be modified)
This is an early stage proof of concept that will eventually be a mobile app that the user can use to listen to bot responses pertaining to the voices and dialog around them.  
# How to Use
Enter your OPEN AI API key in the .env file <br>
Run Voice_Enabled_AI_Assistant.py <br>
The app will start in a listening mode with wake word activated.  The wake word is "oracle" but can be modified in the script.  When you say the wake word, the bot is ready for your question.  After answering your question, the conversation is stored in an ongoing json file, and the app returns to it's initial state.  Both audio from you and the bot are also stored as seperate individual wav files for each question & response. 
# Changing Modes
To deactivate the wake word mode, you use the wake word (in this case "oracle") and then say "deactivate".  This will change the mode to be "Always Listening".  In this mode, wake word is disabled and every question or statement will get a bot response in return.  In this mode, the user could listen to bot responses to the dialog around them.  
# Code explanation:
This code implements a voice-controlled AI assistant with wake word functionality. It introduces the capability to control the wake word mode dynamically.

Defining the Wake Word and Wake Word Mode Control Commands
WAKE_WORD = "oracle": Specifies the wake word that triggers the assistant.
DISABLE_WAKE_WORD_COMMAND = "deactivate": Defines the command to disable wake word mode.
ENABLE_WAKE_WORD_COMMAND = "activate": Defines the command to enable wake word mode.
Initializing the Wake Word Mode
wake_word_mode = True: Keeps track of whether the assistant is currently in wake word mode or not.
Modifying the Main Loop
The main loop is split into two parts to handle wake word mode and non-wake word mode separately.

In wake word mode:

If the wake word is detected using listen_for_wake_word(), the assistant proceeds to listen for a user prompt using listen().
If the prompt is not None, it checks if the user has issued the command to disable wake word mode.
If so, it disables wake word mode and continues listening for the wake word.
If the prompt is not a wake word mode control command, it generates a response and handles it as before.
In non-wake word mode:

The assistant listens for a user prompt using listen() without checking for the wake word.
If the prompt is not None, it checks if the user has issued the command to enable wake word mode.
If so, it enables wake word mode and continues listening for the wake word.
If the prompt is not a wake word mode control command, it generates a response and handles it as before.
By introducing wake word mode control commands, the user can dynamically enable or disable the wake word functionality based on their preference. This provides greater flexibility in how the assistant operates.
