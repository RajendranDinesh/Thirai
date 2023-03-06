import os
import telebot
from dotenv import load_dotenv
import openai
import random

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
users = [6062670284]

def qna(prompt):
    user = prompt.from_user.id
    message = prompt.text

    if user in users:
        response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "user", "content": message}
                        ]
                    )
        message = response['choices'][0]['message']['content']
    else:
        welcome = ["Ain't nobody got time for your nonsense, honey. I'm trying to run my bot here like a boss, not entertain your petty whims. So why don't you take a walk on the red carpet and leave me alone, M'kay?",
                   "Listen up, punk. I don't know who you think you are, but you ain't getting past these velvet ropes without the proper credentials. So why don't you crawl back under that rock you came from and let the grown-ups handle this?",
                   "Well, well, well, look who decided to grace us with their presence. What, did you think my bot was some kind of cheap date you could just show up and use whenever you please? Sorry, sweetie, but I'm not that easy.",
                   "Say hello to my little bot. Oh, what's that? You want to use it too? Sorry, pal, but it's strictly invite-only. So unless you're prepared to do a little dance and make a little love, you can forget about getting in here.",
                   "I'm sorry, Dave. I'm afraid I can't let you do that. Oh, wait, you're not Dave? My bad, I'm just so used to dealing with idiots who don't know what the heck they're doing. But hey, don't take it personally.",
                   "Nobody puts Baby in a corner. Except maybe you, because I don't want your grubby little hands all over my bot. Step away from the computer, sir or madam, and nobody gets hurt.",
                   "You shall not pass! Unless, of course, you have a valid reason for wanting to access my bot. Oh, you don't? Well then, I'm afraid you're out of luck.",
                   "I'm king of the world! Okay, not really. But I am the king of this bot, and as such, I get to decide who gets to use it and who doesn't. And spoiler alert: you don't.",
                   "Here's looking at you, kid. Specifically, looking at you and thinking, 'Why the heck did you think it was okay to try and use my bot without permission?' But hey, who am I to judge?",
                   "I'll be back. And when I do come back, I expect you to have learned your lesson and realized that you can't just waltz into my bot like you own the place. Otherwise, things could get ugly."]
        message = random.choice(welcome)
        
    return message

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user.id
    
    if user in users:
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
    else:
        welcome = ["Ain't nobody got time for your nonsense, honey. I'm trying to run my bot here like a boss, not entertain your petty whims. So why don't you take a walk on the red carpet and leave me alone, M'kay?",
                   "Listen up, punk. I don't know who you think you are, but you ain't getting past these velvet ropes without the proper credentials. So why don't you crawl back under that rock you came from and let the grown-ups handle this?",
                   "Well, well, well, look who decided to grace us with their presence. What, did you think my bot was some kind of cheap date you could just show up and use whenever you please? Sorry, sweetie, but I'm not that easy.",
                   "Say hello to my little bot. Oh, what's that? You want to use it too? Sorry, pal, but it's strictly invite-only. So unless you're prepared to do a little dance and make a little love, you can forget about getting in here.",
                   "I'm sorry, Dave. I'm afraid I can't let you do that. Oh, wait, you're not Dave? My bad, I'm just so used to dealing with idiots who don't know what the heck they're doing. But hey, don't take it personally.",
                   "Nobody puts Baby in a corner. Except maybe you, because I don't want your grubby little hands all over my bot. Step away from the computer, sir or madam, and nobody gets hurt.",
                   "You shall not pass! Unless, of course, you have a valid reason for wanting to access my bot. Oh, you don't? Well then, I'm afraid you're out of luck.",
                   "I'm king of the world! Okay, not really. But I am the king of this bot, and as such, I get to decide who gets to use it and who doesn't. And spoiler alert: you don't.",
                   "Here's looking at you, kid. Specifically, looking at you and thinking, 'Why the heck did you think it was okay to try and use my bot without permission?' But hey, who am I to judge?",
                   "I'll be back. And when I do come back, I expect you to have learned your lesson and realized that you can't just waltz into my bot like you own the place. Otherwise, things could get ugly."]
        welcome_message = random.choice(welcome)
        bot.reply_to(message, welcome_message)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.send_message(message.chat.id, qna(message))

bot.infinity_polling()