from transformers import pipeline

# Load a local text generation pipeline
generator = pipeline("text-generation", model="distilgpt2")

def polish_response_hf(base_response):
    """
    Takes a base response decided by our system logic
    and rewrites it in a warm, empathetic tone.
    """

    prompt = (
        "Rewrite the following text so it sounds calm, warm, "
        "and empathetic. Do NOT give advice. "
        "Do NOT add new information.\n\n"
        f"Text: {base_response}\n\nRewritten: "
    )

    result = generator(
        prompt,
        max_length=150,
        num_return_sequences=1,
        temperature=0.6,
        do_sample=True
    )

    # Extract the generated text and remove the prompt
    generated = result[0]["generated_text"]
    output = generated.replace(prompt, "").strip()
    
    return output if output else base_response
