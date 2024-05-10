import telebot
from telebot import types
import time
import time
import json
import telebot
import requests
from telebot import types
#database

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot("6925014810:AAGrl21g16l3mDIrwbgnojWEcIqBwn0K90s")

CHANNEL_ID = -1002059043048

CHANNEL_ID2 = -1002034696352

CHANNEL_ID3 = -1001860294823
CHANNEL_ID4 = -1001711008160
CHANNEL_USERNAME = 'Dream99_VIP_Hub'
CHANNEL_USERNAME3 = 'Earn_Money_PayTM_UPI'
CHANNEL_USERNAME2 = 'PrivateLoot'
CHANNEL_USERNAME4 = "Official_InstaPLUS"
#database end
def get_admin_ids(bot, chat_id):
    """
    Returns a list of admin IDs for a given chat.
    """
    try:
        return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]
    except Exception as e:
        print(f"Error getting admin IDs: {e}")
        return []


successful_messages = 0
failed_messages = 0

try:
    with open("user_ids.json", "r") as f:
        user_ids = set(json.load(f))
except FileNotFoundError:
    user_ids = set()

# Handle /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    global user_ids
    try:
        # Check if the user is a member of all specified channels
        is_member_channel1 = bot.get_chat_member(CHANNEL_ID, message.from_user.id).status in ['member', 'administrator']
        is_member_channel2 = bot.get_chat_member(CHANNEL_ID2, message.from_user.id).status in ['member', 'administrator']
        is_member_channel3 = bot.get_chat_member(CHANNEL_ID3, message.from_user.id).status in ['member', 'administrator']
        is_member_channel4 = bot.get_chat_member(CHANNEL_ID4, message.from_user.id).status in ['member', 'administrator']
      #  is_member_channel5 = bot.get_chat_member(CHANNEL_ID5, message.from_user.id).status in ['member', 'administrator']
        
        # Check if the user is a member of all specified channels
        if is_member_channel1 and is_member_channel2 and is_member_channel3 and is_member_channel4:
            # Add the new user ID to the set and save it to the JSON file
            user_ids.add(message.chat.id)
            with open("user_ids.json", "w") as f:
                json.dump(list(user_ids), f)
            bot.send_message(message.chat.id,
                             "ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ url remover ʙᴏᴛ!\n\n"
                             "for use me just add me admin in your group\n"
                             "then see my magic 🪄 i am remove urls from your group\n\n")
        else:
            # Prompt user to join all channels and provide buttons with links to the channels
            join_message = f"You are not a member of all our channels. Please join to access this feature."
            
            markup = types.InlineKeyboardMarkup()
            join_button1 = types.InlineKeyboardButton("ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 1", url=f"https://t.me/{CHANNEL_USERNAME}")
            join_button2 = types.InlineKeyboardButton("ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 2", url=f"https://t.me/{CHANNEL_USERNAME2}")
            join_button3 = types.InlineKeyboardButton("ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 3", url=f"https://t.me/{CHANNEL_USERNAME3}")
            join_button4 = types.InlineKeyboardButton("ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 4", url=f"https://t.me/{CHANNEL_USERNAME4}")
         #   join_button5 = types.InlineKeyboardButton("ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 5", url=f"https://t.me/{CHANNEL_USERNAME5}")
            
            markup.add(join_button1, join_button2)
            markup.add(join_button3, join_button4)
            
            bot.reply_to(message, join_message, reply_markup=markup)
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")
        



	                     
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # Get the list of admin IDs
        admin_ids = get_admin_ids(bot, message.chat.id)
        
        # Check if the message contains a URL
        if "http" in message.text:
            # Check if the sender is an admin
            if message.from_user.id not in admin_ids:
                # Delete the message if it's from a regular user
                bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
                # Optionally, you can notify the user that their message was deleted
                bot.send_message(chat_id=message.chat.id, text="Sorry, URLs are not allowed in this group.")
            else:
                # Admin URLs are allowed, so do nothing
                pass
    except Exception as e:
        print(f"Error handling message: {e}")

#while True:
    #try:
        #bot.polling(none_stop=True)
    #except Exception as e:
        #print(f"Bot polling error: {e}")
        #time.sleep(5)  # Wait for 15 seconds before restarting the bot
bot.polling()
        