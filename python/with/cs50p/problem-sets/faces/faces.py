def converter(text: str = None):
    if text is None or text.strip() == "":
        raise ValueError("Missing text!")

    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text


print(converter("hello :):(:)"))
