import re
from typing import List

def _split_numbers(text: str, delimiters: List[str]) -> List[str]:
    pattern = "|".join(re.escape(d) for d in delimiters)
    return re.split(pattern, text)

def add(numbers: str) -> int:
    """
    Add numbers in a string using comma or newline as default delimiters.
    Supports a custom delimiter specified as: //[delimiter]\n[numbers...]
    Raises ValueError if there are negative numbers; lists all negatives in the message.
    """
    if numbers is None or numbers == "":
        return 0

    # Custom delimiter check
    custom_delim = None
    if numbers.startswith("//"):
        try:
            header, numbers = numbers.split("\n", 1)
            custom_delim = header[2:]
        except ValueError:
            custom_delim = None

    delimiters = [",", "\n"]
    if custom_delim:
        delimiters.append(custom_delim)

    tokens = _split_numbers(numbers, delimiters)
    ints, negatives = [], []
    for t in tokens:
        t = t.strip()
        if not t:
            continue
        n = int(t)
        if n < 0:
            negatives.append(n)
        ints.append(n)

    if negatives:
        negs_str = ",".join(map(str, negatives))
        raise ValueError(f"negative numbers not allowed {negs_str}")

    return sum(ints)
