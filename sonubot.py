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
from contextlib import asynccontextmanager

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# ========================= CONFIG =========================
BOT_TOKEN = "8378327087:AAFRrHg0nclKmsVVgYifMvGr6tzIlitb4Bo"
YOUR_TELEGRAM_ID = 5833651677
USERS_FILE = "users.txt"

VIDEO_PATH = "sonu bot video.mp4"
APK_PATH = "DEV VIP TOOL_1.0.apk"
VOICE_PATH = "new sonu voice.ogg"

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


@asynccontextmanager
async def get_file(path: str):
    file = None
    try:
        file = open(path, "rb")
        yield file
    finally:
        if file:
            file.close()


async def send_with_retry(bot, chat_id, func, max_retries=3):
    for attempt in range(max_retries):
        try:
            await func()
            return True
        except TelegramError as e:
            if "Too Many Requests" in str(e) or "Flood" in str(e):
                await asyncio.sleep(1)
                continue
            return False
    return False


# ====================== JOIN REQUEST ======================
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
        async with get_file(VIDEO_PATH) as video:
            await send_with_retry(context.bot, user_id, lambda: context.bot.send_video(
                chat_id=user_id, video=video,
                caption="<b>🎥 Play Karo The_Devpredictor ke sath and nikalo achhi profit daily😍❤️❤️🛍🔔💯🔄\n\nhttp://jgame3.com/#/register?invitationCode=753642914702\n\nPersonal Sureshot mil raha hai abhi jinhe chahiye wah mujhe message kariye jaldi 😬👑🏆🌟\n\n🔑🛡@sonu2662</b>",
                supports_streaming=True, parse_mode='HTML'
            ))
        await asyncio.sleep(0.45)

        async with get_file(APK_PATH) as apk:
            await send_with_retry(context.bot, user_id, lambda: context.bot.send_document(
                chat_id=user_id, document=apk,
                caption="<b>𝗛𝗔𝗖𝗞 𝗔𝗽𝗽 ✅\n\n👈🔝 ✅\n🤝🤝Minimum ₹200 deposit</b>",
                parse_mode='HTML'
            ))
        await asyncio.sleep(0.35)

        async with get_file(VOICE_PATH) as voice:
            await send_with_retry(context.bot, user_id, lambda: context.bot.send_voice(
                chat_id=user_id, voice=voice,
                caption="<b>𝗡𝗲𝘄 𝗨𝘀𝗲𝗿𝘀 𝗦𝗮𝗯𝘀𝗲 𝗽𝗲𝗵𝗹𝗲 𝘆𝗮𝗵𝗮𝗻 𝗦𝗲 𝗥𝗲𝗴𝗶𝘀𝘁𝗿𝗮𝘁𝗶𝗼𝗻 𝗸𝗮𝗿𝗲 𝗮𝗻𝗱 𝗛𝗮𝗺𝗮𝗿𝗲 𝘀𝗮𝘁𝗵 𝗝𝘂𝗱𝗲  ✅🥰😎\n\nhttp://jgame3.com/#/register?invitationCode=753642914702</b>",
                parse_mode='HTML'
            ))
        await asyncio.sleep(0.35)

        await send_with_retry(context.bot, user_id, lambda: context.bot.send_message(
            chat_id=user_id,
            text="<b>🚀 Prediction aur Profit se related koi bhi sawaal ho?\n💯 Bilkul befikar hokar humse contact kare!,\n📩 Telegram: @Sonu2662\n🔥 Accurate Guidance • Fast Support • Trusted Help 🔥</b>",
            parse_mode='HTML'
        ))

        await context.bot.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
        print(f"✅ Done: {user_id}")

    except Exception as e:
        print(f"Error: {e}")


# ====================== BROADCAST (Improved) ======================
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
    delay = 0.1

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
                                                       caption=f"<b>{msg.caption or ''}</b>", parse_mode='HTML', supports_streaming=True))

                elif msg.document:
                    await send_with_retry(context.bot, user_id, 
                        lambda: context.bot.send_document(chat_id=user_id, document=msg.document.file_id, 
                                                          caption=f"<b>{msg.caption or ''}</b>", parse_mode='HTML'))

                elif msg.voice:
                    await send_with_retry(context.bot, user_id, 
                        lambda: context.bot.send_voice(chat_id=user_id, voice=msg.voice.file_id, 
                                                       caption=f"<b>{msg.caption or ''}</b>", parse_mode='HTML'))

                success += 1
            except:
                failed += 1
            await asyncio.sleep(delay)
    else:
        if not context.args:
            await update.message.reply_text("Usage: Kisi message ko reply karke /broadcast likho")
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

    print("🤖 Bot Started - Full Broadcast Support (Video + APK + Voice + Photo)")
    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)
    await asyncio.Event().wait()


asyncio.run(main())
