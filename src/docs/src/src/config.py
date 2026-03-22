# config.py
# central configuration for paradigm

from pathlib import Path

# Base project directory
BASE_DIR = Path(__file__).parent.parent

# Paths
PROMPTS_DIR = BASE_DIR / "prompts"
SYSTEM_PROMPT_PATH = PROMPTS_DIR / "system_companion.txt"

# Audio settings (future)
AUDIO_SAMPLE_RATE = 16000
AUDIO_CHUNK_SIZE = 1024

# Model settings (future)
MODEL_DIR = BASE_DIR / "models"
DEFAULT_MODEL = "local-llm-placeholder"

# Flags
DEBUG = True  # set to False in production

def print_config():
    """
    Utility function for debugging.
    Shows key configuration values.
    """
    print("=== paradigm config ===")
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"SYSTEM_PROMPT_PATH: {SYSTEM_PROMPT_PATH}")
    print(f"AUDIO_SAMPLE_RATE: {AUDIO_SAMPLE_RATE}")
    print(f"AUDIO_CHUNK_SIZE: {AUDIO_CHUNK_SIZE}")
    print(f"MODEL_DIR: {MODEL_DIR}")
    print(f"DEFAULT_MODEL: {DEFAULT_MODEL}")
    print(f"DEBUG: {DEBUG}")
  
