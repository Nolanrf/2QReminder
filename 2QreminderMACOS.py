import subprocess

def notify(title, message):
    script = f'display notification "{message}" with title "{title}"'
    subprocess.run(["osascript", "-e", script])

if __name__ == "__main__":
    notify("Reminder", "1. How are you feeling currently? 2. What is one positive affirmation you need to hear right now?")
