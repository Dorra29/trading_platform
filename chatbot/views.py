from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import openai
import os
import requests


chat_memory = {}

openai.api_key = os.getenv("OPENAI_API_KEY")

@login_required
@csrf_exempt
def chatbot_view(request):
    user = request.user
    chat_history = chat_memory.get(user.username, [])

    if request.method == "GET":
        return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\chatbot.html') 

    if request.method == 'POST':
        user_input = request.POST.get('message', '')

        try:
            messages = [
                {"role": "system", "content": "You're a Gen Z trading assistant helping Tunisian users make smart trading moves."},
                {"role": "user", "content": user_input}
            ]

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages
            )

            bot_reply = response.choices[0].message.content.strip()

            # Save the last 5 messages in memory
            chat_history.append({
                "user_message": user_input,
                "bot_reply": bot_reply
            })
            chat_memory[user.username] = chat_history[-5:]

        except Exception as e:
            bot_reply = "⚠️ Sorry, something went wrong with the chatbot."

            chat_history.append({
                "user_message": user_input,
                "bot_reply": bot_reply
            })
            chat_memory[user.username] = chat_history[-5:]

    return render(request, 'C:\\Users\\DEll\\Desktop\\possiblypfe\\blog\\templates\\chatbot.html', {
        "chat_history": chat_history,
        "user": user,
        "virtual_balance": 10000,     # or get from database
        "trade_history": [],          # optional for now
    })

def chatbot_personality_view(request):
    message = request.GET.get("message")
    personality = request.GET.get("personality", "gen_z")

    bot_reply = None

    if message:
        payload = {
            "sender": "user123",
            "message": f"{message} [{personality}]"
        }
        try:
            response = requests.post(
                "http://localhost:5005/webhooks/rest/webhook",
                json=payload
            )
            data = response.json()
            if data and "text" in data[0]:
                bot_reply = data[0]["text"]
        except Exception as e:
            bot_reply = f"⚠️ Could not reach the Rasa server: {str(e)}"

    return render(request, "chatbot.html", {
        "bot_reply": bot_reply,
        "user_message": message,
        "selected_personality": personality
    })