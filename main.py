import os

# The compass: an agent takes a goal and finds the way through it on
# your behalf. It navigates, decides the next turn, and keeps you on
# course while you look elsewhere. Not a robot face, not a smiley:
# a tool for finding direction, which is what the agent actually does.
ENTRY = "\U0001F9ED"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
