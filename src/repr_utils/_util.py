def indent_each_line(text: str, indent: int = 4):
    indentation = " " * indent
    return "\n".join([f"{indentation}{line}" for line in text.split("\n")])
