from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(name)

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    channel_id = '1001587577987'  # Replace with your actual channel ID
    user_id = update.effective_user.id
    
    # Check if the user is a member of the channel
    if context.bot.get_chat_member(channel_id, user_id).status == 'member':
        update.message.reply_text("Welcome to the bot! You are already a member of the channel.")
    else:
        update.message.reply_text(f"Join the channel to proceed: t.me/Technical_Robot")
        
# Define the message handler
def echo(update: Update, context: CallbackContext) -> None:
    channel_id = '1001587577987'  # Replace with your actual channel ID
    user_id = update.effective_user.id
    
    # Check if the user is still a member of the channel
    if context.bot.get_chat_member(channel_id, user_id).status != 'member':
        update.message.reply_text("You are no longer a member of the channel. Join the channel to continue using the bot.")
    else:
        update.message.reply_text("You can continue using the bot.")

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("7366421763:AAHH211YtRG5jtTYZWE9vEkM-nDDMsfO9AA")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if name == 'main':
    main()