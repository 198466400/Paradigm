# companion_core.py
# placeholder for paradigm's grounding + reflective AI behavior

from config import SYSTEM_PROMPT_PATH, DEBUG

def load_system_prompt():
    """
    Loads the system_companion.txt behavior contract.
    """
    if not SYSTEM_PROMPT_PATH.exists():
        return "system_companion.txt not found."

    if DEBUG:
        print(f"[DEBUG] Loading system prompt from: {SYSTEM_PROMPT_PATH}")

    return SYSTEM_PROMPT_PATH.read_text()


def generate_response(user_text):
    """
    Placeholder for generating a grounding, reflective response.
    """
    system_prompt = load_system_prompt()

    if DEBUG:
        print("[DEBUG] generate_response() called")

    return (
        "paradigm core online.\n"
        "Behavior contract loaded.\n"
        "Full response generation coming soon."
    )


if __name__ == "__main__":
    print(generate_response("test input"))
    
