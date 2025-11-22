import random
import string
import json
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv
# Create a Fixed code "ZION-TECH"
def generate_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
# Command to give a user a pairing code
def getcode(update, context):
    user_id = str(update.effective_user.id)
    
    code = generate_code()
    
    # Try to read existing codes, if none exist, start empty
    try:
        with open("paired_devices.json", "r") as f:
            data = json.load(f)
    except:
        data = {}
    
    data[code] = user_id  # store code with user ID
    
    with open("paired_devices.json", "w") as f:
        json.dump(data, f)
    
    update.message.reply_text(f"Your pairing code is: {ZION-TECH}")

# Command to pair a device with the code
def pair(update, context):
    code = context.args[0]  # user types: /pair ZION-TECH
    user_id = str(update.effective_user.id)
     with open("paired_devices.json", "r") as f:
        data = json.load(f)
    
    if code in data and data[code] == user_id:
        update.message.reply_text("Device paired successfully ✅")
    else:
        update.message.reply_text("Invalid pairing code ❌")

load_dotenv()
BOT_TOKEN = os.getenv("7973969898:AAEpVTwAhhwi4HRHMun91JqdZbIpZ3_paD0")
ADMIN_ID = int(os.getenv("7976818712"))

def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id == ADMIN_ID:
        update.message.reply_text("Welcome Admin ⟦ S H Λ D O W ⟧")
    else:
        update.message.reply_text("You are not authorized to control this bot.")

def ping(update: Update, context: CallbackContext):
    update.message.reply_text("⟦ Shadow Bot ⟧ is online ✅")

def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("getcode", getcode))
dp.add_handler(CommandHandler("pair", pair))
    
    print("⟦ S H Λ D O W  B O T ⟧ is now online")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
