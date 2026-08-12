import os
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# === KONFIGURASI ===
TOKEN = os.environ.get("TOKEN", "TOKEN_BOT_ANDA")
API_KEY = os.environ.get("API_KEY", "API_KEY_PROVIDER")

# === DATABASE SEDERHANA ===
users = {}
orders = {}

# === FUNGSI BANTU ===
def get_user(user_id):
    if user_id not in users:
        users[user_id] = {"balance": 0, "orders": []}
    return users[user_id]

# === COMMAND /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    get_user(user_id)
    
    keyboard = [
        [InlineKeyboardButton("💰 Deposit", callback_data="deposit")],
        [InlineKeyboardButton("📱 Pesan OTP", callback_data="order")],
        [InlineKeyboardButton("📊 Saldo Saya", callback_data="balance")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Selamat datang di OTP Bot!\n\n"
        "Pilih menu di bawah:",
        reply_markup=reply_markup
    )

# === CALLBACK QUERY ===
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    user = get_user(user_id)
    
    if query.data == "deposit":
        await query.edit_message_text(
            "💳 Metode Deposit:\n\n"
            "1. QRIS (Rp 10.000 - Rp 1.000.000)\n"
            "2. Crypto (USDC/BNB)\n\n"
            "Kirim /deposit [jumlah] untuk mulai."
        )
    elif query.data == "order":
        await query.edit_message_text(
            "📱 Pilih Aplikasi:\n\n"
            "Kirim /order [aplikasi] [negara]\n"
            "Contoh: /order whatsapp indonesia"
        )
    elif query.data == "balance":
        await query.edit_message_text(
            f"💰 Saldo Anda: Rp {user['balance']:,}\n"
            f"📦 Total Order: {len(user['orders'])}"
        )

# === COMMAND DEPOSIT ===
async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    
    if not context.args:
        await update.message.reply_text("❌ Gunakan: /deposit [jumlah]")
        return
    
    try:
        amount = int(context.args[0])
        if amount < 10000:
            await update.message.reply_text("❌ Minimal deposit Rp 10.000")
            return
        
        await update.message.reply_text(
            f"💳 Silakan transfer ke:\n\n"
            f"Bank BCA: 1234567890\n"
            f"a.n: OTP BOT\n"
            f"Jumlah: Rp {amount:,}\n\n"
            f"Setelah transfer, kirim /confirm [kode_unik]"
        )
        user["pending_deposit"] = amount
    except ValueError:
        await update.message.reply_text("❌ Masukkan angka yang valid")

# === COMMAND ORDER ===
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    
    if len(context.args) < 2:
        await update.message.reply_text("❌ Gunakan: /order [aplikasi] [negara]")
        return
    
    app = context.args[0]
    country = " ".join(context.args[1:])
    
    await update.message.reply_text(
        f"✅ Order diproses!\n\n"
        f"📱 Aplikasi: {app}\n"
        f"🌍 Negara: {country}\n\n"
        f"⏳ Tunggu sebentar...\n"
        f"Fitur API OTP sedang dalam pengembangan."
    )

# === COMMAND GET OTP ===
async def get_otp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⏳ Fitur cek OTP sedang dalam pengembangan.\n"
        "Nanti akan terhubung dengan provider OTP."
    )

# === MAIN ===
def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("deposit", deposit))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("getotp", get_otp))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Bot berjalan di Render!")
    app.run_polling()

if __name__ == "__main__":
    main()
