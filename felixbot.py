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

    print("🤖 Bot Started - Custom Welcome + Photo Mode")
    await app.initialize()
    await app.start()
    await app.updater.start_polling(drop_pending_updates=True)
    await asyncio.Event().wait()


asyncio.run(main())
