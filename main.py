"""Entry for make.fun bounty: u-kreutzx-the-funniest-out-of-office-054815cf.

Writes one text (1-140 characters) to /output/entry.txt. The text below is the entry.
"""
import os

TEXT = "Out of office until Monday. All meetings in my absence will be held, as scheduled, about this."


def write_entry(text, limit):
    text = text.strip()
    assert 1 <= len(text) <= limit, f"length {len(text)} outside the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {len(text)} characters")


write_entry(TEXT, 140)
