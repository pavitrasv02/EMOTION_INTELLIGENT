def detect_emotion_and_risk(user_message):
    msg = user_message.lower()

    if any(word in msg for word in ["die", "end it", "kill myself", "suicide"]):
        return "crisis", "high"

    if any(word in msg for word in ["alone", "lonely", "nobody cares"]):
        return "lonely", "medium"

    if any(word in msg for word in ["sad", "empty", "tired", "hopeless"]):
        return "sad", "medium"

    if any(word in msg for word in ["angry", "mad", "hate"]):
        return "angry", "low"

    return "neutral", "low"


def generate_response(emotion, strategy):
    if strategy == "escalate":
        return (
            "I’m really glad you told me this. You don’t have to go through this alone. "
            "If you can, please consider reaching out to someone you trust right now."
        )

    if strategy == "validate":
        return f"It sounds like you’re feeling {emotion}. That can be really hard. I’m here with you."

    if strategy == "ground":
        return "It sounds like there’s a lot of tension. Let’s pause for a breath together."

    return "I’m here. You can tell me more if you want."

def select_strategy(emotion, risk):
    if risk == "high":
        return "escalate"
    if emotion in ["sad", "lonely"]:
        return "validate"
    if emotion == "angry":
        return "ground"

    return "listen"

def use_emotional_memory(current_emotion, previous_emotion):
    if previous_emotion and current_emotion == previous_emotion:
        return f"You mentioned feeling {current_emotion} earlier too. I’m still here with you."
    return None

