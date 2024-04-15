import requests
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HALLS_API_URL = os.getenv("HALLS_API_URL")  

TOKEN = "YOUR_BOT_TOKEN"

# Replace with the actual URL of your Flask app (once deployed)
HALLS_API_URL = "YOUR_FLASK_APP_URL"

def get_halls():
    """Fetches data about halls from the Flask app."""
    response = requests.get(HALLS_API_URL)
    return response.json()["halls"]

def get_hall_details(hall_name):
    """Retrieves details of a specific hall."""
    halls = get_halls()
    for hall in halls:
        if hall_names_match(hall["names"], hall_name):
            return hall
    return None

def hall_names_match(hall_names, user_input):
    """Checks if any of the hall names (including aliases) match the user's input."""
    for name in hall_names:
        if name.lower() == user_input.lower():
            return True
    return False

def format_hall_info(hall):
    """Formats hall information for a clear Telegram message."""
    message = f"**Hall:** {hall['names'][0]}\n"
    if len(hall["names"]) > 1:
        message += f"  (Aliases: {', '.join(hall['names'][1:])})\n"
    message += f"**Picture:** {hall['picture']}\n"
    return message

def create_navigation_markup(hall_coordinates):
    """Generates a Telegram button for opening Google Maps navigation."""
    latitude = hall_coordinates["latitude"]
    longitude = hall_coordinates["longitude"]
    navigation_url = f"https://www.google.com/maps?dir=my+location+{latitude},{longitude}"
    button = KeyboardButton("Navigate on Maps", url=navigation_url)
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard.add(button)
    return keyboard

def handle_start(update: Update, context: CallbackQueryHandler):
    """Welcomes the user and prompts for hall information."""
    update.effective_chat.send_message(
        text="Hi! I can provide information about halls and help you navigate to them.\n"
             "Type the name of a hall to get details or 'list halls' to see all halls.",
        reply_markup=ForceReply(selective=False),
    )

def handle_list_halls(update: Update, context: CallbackQueryHandler):
    """Sends a list of all hall names
