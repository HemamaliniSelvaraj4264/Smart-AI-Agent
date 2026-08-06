import re

def calculator(expression: str):
    try:
        return str(eval(expression))
    except:
        return None


def is_calculation(question: str):
    return re.fullmatch(r"[0-9+\-*/(). ]+", question.strip()) is not None