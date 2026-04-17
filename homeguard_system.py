def respond_to_radio_check(message: str) -> str:
    """Return an acknowledgement to a radio-check style message."""
    normalized = message.strip().lower()
    if normalized == "прием. слышно меня?":
        return "Да, слышно."
    return "Сообщение получено."


if __name__ == "__main__":
    print(respond_to_radio_check("прием. слышно меня?"))
