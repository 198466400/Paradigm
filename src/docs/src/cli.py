# cli.py
# simple command-line interface for paradigm

from app import main

def run():
    """
    Entry point for running paradigm from the command line.
    """
    print("=== paradigm CLI ===")
    main()

if __name__ == "__main__":
    run()
