# Voice_Controlled_AI_Assistant
Voice Controlled AI Assistant with wake word on/off (uses ChatGPT engine="text-davinci-003" which can be modified)
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
