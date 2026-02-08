from django.shortcuts import render
from .logic import detect_emotion_and_risk, select_strategy, generate_response, use_emotional_memory
from .ai_hf import polish_response_hf as polish_response


def chat_view(request):
    response = ""
    user_message = ""

    if request.method == "POST":
        user_message = request.POST.get("message")

        emotion, risk = detect_emotion_and_risk(user_message)

        previous_emotion = request.session.get("emotion")
        request.session["emotion"] = emotion

        memory_response = use_emotional_memory(emotion, previous_emotion)

        strategy = select_strategy(emotion, risk)
        response = generate_response(emotion, strategy)
        response = polish_response(response)


        if memory_response:
            response = memory_response + " " + response

    return render(request, "chat.html", {
        "response": response,
        "user_message": user_message
    })

