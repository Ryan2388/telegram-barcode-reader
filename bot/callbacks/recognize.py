import io

from PIL import Image
from pyzbar import pyzbar
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, run_async


@run_async
def handle_photo(update: Update, context: CallbackContext):
    del context
    photo = update.effective_message.photo[-1]
    file = photo.get_file()
    file_data = file.download_as_bytearray()
    pil_image = Image.open(io.BytesIO(file_data))
    results = pyzbar.decode(pil_image)
    if not results:
        update.effective_message.reply_text(
            "Упс, я ничего не нашёл на этом изображении. Попробуйте ещё раз"
        )
        return
    vcards = []
    result_descriptions = ""
    for barcode in results:
        data = barcode.data.decode()
        if data.startswith("BEGIN:VCARD"):
            vcards.append(data)
            continue
        result_descriptions += f"*{barcode.type}*: `{data}`\n"
    if result_descriptions:
        update.effective_message.reply_text(
            f"На этом изображении:\n{result_descriptions}",
            parse_mode=ParseMode.MARKDOWN,
        )
    if vcards:
        update.effective_message.reply_text("Найдены vcf контакты:")
    for vcf in vcards:
        update.effective_message.reply_document(
            document=io.BytesIO(vcf.encode()), filename="contact.vcf"
        )
