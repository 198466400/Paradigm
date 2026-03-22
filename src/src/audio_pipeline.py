# audio_pipeline.py
# placeholder for paradigm's audio → text → response flow

from config import AUDIO_SAMPLE_RATE, AUDIO_CHUNK_SIZE, DEBUG

def capture_audio():
    """
    Placeholder function for capturing microphone audio.
    """
    if DEBUG:
        print(f"[DEBUG] capture_audio() called — sample_rate={AUDIO_SAMPLE_RATE}, chunk={AUDIO_CHUNK_SIZE}")

    print("capture_audio() called - audio pipeline not implemented yet.")
    return None


def transcribe_audio(audio_data):
    """
    Placeholder for local speech-to-text.
    """
    if DEBUG:
        print("[DEBUG] transcribe_audio() called")

    print("transcribe_audio() called - STT not implemented yet.")
    return ""


def process_input_text(text):
    """
    Placeholder for sending text to the companion core.
    """
    if DEBUG:
        print("[DEBUG] process_input_text() called")

    print("process_input_text() called - AI core not implemented yet.")
    return "paradigm is not fully online yet, but the pipeline is taking shape."


def run_pipeline():
    """
    High-level placeholder for the full flow:
    audio → text → response
    """
    if DEBUG:
        print("[DEBUG] run_pipeline() starting")

    audio = capture_audio()
    text = transcribe_audio(audio)
    response = process_input_text(text)

    if DEBUG:
        print("[DEBUG] run_pipeline() finished")

    return response


if __name__ == "__main__":
    print(run_pipeline())
