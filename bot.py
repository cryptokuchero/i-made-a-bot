import requests
import re
from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    MessageHandler,
    Filters,
)


def swap(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        f"So your selling how many\? {update.effective_user.first_name}"
    )


def do_saywhat(username, user_input):
    answer = "You wrote" + user_input + "into the channel @SwapSats"
    message_to_channel = user_input
    clean_message = re.sub("\W+", " ", message_to_channel)
    # Change this
    apikey = "547559123:NNUE4LwNhtg-Fu9O9ZmzsAabCDEfgh9j0123456"
    # Change this
    the_channel = "SomeChannel"
    requests.post(
        "https://api.telegram.org/bot"
        + apikey
        + "/sendMessage?chat_id=@+" + the_channel + "&text="
        + clean_message
        + "! contact @"
        + username
        + ":-)"
    )
    return answer


def reply(update: Update, context: CallbackContext):
    user_input = update.message.text
    user = update.message.from_user
    username = user["username"]
    update.message.reply_text(do_saywhat(username, user_input))


def main() -> None:
     # This key is fake
    apikey = "547559123:NNUE4LwNhtg-Fu9O9ZmzsAabCDEfgh9j0123456"

    updater = Updater(apikey)

    updater.dispatcher.add_handler(CommandHandler("swapping", swap))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
