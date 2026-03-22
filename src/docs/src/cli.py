# cli.py
# simple command-line interface for paradigm

from app import main
from config import DEBUG

def run():
    if DEBUG:
        print("[DEBUG] CLI invoked")

    print("=== paradigm CLI ===")
    main()

if __name__ == "__main__":
    run()
