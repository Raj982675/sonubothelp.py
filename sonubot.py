from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes,
    CommandHandler
)
from telegram.error import TelegramError
import asyncio
import sys
import os
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# ========================= CONFIG =========================
BOT_TOKEN = "8378327087:AAFRrHg0nclKmsVVgYifMvGr6tzIlitb4Bo"
YOUR_TELEGRAM_ID = 5833651677
USERS_FILE = "users.txt"

VIDEO_PATH = "sonu bot video.mp4"
APK_PATH = "DEV VIP TOOL_1.0.apk"
VOICE_PATH = "sonu voice.mp3"

# =========================================================

def save_user(user_id: int):
    try:
        Path(USERS_FILE).parent.mkdir(parents=True, exist_ok=True)
        with open(USERS_FILE, "a+", encoding="utf-8") as f:
            f.seek(0)
            users = {line.strip() for line in f if line.strip()}
            if str(user_id) not in users:
                f.write(f"{user_id}\n")
    except:
        pass


def get_all_users():
    try:
        if not os.path.exists(USERS_FILE):
            return []
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            return [int(line.strip()) for line in f if line.strip().isdigit()]
    except:
        return []


async def send_with_retry(bot, chat_id, func, max_retries=2):
    for attempt in range(max_retries):
        try:
            await func()
            return True
        except TelegramError as e:
            if "Too Many Requests" in str(e):
                await asyncio.sleep(0.6)
                continue
            return False
    return False


# ====================== JOIN REQUEST (3 Sec + All Bold) ======================
async def join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    req = update.chat_join_request
    user_id = req.from_user.id
    chat_id = req.chat.id

    print(f"🔄 New Join Request from: {user_id}")
    save_user(user_id)

    if not all(os.path.exists(p) for p in [VIDEO_PATH, APK_PATH, VOICE_PATH]):
        print("❌ Files missing!")
        return

    try:
        # 1. Welcome
        await send_with_retry(context.bot, user_id, lambda: context.bot.send_message(
            chat_id=user_id,
            text="<b>👋 Welcome!\n\n✅ Aapka join request successfully approve ho gaya hai\n📢 @𝐃𝐞𝐯_𝐭𝐡𝐞𝐏𝐫𝐞𝐝𝐢𝐜𝐭𝐨𝐫.\n\n📩 Niche diya gaya important hack zarur use karein 👇\n\n🚀 Ye hack aapko better results aur fast growth dene me help karega.\n\nPlease wait a moment ⏳</b>",
            parse_mode='HTML'
        ))
        await asyncio.sleep(0.25)

        # 2. Video
        await send_with_retry(context.bot, user_id, lambda: context.bot.send_video(
            chat_id=user_id,
            video=open(VIDEO_PATH, "rb"),
            caption="<b>🎥 Play Karo The_Devpredictor ke sath and nikalo achhi profit daily😍❤️❤️🛍🔔💯🔄\n\nhttp://jgame3.com/#/register?invitationCode=753642914702\n\nPersonal Sureshot mil raha hai abhi jinhe chahiye wah mujhe message kariye jaldi 😬👑🏆🌟\n\n🔑🛡@sonu2662</b>",
            supports_streaming=True,
            parse_mode='HTML'
        ))
        await asyncio.sleep(0.45)

        # 3. APK
        await send_with_retry(context.bot, user_id, lambda: context.bot.send_document(
            chat_id=user_id,
            document=open(APK_PATH, "rb"),
            caption="<b>𝗛𝗔𝗖𝗞 𝗔𝗽𝗽 ✅\n\n👈🔝 ✅\n🤝🤝Minimum ₹200 deposit</b>",
            parse_mode='HTML'
        ))
        await asyncio.sleep(0.25)

        # 4. Voice
        await send_with_retry(context.bot, user_id, lambda: context.bot.send_voice(
            chat_id=user_id,
            voice=open(VOICE_PATH, "rb"),
            caption="<b>🎙 Important Voice Message</b>",
            parse_mode='HTML'
        ))
        await asyncio.sleep(0.25)

        # 5. Final Message
        await send_with_retry(context.bot, user_id, lambda: context.bot.send_message(
            chat_id=user_id,
            text="<b>✅ 𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗮𝘁𝗶𝗼𝗻 𝗸𝗮𝗿𝗸𝗲 𝗞𝘂𝗰𝗵𝗵 𝗯𝗵𝗶 𝗔𝗺𝗼𝘂𝗻𝘁 𝗗𝗲𝗽𝗼𝘀𝗶𝘁 𝗸𝗮𝗿𝗹𝗼\n𝗼𝗼𝘀𝗸𝗲 𝗯𝗮𝗮𝗱 𝗵𝗮𝗺𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗸𝗮𝗿𝗼 𝗨𝗜𝗗 𝗻𝘂𝗺𝗯𝗲𝗿 𝗸𝗲 𝘀𝗮𝘁𝗵,\n𝗛𝗮𝗺 𝗮𝗮𝗽𝗸𝗼 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲 𝗔𝗱𝗱 𝗸𝗮𝗿𝗱𝗲𝗻𝗴𝗲\n𝗮𝗻𝗱 𝗮𝗮𝗽 𝘄𝗮𝗵𝗮𝗻 𝘀𝗲 𝗮𝗰𝗵𝗵𝗮 𝗽𝗿𝗼𝗳𝗶𝘁 𝗡𝗶𝗸𝗮𝗹𝗻𝗮 💳🪙 🎉</b>",
            parse_mode='HTML'
        ))

        await context.bot.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
        print(f"✅ 3 Sec Bold Sequence Done: {user_id}")

    except Exception as e:
        print(f"Error: {e}")


