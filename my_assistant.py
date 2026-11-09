# my_assistant.py
# Author: [Your Name]

HANDOFF_WORDS = ["book", "cancel", "reschedule"]


class AppointmentAssistant:
    """A mock appointment assistant. Its replies come from simple rules, not from AI."""

    def __init__(self, name, instructions, appointment_book, model):
        """Set up one assistant with its own name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.appointment_book = appointment_book
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply with keyword rules. This is the mock part."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I am unable to change the schedule on my end, I will pass you onto the front desk."
        if "open" in text or "available" in text:
            return self.times_reply(user_message)
        return self.model_reply()

    def model_reply(self):
        """Ask the model for a reply. Give a safe answer if the mode has none."""
        reply = self.model.reply(self.instructions, self.history)
        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."
        return reply

    def needs_human(self, text):
        """Return True if the message asks to change the schedule."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def times_reply(self, user_message):
        """Use the appointment book to answer a question about open times."""
        day = self.appointment_book.find_day(user_message)
        if day is None:
            return "Which day are you interested in? I can check Monday, Tuesday, Wednesday, Thursday, or Friday."
        times = self.appointment_book.times_for(day)
        return f"Open times on {day}: {times}."
