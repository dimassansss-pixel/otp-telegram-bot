import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ===== FUNGSI-FUNGSI COMMAND =====
async def s(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo dari command /s")

async def d(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo dari command /d")

async def o(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo dari command /o")

async def g(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo dari command /g")

# ===== CALLBACK QUERY HANDLER =====
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # wajib untuk merespon callback

    if query.data == "deposit":
        await query.edit_message_text(
            "Metode Deposit:\n\n"
            "1. QRIS (Rp 1.000 - Rp 50.000)\n"
            "2. Crvnto (USD/C/RNB)"
        )

# ===== MAIN FUNCTION =====
async def main():
    # Ganti 'TOKEN_KAMU' dengan token bot asli
    app = Application.builder().token("8902588624:AAF8Wt4-EnJIAIxMDyXmHw3KwA1_Uygd_SA").build()

    # Tambahkan handler command
    app.add_handler(CommandHandler("s", s))
    app.add_handler(CommandHandler("d", d))
    app.add_handler(CommandHandler("o", o))
    app.add_handler(CommandHandler("g", g))
    app.add_handler(CallbackQueryHandler(button_handler))  # <-- perbaiki di sini

    print("Bot berjalan di Railway")
    await app.run_polling()

# ===== ENTRY POINT =====
if __name__ == "__main__":
    asyncio.run(main())  # hanya 1 kali, di paling bawah    app.add_handler(CommandHandler("deposit", deposit))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("getotp", get_otp))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Bot berjalan di Railway!")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())# === MAIN ===
async def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("deposit", deposit))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("getotp", get_otp))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Bot berjalan di Railway!")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())        "👋 Selamat datang di OTP Bot!\n\n"
        "Pilih menu di bawah:",
        reply_markup=reply_markup
    

# === CALLBACK QUERY ===
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    user = get_user(user_id)
    
    if query.data == "deposit":
        query.edit_message_text(
            "💳 Metode Deposit:\n\n"
            "1. QRIS (Rp 10.000 - Rp 1.000.000)\n"
            "2. Crypto (USDC/BNB)\n\n"
            "Kirim /deposit [jumlah] untuk mulai."
        )
    elif query.data == "order":
        query.edit_message_text(
            "📱 Pilih Aplikasi:\n\n"
            "Kirim /order [aplikasi] [negara]\n"
            "Contoh: /order whatsapp indonesia"
        )
    elif query.data == "balance":
        query.edit_message_text(
            f"💰 Saldo Anda: Rp {user['balance']:,}\n"
            f"📦 Total Order: {len(user['orders'])}"
        )

# === COMMAND DEPOSIT ===
def deposit(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = get_user(user_id)
    
    if not context.args:
        update.message.reply_text("❌ Gunakan: /deposit [jumlah]")
        return
    
    try:
        amount = int(context.args[0])
        if amount < 10000:
            update.message.reply_text("❌ Minimal deposit Rp 10.000")
            return
        
        update.message.reply_text(
            f"💳 Silakan transfer ke:\n\n"
            f"Bank BCA: 1234567890\n"
            f"a.n: OTP BOT\n"
            f"Jumlah: Rp {amount:,}\n\n"
            f"Setelah transfer, kirim /confirm [kode_unik]"
        )
        user["pending_deposit"] = amount
    except ValueError:
        update.message.reply_text("❌ Masukkan angka yang valid")

# === COMMAND ORDER ===
def order(update: Update, context: CallbackContext):
    if len(context.args) < 2:
        update.message.reply_text("❌ Gunakan: /order [aplikasi] [negara]")
        return
    
    app = context.args[0]
    country = " ".join(context.args[1:])
    
    update.message.reply_text(
        f"✅ Order diproses!\n\n"
        f"📱 Aplikasi: {app}\n"
        f"🌍 Negara: {country}\n\n"
        f"⏳ Tunggu sebentar...\n"
        f"Fitur API OTP sedang dalam pengembangan."
    )

# === COMMAND GET OTP ===
def get_otp(update: Update, context: CallbackContext):
    update.message.reply_text(
        "⏳ Fitur cek OTP sedang dalam pengembangan.\n"
        "Nanti akan terhubung dengan provider OTP."
    )

# === MAIN ===
def main():
    logger.info("🤖 Starting bot...")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("deposit", deposit))
    dp.add_handler(CommandHandler("order", order))
    dp.add_handler(CommandHandler("getotp", get_otp))
    dp.add_handler(CallbackQueryHandler(button_handler))
    
    logger.info("🤖 Bot berjalan di Render!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
# === CALLBACK QUERY ===
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user_id = query.from_user.id
    user = get_user(user_id)
    
    if query.data == "deposit":
        query.edit_message_text(
            "💳 Metode Deposit:\n\n"
            "1. QRIS (Rp 10.000 - Rp 1.000.000)\n"
            "2. Crypto (USDC/BNB)\n\n"
            "Kirim /deposit [jumlah] untuk mulai."
        )
    elif query.data == "order":
        query.edit_message_text(
            "📱 Pilih Aplikasi:\n\n"
            "Kirim /order [aplikasi] [negara]\n"
            "Contoh: /order whatsapp indonesia"
        )
    elif query.data == "balance":
        query.edit_message_text(
            f"💰 Saldo Anda: Rp {user['balance']:,}\n"
            f"📦 Total Order: {len(user['orders'])}"
        )

# === COMMAND DEPOSIT ===
def deposit(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = get_user(user_id)
    
    if not context.args:
        update.message.reply_text("❌ Gunakan: /deposit [jumlah]")
        return
    
    try:
        amount = int(context.args[0])
        if amount < 10000:
            update.message.reply_text("❌ Minimal deposit Rp 10.000")
            return
        
        update.message.reply_text(
            f"💳 Silakan transfer ke:\n\n"
            f"Bank BCA: 1234567890\n"
            f"a.n: OTP BOT\n"
            f"Jumlah: Rp {amount:,}\n\n"
            f"Setelah transfer, kirim /confirm [kode_unik]"
        )
        user["pending_deposit"] = amount
    except ValueError:
        update.message.reply_text("❌ Masukkan angka yang valid")

# === COMMAND ORDER ===
def order(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user = get_user(user_id)
    
    if len(context.args) < 2:
        update.message.reply_text("❌ Gunakan: /order [aplikasi] [negara]")
        return
    
    app = context.args[0]
    country = " ".join(context.args[1:])
    
    update.message.reply_text(
        f"✅ Order diproses!\n\n"
        f"📱 Aplikasi: {app}\n"
        f"🌍 Negara: {country}\n\n"
        f"⏳ Tunggu sebentar...\n"
        f"Fitur API OTP sedang dalam pengembangan."
    )

# === COMMAND GET OTP ===
def get_otp(update: Update, context: CallbackContext):
    update.message.reply_text(
        "⏳ Fitur cek OTP sedang dalam pengembangan.\n"
        "Nanti akan terhubung dengan provider OTP."
    )

# === MAIN ===
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("deposit", deposit))
    dp.add_handler(CommandHandler("order", order))
    dp.add_handler(CommandHandler("getotp", get_otp))
    dp.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Bot berjalan di Render!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
