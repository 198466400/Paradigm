# companion_core.py
# placeholder for paradigm's grounding + reflective AI behavior

from pathlib import Path

def load_system_prompt():
    """
    Loads the system_companion.txt behavior contract.
    In the future, this will:
    - read the prompt from prompts/system_companion.txt
    - feed it into the local model
    """
    prompt_path = Path(__file__).parent.parent / "prompts" / "system_companion.txt"

    if not prompt_path.exists():
        return "system_companion.txt not found."

    return prompt_path.read_text()


def generate_response(user_text):
    """
    Placeholder for generating a grounding, reflective response.
    Later, this will:
    - combine system prompt + user text
    - run through a local model
    - return a safe, supportive response
    """
    system_prompt = load_system_prompt()

    print("generate_response() called - AI model not implemented yet.")
    return (
        "paradigm core online.\n"
        "Behavior contract loaded.\n"
        "Full response generation coming soon."
    )


if __name__ == "__main__":
    print(generate_response("test input"))
  