# ====================== BROADCAST ======================
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != YOUR_TELEGRAM_ID:
        await update.message.reply_text("❌ Permission Denied!")
        return

    users = get_all_users()
    if not users:
        await update.message.reply_text("❌ No users found.")
        return

    await update.message.reply_text(f"🔄 Broadcasting to {len(users)} users...")

    success = failed = 0
    delay = 0.07

    if update.message.reply_to_message:
        msg = update.message.reply_to_message
        for user_id in users:
            try:
                if msg.text:
                    await send_with_retry(context.bot, user_id, 
                        lambda: context.bot.send_message(chat_id=user_id, text=f"<b>{msg.text}</b>", parse_mode='HTML'))
                elif msg.photo:
                    await send_with_retry(context.bot, user_id, 
                        lambda: context.bot.send_photo(chat_id=user_id, photo=msg.photo[-1].file_id, 
                                                       caption=f"<b>{msg.caption or ''}</b>", parse_mode='HTML'))
                elif msg.video:
                    await send_with_retry(context.bot, user_id, 
                        lambda: context.bot.send_video(chat_id=user_id, video=msg.video.file_id, 
                                                       caption=f"<b>{msg.caption or ''}</b>", parse_mode='HTML'))
                elif msg.document:
                    await send_with_retry(context.bot, user_id, 
                        lambda: context.bot.send_document(chat_id=user_id, document=msg.document.file_id, 
                                                          caption=f"<b>{msg.caption or ''}</b>", parse_mode='HTML'))
                success += 1
            except:
                failed += 1
            await asyncio.sleep(delay)
    else:
        if not context.args:
            await update.message.reply_text("Usage: Reply karke /broadcast karo ya text likho")
            return
        text = ' '.join(context.args)
        for user_id in users:
            await send_with_retry(context.bot, user_id, 
                lambda: context.bot.send_message(chat_id=user_id, text=f"<b>{text}</b>", parse_mode='HTML'))
            success += 1
            await asyncio.sleep(delay)

    await update.message.reply_text(f"✅ Broadcast Completed!\nSuccess: {success}\nFailed: {failed}")


async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(join_request))
    app.add_handler(CommandHandler("broadcast", broadcast))

    print("🤖 Bot Started - 3 Second Fast + All Bold + Broadcast Ready")
    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)
    await asyncio.Event().wait()


asyncio.run(main())