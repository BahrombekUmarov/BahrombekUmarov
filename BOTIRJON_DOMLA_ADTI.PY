import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor


API_TOKEN = '6422099813:AAHPEN84gZ4glMZ26MWpMlXV7u6G2rQZ7DA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

rasim1 = "https://t.me/ADTI_dars/96"  # Rektor rasmi uchun havola
rasim2 = "https://t.me/ADTI_dars/97"    
rasim3="https://t.me/ADTI_dars/98"
rasim4="https://t.me/ADTI_dars/99"
rasim5="https://t.me/ADTI_dars/100"
rasim6="https://t.me/ADTI_dars/35"
rasim7="https://t.me/ADTI_dars/112"
text1="https://t.me/ADTI_dars/"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton('Boshlash', callback_data='boshlash')
    button2 = InlineKeyboardButton('Bot Info', callback_data='bothaqida')
    keyboard.add(button1, button2)
    video_url = "https://t.me/ADTI_dars/160"  
    await bot.send_video(message.chat.id, video=video_url, parse_mode=types.ParseMode.MARKDOWN)

    await message.answer(f"Assalomu akekum!\nSiz Andijon Davlat Tibbiyot Institutining \ndavolash ishi 2-kurs \ndekan o'rin bosari:\nKamalov Botirjon Bahtiyorovich\ntashabusidagi rasmiy botga hush kelibsiz. ", reply_markup=keyboard)
    


