from huggingface_hub import InferenceClient

client = InferenceClient()

def polish_response_hf(base_response):
    prompt = (
        "Rephrase this to sound warm and empathetic, "
        "NOT giving advice:\n\n"
        f"{base_response}"
    )

    output = client.text_generation(
        model="gpt2",     # free model
        prompt=prompt,
        max_length=150
    )

    return output
