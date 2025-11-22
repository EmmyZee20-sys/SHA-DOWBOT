import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

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
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))
    
    print("⟦ S H Λ D O W  B O T ⟧ is now online")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
