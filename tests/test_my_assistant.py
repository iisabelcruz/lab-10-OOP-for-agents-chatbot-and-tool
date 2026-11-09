from mock_model import MockModel
from my_assistant import AppointmentAssistant
from my_tool import AppointmentBook


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        """Return None to indicate no answer is available."""
        return


def make_assistant():
    """Build a fresh assistant with its own tool for each test."""
    book = AppointmentBook({"monday": "9:00 am and 2:30 pm", "friday": "none"})
    return AppointmentAssistant("Jim", "Be clear.", book, MockModel())


def test_open_times_question_uses_the_tool():
    assistant = make_assistant()
    reply = assistant.respond("What times are open on Monday?")
    assert reply == "Open times on monday: 9:00 am and 2:30 pm."


def test_question_without_a_known_day_asks_for_one():
    assistant = make_assistant()
    assert "Which day are you interested in?" in assistant.respond(
        "What times are open on Sunday?"
    )


def test_booking_request_goes_to_a_human():
    assistant = make_assistant()
    assert "front desk" in assistant.respond("Please book me for Monday at 9")


def test_unknown_request_gets_a_safe_reply():
    book = AppointmentBook({"monday": "9:00 am and 2:30 pm", "friday": "none"})
    assistant = AppointmentAssistant("Jim", "Be clear.", book, SilentModel())
    assert "try again" in assistant.respond("What is you favorite snack?")


def test_history_grows_by_two_each_turn():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What is open on Friday?")
    assert len(assistant.history) == 4


def test_other_messages_go_to_the_model():
    assistant = make_assistant()
    assert assistant.respond("hello") == "Hello! How can I assist you today?"
