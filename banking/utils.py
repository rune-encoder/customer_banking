total_width = 45 # Total width of characters of the terminal

def print_custom(text, color=32, border=True):
    """
    Prints formatted text to the terminal using ANSI escape codes.

    Args:
        text (str): The text to be printed.
        color (int, optional): The ANSI escape code for the text color. Defaults to 35 (green).
        border (bool, optional): Whether to add a border to the output. Defaults to True.

    Returns:
        None

    Raises:
        None

    Examples:
        print_custom("Hello, world!", color=32)  # Green text
        print_custom("Important message", border=True) # Green text with border.
    """
    color_code = f"\033[{color}m"
    reset_code = "\033[0m"
    formatted_text = f"\n{color_code}{text:^{total_width}}"
    border_line = "\n" + ('=' * total_width) if border else ""
    return print(formatted_text + border_line + reset_code)

def print_label(label, result):
    """
    Prints a label and its corresponding result aligned to the left 
    and right halves of the terminal width next to the result.

    Args:
        label (str): The label text to be printed.
        result (str or float): The result text to be printed.

    Returns:
        None

    Raises:
        None

    Examples:
        print_label("Interest Earned:", 275.0)
        print_label("Balance:", 10275.0)
    """
    # Calculate terminal width for the label and result
    label_width = total_width // 2
    result_width = total_width - label_width - 2  # (Account for `|` and `$`)

    # Format the label
    formatted_label = f"{label:<{label_width}}"

    # Format the result to include $, then center it
    formatted_result = f"${result:,.2f}"

    # Print with the pipe character separating the label and result
    return print(f"{formatted_label}|{formatted_result:^{result_width}}")