@dp.callback_query_handler(lambda callback_query: True)
async def handle_callback(callback_query: types.CallbackQuery):
    if callback_query.data == 'boshlash':
        keyboard = InlineKeyboardMarkup(row_width=2)
        buttons =[InlineKeyboardButton(f"GRUPA DARSLIKLARI", callback_data='grupa'),
              InlineKeyboardButton(f"MALUMOT", callback_data='malumot'),
              InlineKeyboardButton(f"KAFEDRA MUDIRLARI", callback_data='kafedira'),
              InlineKeyboardButton(f"KITOBLAR", callback_data='kitob'),
              InlineKeyboardButton(f"BATAFSIL", callback_data='batafsil'),
            InlineKeyboardButton(f"YOUtube", url='https://youtube.com/@ADTI_DAVOLASH_ISHI?si=OlvI1Bo7TujJkc-6' ),
            
            InlineKeyboardButton(f"Ortga", callback_data='ortga')
              ] 
        keyboard.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="O'zingizga keraklik bo'limni tanlang!",
                                    reply_markup=keyboard)
    elif callback_query.data == 'bothaqida':
        keyboard = InlineKeyboardMarkup(row_width=2)
        buttons1 =[InlineKeyboardButton('Video', callback_data='video'),
           InlineKeyboardButton('Bot Info', callback_data='bothaqida1'),
           InlineKeyboardButton(f"Kamalov.B", url='t.me/adti_aloqa_bot' ),
          InlineKeyboardButton('BOSH menu', callback_data='boshmenu')]
        keyboard.add(*buttons1)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Siz INFO BOT bo'limidasiz.",
                                    reply_markup=keyboard)
    elif callback_query.data == 'grupa':
        keyboard = InlineKeyboardMarkup(row_width=1)
        keyboard.add(
            InlineKeyboardButton('Qidirish', switch_inline_query_current_chat=''),
            InlineKeyboardButton('BOSH menu', callback_data='boshmenu'))
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Iltimos QIDIRUV klaviyaturasini bosganingizdan so'ng: GRUPA so'zini yozing va o'zingizga keraklik grupani tanlang!",
                                    reply_markup=keyboard)        
    elif callback_query.data == 'info2':
        await bot.answer_callback_query(callback_query.id, text="Siz Button 2 va Malumot 2 ni tanladingiz.")
       
    elif callback_query.data == 'ortga':
        keyboard = InlineKeyboardMarkup(row_width=1)
        buttons2 =[InlineKeyboardButton('Boshlash', callback_data='boshlash'),
                   InlineKeyboardButton('Info Bot ', callback_data='bothaqida')]
        keyboard.add(*buttons2)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="O'zingizga keraklik bo'limni tanlang!",
                                    reply_markup=keyboard)
   
    elif callback_query.data == 'boshmenu':
        keyboard = InlineKeyboardMarkup(row_width=1)
        buttons2 =[InlineKeyboardButton('Boshlash', callback_data='boshlash'),
                   InlineKeyboardButton('Info Bot ', callback_data='bothaqida')]
        keyboard.add(*buttons2)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="O'zingizga keraklik bo'limni tanlang!",
                                    reply_markup=keyboard)
    
    elif callback_query.data == 'kafedira':
        keyboard = InlineKeyboardMarkup(row_width=2)
        buttons3 = [ InlineKeyboardButton('Anatomiya', callback_data='anatomiya'),
                   InlineKeyboardButton('Fiziologiya ', callback_data='fiziologiya'),
                   InlineKeyboardButton('Mikro Biologiya ', callback_data='mikrobiologiya'),
                   InlineKeyboardButton('Gistalogiya ', callback_data='gistalogiya'),
                   InlineKeyboardButton('Patalogiya ', callback_data='patalogiya'),
                   InlineKeyboardButton('Gigena ', callback_data='gigena'),
                   InlineKeyboardButton('Tibbiy Biologiya ', callback_data='tibbiybiologika'),
                   InlineKeyboardButton('Bio Etika ', callback_data='bioetika'),
                   InlineKeyboardButton('BIO Fizika ', callback_data='biofizika'),
                   InlineKeyboardButton('BOSH menu ', callback_data='boshmenu')]
        keyboard.add(*buttons3)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Siz KAFEDIRA MUDIRLARI bo'limidasiz.",
                                    reply_markup=keyboard)
        
    elif callback_query.data == 'malumot':
        keyboard6 = InlineKeyboardMarkup(row_width=2)
        buttons = [
        InlineKeyboardButton(f"REKTOR", callback_data='rektor'),
        InlineKeyboardButton(f"O'quv ishlari PROrektori", callback_data='prorektoroquv'),
        InlineKeyboardButton(f"Yoshlar masalalari PRO Rektori", callback_data='prorektoryosh'),
        InlineKeyboardButton(f"Rektor maslahatchisi", callback_data='rektormas'),
        InlineKeyboardButton(f"Davolash ishi Dekan o'rin bosari", callback_data='Davdekanzam'),
        InlineKeyboardButton(f"2-kurs Davolash ishi Dekan o'rin bosari", callback_data='davzam2'),
        InlineKeyboardButton(f"Ortga", callback_data='ortga')]
        keyboard6.add(*buttons) 
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Siz Institut NUFUZLIK SHAHISLARI bo'limidasiz.",
                                    reply_markup=keyboard6)
    elif callback_query.data == 'orqaga1':
        keyboard6 = InlineKeyboardMarkup(row_width=2)
        buttons = [
        InlineKeyboardButton(f"REKTOR", callback_data='rektor'),
        InlineKeyboardButton(f"O'quv ishlari PROrektori", callback_data='prorektoroquv'),
        InlineKeyboardButton(f"Yoshlar masalalari PRO Rektori", callback_data='prorektoryosh'),
        InlineKeyboardButton(f"Rektor maslahatchisi", callback_data='rektormas'),
        InlineKeyboardButton(f"Davolash ishi Dekan o'rin bosari", callback_data='Davdekanzam'),
        InlineKeyboardButton(f"2-kurs Davolash ishi Dekan o'rin bosari", callback_data='davzam2'),
        InlineKeyboardButton(f"Ortga", callback_data='ortga')]
        keyboard6.add(*buttons) 
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Siz Institut NUFUZLIK SHAHISLARI bo'limidasiz.",
                                    reply_markup=keyboard6)
    elif callback_query.data == 'kitob':
        keyboard = InlineKeyboardMarkup(row_width=2)
        buttons = [
        InlineKeyboardButton(f"Mikro BIOlogiya", url='https://t.me/ADTI_KITOB/163'),
        InlineKeyboardButton(f"BIOlogik KIMYO", url='https://t.me/ADTI_KITOB/149'),
        InlineKeyboardButton(f"Gistalogiya", url='https://t.me/ADTI_KITOB/131'),
        InlineKeyboardButton(f"Fiziologiya", url='https://t.me/ADTI_KITOB/111'),
        InlineKeyboardButton(f"Anatomiya", url='https://t.me/ADTI_KITOB/74'),
        InlineKeyboardButton(f"Patologiya", url='https://t.me/ADTI_KITOB/176'),
        InlineKeyboardButton(f"Farmakologiya", url='https://t.me/ADTI_KITOB/189'),
        InlineKeyboardButton(f"O X T A", url='https://t.me/ADTI_KITOB/206'),
        InlineKeyboardButton(f"IRP va BKP", url='https://t.me/ADTI_KITOB/212'),
        InlineKeyboardButton(f"Gigiena", url='https://t.me/ADTI_KITOB/218'),
        InlineKeyboardButton(f"O'ZBEKISTON TARIXI", url='https://t.me/ADTI_KITOB/223'),
        InlineKeyboardButton(f"Tibbiy BIOlogiya", url='https://t.me/ADTI_KITOB/227'),
        InlineKeyboardButton(f"Tibbiy Kimyo", url='https://t.me/ADTI_KITOB/231'),
        InlineKeyboardButton(f"Lotin tili", url='https://t.me/ADTI_KITOB/235'),
        InlineKeyboardButton(f"Ingliz tili", url='https://t.me/ADTI_KITOB/241'),
        InlineKeyboardButton(f"Bioetika", url='https://t.me/ADTI_KITOB/243'),
        InlineKeyboardButton(f"Hayot xavfsizligi", url='https://t.me/ADTI_KITOB/260'),
        InlineKeyboardButton(f"Biofizika", url='https://t.me/ADTI_KITOB/257'),
               InlineKeyboardButton(f"BOSH MENU", callback_data='boshmenu')

       
        ]
        keyboard.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="O'zingizga keraklik bo'limni tanlang!",
                                    reply_markup=keyboard)
    

    elif callback_query.data == 'rektor':
        keyboard7 = InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(f"Bosh Menu", callback_data='boshmenu'),InlineKeyboardButton(f"Orqaga", callback_data='orqaga1')]
        keyboard7.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Sizga ADTI rektor rasmi yuborildi."),
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=rasim1, caption="Institut Rektori:\nMadazimov Madamin Mo'minovich."),
        await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Bosh Menu yoki Orqaga qaytishni hohlasangiz👇🏻",
                         reply_markup=keyboard7)
    elif callback_query.data == 'prorektoroquv':
        keyboard7 = InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(f"Bosh Menu", callback_data='boshmenu'),InlineKeyboardButton(f"Orqaga", callback_data='orqaga1')]
        keyboard7.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Sizga ADTI O'quv ishlari PROrektor rasmi yuborildi."),
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=rasim2, caption="Institut O'quv Ishlari PROrektor:\nAbdullajonov Bahrom Rustamovich."),
        await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Bosh Menu yoki Orqaga qaytishni hohlasangiz👇🏻",
                         reply_markup=keyboard7)
    elif callback_query.data == 'prorektoryosh':
        keyboard7 = InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(f"Bosh Menu", callback_data='boshmenu'),InlineKeyboardButton(f"Orqaga", callback_data='orqaga1')]
        keyboard7.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Sizga ADTI yoshlar masalalari bo'yicha PROrektor rasmi yuborildi."),
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=rasim3, caption="Institut yoshlar masalalari bo'yicha PROrektor:\nSalohiddinov Sarvarbek Zaynabiddinovich."),
        await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Bosh Menu yoki Orqaga qaytishni hohlasangiz👇🏻",
                         reply_markup=keyboard7)
    elif callback_query.data == 'rektormas':
        keyboard7 = InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(f"Bosh Menu", callback_data='boshmenu'),InlineKeyboardButton(f"Orqaga", callback_data='orqaga1')]
        keyboard7.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Sizga ADTI Institut xotin qizlar masalalari bo'yicha REKTOR maslahatchisi rasmi yuborildi."),
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=rasim4, caption="Institut xotin qizlar masalalari bo'yicha REKTOR maslahatchisi:\nXolmatova Gulhayo Azimjonovna."),
        await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Bosh Menu yoki Orqaga qaytishni hohlasangiz👇🏻",
                         reply_markup=keyboard7)
    elif callback_query.data == 'Davdekanzam':
        keyboard7 = InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(f"Bosh Menu", callback_data='boshmenu'),InlineKeyboardButton(f"Orqaga", callback_data='orqaga1')]
        keyboard7.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Sizga ADTI Davolash fakulteti yoshlar masalalari bo'yicha dekan o'rinbosari rasmi yuborildi."),
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=rasim5, caption="Institut Davolash fakulteti yoshlar masalalari bo'yicha dekan o'rinbosari:\nO'lmasov Murodjon Mahmudovich."),
        await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Bosh Menu yoki Orqaga qaytishni hohlasangiz👇🏻",
                         reply_markup=keyboard7)
    elif callback_query.data == 'davzam2':
        keyboard7 = InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(f"Bosh Menu", callback_data='boshmenu'),InlineKeyboardButton(f"Orqaga", callback_data='orqaga1')]
        keyboard7.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="Sizga ADTI 2-kurs Davolash ishi fakulteti DEKAN o'rinbosari rasmi yuborildi."),
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=rasim6, caption="Institut 2-kurs Davolash ishi fakulteti DEKAN o'rinbosari:Kamalov Botirjon Bahtiyorovich."),
        await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Bosh Menu yoki Orqaga qaytishni hohlasangiz👇🏻",
                         reply_markup=keyboard7)
    elif callback_query.data == 'batafsil':
        keyboard7 = InlineKeyboardMarkup()
        buttons = [InlineKeyboardButton(f"Bosh Menu", callback_data='boshmenu')]
        keyboard7.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="ADTI Info bot nima uchun kerak...?🤔"),
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=rasim7, caption="Assalomu alekum aziz foydalanuvchi.\nSiz ADTI Info rasmiy botidan o'zingizni grupa dars jadvalingizni , ADTI nufuzlik shahslarning malumotlarini va KAFEDIRA MUDIRlarini rasmi hamda telegram profili yoki mobil telefon raqamini topa olasiz.\n\n\nBOTni yaratishdan maqsad har bir talaba o'z oliy talim muasasasining har bir nufuzlik shahsini tanishi va kerak bo'lsa ular bilan aloqada bo'lishni YENGILLATISHDAN iborat.\n\n\nSiz bot orqalik Davolash ishi fakultetining 2-kurs dekan o'rinbosari bilan to'g'ridan to'g'ri aloqada bo'lasiz.\n\n\nBotda yana bir qancha muhum VAZIFALAR mavjud bo'lib siz buni botdan foydalanish davomida bilib olasiz."),
        await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Bosh Menuga qaytishni hohlasangiz👇🏻",
                         reply_markup=keyboard7)
    elif callback_query.data == 'bothaqida1':
        keyboard = InlineKeyboardMarkup(row_width=2)
        buttons = [InlineKeyboardButton(f"Kamalov.B.B", url='t.me/+998932561551'),InlineKeyboardButton(f"Umarov.B.B", url='https://t.me/bahrombek_adti'),InlineKeyboardButton(f"Bosh Menu", callback_data='boshmenu')]
        keyboard.add(*buttons)
        await bot.edit_message_text(chat_id=callback_query.message.chat.id,
                                    message_id=callback_query.message.message_id,
                                    text="ADTI bot haqida malumotlar...😎"),
        await bot.send_photo(chat_id=callback_query.message.chat.id, photo=rasim7, caption=f"Assalomu alekum.\nBot nomi: ADTI Info.\nBot usernamesi:@ADTI_bot.\nBot mualifi:Kamalov Botirjon Bahtiyorovich.\nBot admini:Kamalov Botirjon Bahtiyorovich.\nBot yuzasidan taklif va shikoyatlar uchun:Kamalov Botirjon Bahtiyorovich\nBot yaratuvchisi:Umarov Bahrombek Nodirbekvich.\n\n\nBot yaratilishidan maqsad:Talabalarga qulaylik va harbir OTM rahbariyatlarini yaqindan tanitish."),
        await bot.send_message(chat_id=callback_query.message.chat.id,
                         text="Bosh Menu , Kamalov.B.B va Umarov.B.N shaxsiy telegram chatlari uchun👇🏻.",
                         reply_markup=keyboard)
    
   
    
     
        

   

















if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
