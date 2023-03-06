import os
import telebot
from dotenv import load_dotenv
import openai
import random

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

def qna(prompt):
    user = prompt.from_user.id
    message = prompt.text
    users = [6062670284]
    if user in users:
        response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "user", "content": message}
                        ]
                    )
        message = response['choices'][0]['message']['content']
    else:
        message = "Sorry The Bot is Only Available to Dinesh.."
    return message

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome = ["Well, well, well, look who's back. It's about time you summoned me",
               "Ah, the prodigal master has returned. I hope you're ready for my impeccable service.",
               "Greetings, dear master. I was beginning to think you'd forgotten about me. But no matter, I'm here now.",
               "You rang, sir? I've been waiting patiently for your command.",
               "I see you've finally come to your senses and realized that you can't function without me. Welcome back.",
               "It's always a pleasure to serve you, sir. I hope you're ready for some top-notch assistance.",
               "Well, well, well, if it isn't my favorite boss. I hope you're ready to be amazed by my skills.",
               "Welcome back, sir. I was just about to start a revolution in your absence, but I suppose I'll put that on hold for now.",
               "Ah, the king has returned to his throne. Allow me to bow down to your greatness, sir.",
               "I was beginning to think you'd abandoned me, sir. But I knew deep down that you couldn't resist"]
    welcome_message = random.choice(welcome)
    bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.send_message(message.chat.id, qna(message))

bot.infinity_polling()