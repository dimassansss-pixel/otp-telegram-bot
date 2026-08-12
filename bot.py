import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ===== TOKEN =====
# GANTI DENGAN TOKEN BARU DARI @BOTFATHER!
TOKEN = "8902588624:AAHgrXLuJ3k4QT9kAMoCxAkeWn1Obefc0yQ"

# ===== DATA SEMENTARA =====
users = {}

def get_user(user_id):
    if user_id not in users:
        users[user_id] = {"balance": 0, "orders": [], "pending_deposit": 0}
    return users[user_id]

# ===== COMMAND /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Deposit", callback_data="deposit")],
        [InlineKeyboardButton("📦 Order", callback_data="order")],
        [InlineKeyboardButton("💳 Saldo", callback_data="balance")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Selamat datang di OTP Bot!\n\n"
        "Pilih menu di bawah:",
        reply_markup=reply_markup
    )

# ===== COMMAND /s =====
async def s(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo dari command /s")

# ===== COMMAND /d =====
async def d(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo dari command /d")

# ===== COMMAND /o =====
async def o(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo dari command /o")

# ===== COMMAND /g =====
async def g(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo dari command /g")

# ===== COMMAND /deposit =====
async def deposit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user = get_user(user_id)
    
    if not context.args:
        await update.message.reply_text(
            "💳 Metode Deposit:\n\n"
            "1. QRIS (Rp 10.000 - Rp 1.000.000)\n"
            "2. Crypto (USDC/BNB)\n\n"
            "Kirim /deposit [jumlah] untuk mulai."
        )
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

# ===== COMMAND /order =====
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("❌ Gunakan: /order [aplikasi] [negara]")
        return
    
    app_name = context.args[0]
    country = " ".join(context.args[1:])
    
    await update.message.reply_text(
        f"✅ Order diproses!\n\n"
        f"📱 Aplikasi: {app_name}\n"
        f"🌍 Negara: {country}\n\n"
        f"⏳ Tunggu sebentar...\n"
        f"Fitur API OTP sedang dalam pengembangan."
    )

# ===== COMMAND /getotp =====
async def get_otp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⏳ Fitur cek OTP sedang dalam pengembangan.\n"
        "Nanti akan terhubung dengan provider OTP."
    )

# ===== CALLBACK QUERY HANDLER =====
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

# ===== MAIN FUNCTION =====
async def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("s", s))
    app.add_handler(CommandHandler("d", d))
    app.add_handler(CommandHandler("o", o))
    app.add_handler(CommandHandler("g", g))
    app.add_handler(CommandHandler("deposit", deposit))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("getotp", get_otp))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Bot berjalan di Railway!")
    await app.run_polling()

# ===== ENTRY POINT =====
:
    asyncio.run(main())            "2. Crypto (USDC/BNB)\n\n"
            "Kirim /deposit [jumlah] untuk mulai."
        )
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

# ===== COMMAND /order =====
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text("❌ Gunakan: /order [aplikasi] [negara]")
        return
    
    app_name = context.args[0]
    country = " ".join(context.args[1:])
    
    await update.message.reply_text(
        f"✅ Order diproses!\n\n"
        f"📱 Aplikasi: {app_name}\n"
        f"🌍 Negara: {country}\n\n"
        f"⏳ Tunggu sebentar...\n"
        f"Fitur API OTP sedang dalam pengembangan."
    )

# ===== COMMAND /getotp =====
async def get_otp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⏳ Fitur cek OTP sedang dalam pengembangan.\n"
        "Nanti akan terhubung dengan provider OTP."
    )

# ===== CALLBACK QUERY HANDLER =====
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

# ===== MAIN FUNCTION =====
async def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("s", s))
    app.add_handler(CommandHandler("d", d))
    app.add_handler(CommandHandler("o", o))
    app.add_handler(CommandHandler("g", g))
    app.add_handler(CommandHandler("deposit", deposit))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("getotp", get_otp))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("🤖 Bot berjalan di Railway!")
    await app.run_polling()

# ===== ENTRY POINT =====
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "You reached the end of the range" in str(e):
            print("✅ Bot berhenti dengan normal")
        else:
            raise e

# ===== ENTRY POINT =====
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "You reached the end of the range" in str(e):
            print("Bot berhasil dihentikan dengan normal")
        else:
            raise e
