def print_custom(text, color=35, border=True):
    """
    Prints formatted text to the terminal using ANSI escape codes.

    Args:
        text (str): The text to be printed.
        color (int, optional): The ANSI escape code for the text color. Defaults to 35 (magenta).
        border (bool, optional): Whether to add a border to the output. Defaults to True.

    Returns:
        None

    Raises:
        None

    Examples:
        print_custom("Hello, world!", color=32)  # Green text
        print_custom("Important message", border=True) # Magenta text with border.
    """
    width = 45
    color_code = f"\033[{color}m"
    reset_code = "\033[0m"
    formatted_text = f"{color_code}{text:^{42}}{reset_code}"
    border_line = "\n" + ('=' * width) if border else ""
    return print(formatted_text + border_line)