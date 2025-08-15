# bot.py
# Simple Telegram bot that responds to commands and echoes messages.

from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
)

# --- Your bot token ---
BOT_TOKEN = "YOUR BOT TOKEN"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hi! 👋 I’m alive.\n\n"
        "Commands:\n"
        "• /help – show help\n"
        "• /ping – test me\n"
        "Or send me any text and I’ll echo it."
    )

# /help
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I’m a simple bot.\n\n"
        "Commands:\n"
        "/start – greet\n"
        "/help – this message\n"
        "/ping – I say pong\n\n"
        "Send any text and I’ll echo it."
    )

# /ping
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("pong ✅")

# Echo
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"You said: {update.message.text}")

# Main
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("ping", ping))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()

