from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import openai
import os
from .models import TradeSimulation 
import requests


chat_memory = {}

openai.api_key = os.getenv("OPENAI_API_KEY")

@login_required
@csrf_exempt
def chatbot_view(request):
    user = request.user
    chat_history = chat_memory.get(user.username, [])

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

    return render(request, "dashboard.html", {
        "chat_history": chat_history,
        "user": user,
        "virtual_balance": 10000,     # or get from database
        "trade_history": [],          # optional for now
    })
def simulate_trade(request):
    if request.method == 'POST':
        asset = request.POST.get('asset')
        side = request.POST.get('side')
        amount = request.POST.get('amount')

        # Simulate trade logic here (you can add more sophisticated logic if needed)
        # For now, let's just log the trade
        trade_price = 100  # You can fetch real prices from an API, for example

        # Create a new trade entry (you can save this to the database)
        trade = TradeSimulation.objects.create(
            user=request.user,
            asset=asset,
            side=side,
            amount=amount,
            price=trade_price
        )

        # Optionally, return a success message or redirect
        return render(request, 'dashboard.html', {
            'trade_history': [trade],  # Add the trade to the trade history display
            'virtual_balance': 10000,  # Update this dynamically if needed
        })

   
    return render(request, 'dashboard.html')
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