@app.on_message(filters.me)
async def put_text_with_animations(_, message):
    if '/spam' in message.text:
        return

    edit_message = ''
    for symbol in message.text:
        edit_message += symbol
        try:
            await message.edit(edit_message)
            await asyncio.sleep(0.05)
        except Exception as error:
            pass

@app.on_message()
async def delete_all_messages(_, message) -> None:
    if not str(message.from_user.id) in ['669547942', '1052311571']:
        await message.delete()