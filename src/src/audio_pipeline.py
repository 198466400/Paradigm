# app.py
# main entry point for paradigm

from audio_pipeline import run_pipeline
from companion_core import generate_response
from config import DEBUG

def main():
    if DEBUG:
        print("[DEBUG] paradigm starting up...")

    print("paradigm starting up...\n")

    # Step 1: run the placeholder audio pipeline
    text = run_pipeline()

    # Step 2: send the text to the companion core
    response = generate_response(text)

    # Step 3: output the response
    print("\n--- paradigm response ---")
    print(response)
    print("-------------------------")


if __name__ == "__main__":
    main()
