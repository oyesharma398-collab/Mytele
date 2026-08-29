import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.error import BadRequest

# ==========================================
# CONFIGURATION
# ==========================================
BOT_TOKEN = "8661315253:AAFFTw7k9RxvtXAXDkr4mcd60Rd0fsUUBcU"
CHANNEL_USERNAME = "@kronrules"
CHANNEL_LINK = "https://t.me/kronrules"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            await deliver_content(update.message)
            return
    except BadRequest:
        pass

    keyboard = [
        [InlineKeyboardButton("📢 JOIN OFFICIAL CHANNEL", url=CHANNEL_LINK)],
        [InlineKeyboardButton("🔓 VERIFY & UNLOCK", callback_data="check_join")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    lock_message = (
        "❖ <b>────── [ SYSTEM ACCESS LOCKED ] ──────</b> ❖\n\n"
        "🔒 <b>AUTHORIZATION REQUIRED</b>\n\n"
        "To access the secret generator bots, you must join our channel first.\n\n"
        "<b>Steps to unlock:</b>\n"
        "1️⃣ Click <b>JOIN OFFICIAL CHANNEL</b> below.\n"
        "2️⃣ Click <b>VERIFY & UNLOCK</b> button.\n\n"
        "<i>[@kronrules Security Terminal]</i>"
    )
    
    await update.message.reply_text(lock_message, reply_markup=reply_markup, parse_mode="HTML")

async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            await run_multi_stage_animations(query)
        else:
            await query.answer("❌ Verification Failed! Please join @kronrules first.", show_alert=True)
    except BadRequest:
        await query.answer("⚠️ System Error: Unable to verify channel membership.", show_alert=True)

async def run_multi_stage_animations(query):
    # 6 Completely Different Animations with unique visuals & layouts
    animations = [
        # Frame 1: Terminal Init
        "❖ <b>[ STAGE 1/6 ]</b> ❖\n\n"
        "📡 <code>INITIALIZING SYSTEM SCAN...</code>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "<code>Target: @kronrules Network</code>\n"
        "<code>Protocol: Secure Handshake v4.2</code>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "⏳ <i>Establishing encrypted connection...</i>",

        # Frame 2: Gateway Verification
        "❖ <b>[ STAGE 2/6 ]</b> ❖\n\n"
        "🔐 <code>CHECKING SECURITY GATEWAY...</code>\n"
        "┌──────────────────────┐\n"
        "│  Bypassing Gateway #1 [ OK ]  │\n"
        "│  Bypassing Gateway #2 [ OK ]  │\n"
        "└──────────────────────┘\n"
        "⚡ <i>Gateways cleared successfully.</i>",

        # Frame 3: Member Token Scan
        "❖ <b>[ STAGE 3/6 ]</b> ❖\n\n"
        "👤 <code>SCANNING USER MEMBERSHIP...</code>\n"
        "<code>[✔] User Verification : APPROVED</code>\n"
        "<code>[✔] Channel Status    : ACTIVE MEMBER</code>\n"
        "<code>[✔] Access Privilege : GRANTED</code>\n\n"
        "🔑 <i>Authorization Key Verified.</i>",

        # Frame 4: Data Decryption
        "❖ <b>[ STAGE 4/6 ]</b> ❖\n\n"
        "🗝️ <code>DECRYPTING SECRET PAYLOAD...</code>\n"
        "<code>Cipher  : AES-256-GCM</code>\n"
        "<code>Payload : [ █ █ █ █ █ █ █ █ ░ ░ ] 75%</code>\n\n"
        "⚙️ <i>Unlocking restricted handles...</i>",

        # Frame 5: Server Allocation
        "❖ <b>[ STAGE 5/6 ]</b> ❖\n\n"
        "⚡ <code>ALLOCATING SYSTEM RESOURCES...</code>\n"
        "<code>----------------------------------</code>\n"
        "<code>Buffer  : 2048 KB Allocated</code>\n"
        "<code>Status  : Transmitting Final Data...</code>\n"
        "<code>----------------------------------</code>\n"
        "🚀 <i>Preparing payload delivery...</i>",

        # Frame 6: Access Granted
        "❖ <b>[ STAGE 6/6 ]</b> ❖\n\n"
        "✅ <code>SYSTEM OVERRIDE COMPLETE!</code>\n"
        "<code>==================================</code>\n"
        "<code>ALL SECURITY CHECKS PASSED PASSED</code>\n"
        "<code>==================================</code>\n\n"
        "🎉 <i>Displaying content now...</i>"
    ]
    
    # Run through each animation stage (1.5 seconds delay per stage)
    for frame in animations:
        await query.edit_message_text(frame, parse_mode="HTML")
        await asyncio.sleep(1.5)  # 1.5 Seconds Display Time per Animation
    
    await asyncio.sleep(0.5)
    
    # Final Custom Payload Message
    final_payload = (
        "𝜥𝜸𝜽𝜼: 𝑪𝜞𝑼𝑺𝜮𝑫 𝑾𝜤𝜯𝜢 𝜥𝜫𝜣𝑾𝑳𝜮𝑫𝑮𝜮\n\n"
        "Here are your requested resources:\n\n"
        "🛠️ <b>Gmail Generator Service:</b>\n"
        "👉 @Create_Unlimited_Gmaiiil_Bot\n\n"
        "📱 <b>Virtual Number Service:</b>\n"
        "👉 @Unlimited_Numbers1_bot\n\n"
        "───────────────\n"
        "⚡ <i>Powered by @kronrules</i>"
    )
    
    await query.edit_message_text(final_payload, parse_mode="HTML")

async def deliver_content(message_obj):
    final_payload = (
        "𝜥𝜸𝜽𝜼: 𝑪𝜞𝑼𝑺𝜮𝑫 𝑾𝜤𝜯𝜢 𝜥𝜫𝜣𝑾𝑳𝜮𝑫𝑮𝜮\n\n"
        "Your access is already active. Here are your links:\n\n"
        "🛠️ <b>Gmail Generator Service:</b>\n"
        "👉 @Create_Unlimited_Gmaiiil_Bot\n\n"
        "📱 <b>Virtual Number Service:</b>\n"
        "👉 @Unlimited_Numbers1_bot\n\n"
        "───────────────\n"
        "⚡ <i>Powered by @kronrules</i>"
    )
    await message_obj.reply_text(final_payload, parse_mode="HTML")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(check_join, pattern="^check_join$"))
    
    print("[+] Kronrules Advanced Animation Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
  
