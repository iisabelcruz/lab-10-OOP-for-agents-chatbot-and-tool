from my_assistant import AppointmentAssistant
from my_tool import AppointmentBook


def make_assistant():
    """Build a fresh assistant with its own tool for each test."""
    book = AppointmentBook({"monday": "9:00 am and 2:30 pm", "friday": "none"})
    return AppointmentAssistant("Jim", "Be clear.", book)


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
    assistant = make_assistant()
    assert "not sure" in assistant.respond("What is your favorite color?")


def test_history_grows_by_two_each_turn():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What is open on Friday?")
    assert len(assistant.history) == 4
