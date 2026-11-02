# appointment_main.py
# Author: [Your Name]

from my_assistant import AppointmentAssistant
from my_tool import AppointmentBook

OPEN_TIMES = {
    "monday": "9:00 am and 2:30 pm",
    "tuesday": "10:00 am",
    "wednesday": "11:00 am",
    "thursday": "1:00 pm",
    "friday": "none",
}

appointment_book = AppointmentBook(OPEN_TIMES)
assistant = AppointmentAssistant(
    "Jim",
    "You help patients of Kendall Clinic Center find an open appointment time.",
    appointment_book,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
