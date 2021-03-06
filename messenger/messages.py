########################################################################
# COMPONENT:
#    MESSAGES
# Author:
#    Br. Helfrich, Kyle Mueller, Joshua Bee
# Summary: 
#    This class stores the notion of a collection of messages
########################################################################

import control, message

##################################################
# MESSAGES
# The collection of high-tech messages
##################################################
class Messages:

    ##################################################
    # MESSAGES CONSTRUCTOR
    # Read a file to fill the messages
    ##################################################
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    ##################################################
    # MESSAGES :: DISPLAY
    # Display the list of messages
    ################################################## 
    def display(self, clearance):
        for m in self._messages:
            m.display_properties(clearance)

    ##################################################
    # MESSAGES :: SHOW
    # Show a single message
    ################################################## 
    def show(self, id, clearance):
        for m in self._messages:
            if m.get_id() == id:
                if control.security_condition_read(clearance, m.get_clearance_m()):
                    m.display_text()
                else:
                    print(f"ERROR! Insufficient clearance to read.")
                return True
        return False

    ##################################################
    # MESSAGES :: UPDATE
    # Update a single message
    ################################################## 
    def update(self, id, text, clearance):
        for m in self._messages:
            if m.get_id() == id:
                if control.security_condition_write(clearance, m.get_clearance_m()):
                    m.update_text(text)
                else:
                    print("ERROR! Improper clearance to update")
    ##################################################
    # MESSAGES :: REMOVE
    # Remove a single message
    ################################################## 
    def remove(self, id, clearance):
        for m in self._messages:
            if m.get_id() == id:
                if control.security_condition_write(clearance, m.get_clearance_m()):
                    m.clear()
                    return
                else:
                    print("ERROR! Improper clearance to remove")
                    return
        print("ERROR! ID not found")
    ##################################################
    # MESSAGES :: ADD
    # Add a new message
    ################################################## 
    def add(self, text, author, date, text_clearance):
        m = message.Message(text, author, date, text_clearance)
        self._messages.append(m)

    ##################################################
    # MESSAGES :: READ MESSAGES
    # Read messages from a file
    ################################################## 
    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text = line.split('|')
                    self.add(text.rstrip('\r\n'), author, date, text_control)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return
