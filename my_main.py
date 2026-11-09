# appointment_main.py
# Author: Isabel Cruz

from my_assistant import AppointmentAssistant
from my_tool import AppointmentBook
from ollama_model import OllamaModel

OPEN_TIMES = {
    "monday": "9:00 am and 2:30 pm",
    "tuesday": "10:00 am",
    "wednesday": "11:00 am",
    "thursday": "1:00 pm",
    "friday": "none",
}

INSTRUCTIONS = """You are Jim, an assistant for the Kendall Clinic Center. Answer in one short sentence.
The office is at 224 Sunset Drive, on the the thrid floor.
Bring a photo ID and your insurance card to your appointment.
Only stste facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the client to the front desk."""

appointment_book = AppointmentBook(OPEN_TIMES)
model = OllamaModel("granite4.1:3b")
assistant = AppointmentAssistant("Jim", INSTRUCTIONS, appointment_book, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
