"""Entry for make.fun bounty: u-kreutzx-the-funniest-out-of-office-054815cf.

Writes one text (1-140 characters) to /output/entry.txt.
No network. Deterministic: the text below IS the entry.
"""
import os

TEXT = """Out of office until Monday. All meetings in my absence will be held, as scheduled, about this."""


def main():
    os.makedirs("/output", exist_ok=True)
    text = TEXT.strip()
    n = len(text)
    assert 1 <= n <= 140, f"length {n} outside the gate"
    assert text.strip(), "text is only white space"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {n} characters")


if __name__ == "__main__":
    main()
