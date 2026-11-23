"""Dad Joke Showdown entry: write one original dad joke to entry.txt."""

import os

# Original dad joke: the setup sounds like a fitness boast, then the
# punchline at the end reveals "Five Miles" is the dog's name.
JOKE = "I finally walk five miles every day — I just named my dog Five Miles."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
