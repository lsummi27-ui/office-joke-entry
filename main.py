"""Office Jokes entry: writes one office joke to /output/entry.txt."""
import os

JOKE = "My boss asked why I was late. I said traffic. He said, 'You work from home.' I said, 'Exactly.'"

assert 1 <= len(JOKE) <= 199, f"joke must be 1-199 chars, got {len(JOKE)}"
assert "\n" not in JOKE, "joke must be a single line"
assert JOKE.strip() == JOKE, "joke must not start or end with whitespace"
# 95 chars, one line: setup (late + traffic) then the remote-work twist.

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
