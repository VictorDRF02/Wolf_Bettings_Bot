import os
from dotenv import load_dotenv 
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, 
    ContextTypes
)

# Telegram groups and admin links
GROUP_1 = "https://t.me/alejesuszcryptos"
GROUP_2 = "https://t.me/alejesusz_comunidad"
ADMIN = "https://t.me/alejesusz"

menus = {
    "principal": {
        "keyboard": [
            [InlineKeyboardButton("🏆 APUESTAS 🏆", callback_data="bets")],
            [InlineKeyboardButton("👤 CUENTA", callback_data="acount")],
            [InlineKeyboardButton("🎁 BONO REFERIDO", callback_data="refer")],
            [InlineKeyboardButton("💬 SOPORTE", callback_data="support")],
            [InlineKeyboardButton("📢 CANAL", url=GROUP_1)],
            [InlineKeyboardButton("👥 COMUNIDAD", url=GROUP_2)]
        ],
        "reply_text": '¡Hola! \n \n🐺 ¡Bienvenido a Wolf Bettings! 🏆 Prepárate para una experiencia de apuestas emocionantes, llena de acción y oportunidades para ganar. 🤩 \n \n¡Que la suerte te acompañe! 🍀'
    },
    "bets": {
        "keyboard": [
            [InlineKeyboardButton("🎫 Ver apuestas activas", callback_data="ver_apuestas")],
            [InlineKeyboardButton("⚽️ FÚTBOL", callback_data="soccer"), 
             InlineKeyboardButton("🏀 BALONCESTO", callback_data="baloncesto")],
            [InlineKeyboardButton("⚾️ BEISBOL", callback_data="beisbol"), 
             InlineKeyboardButton("🏈 F. AMERICANO", callback_data="futbol_americano")],
            [InlineKeyboardButton("🎾 TENIS", callback_data="tenis"), 
             InlineKeyboardButton("🏒 HOCKEY", callback_data="hockey")],
            [InlineKeyboardButton("🤝 Apuesta combinada",  callback_data="combinada")],
            [InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="principal")]
        ],
        "reply_text": 'Únete a la diversion 🎉 Apuesta ahora en tu deporte favorito 🏈 ¡E𝗌 hora de jugar! 🎲'
    },
    "acount": {
        "keyboard": [
            [InlineKeyboardButton("📥 DEPOSITAR", callback_data="depositar"), 
             InlineKeyboardButton("📤 RETIRAR", callback_data="retirar")],
            [InlineKeyboardButton("⚙️ OPCIONES", callback_data="options")],
            [InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="principal")]
        ],
        "reply_text": 'Mi cuenta Wolfbettings 🐺 \n\n👤Nombre: -- \n🆔ID: -- \n\n🎟Apuestas activas: XXXX \n\n💰SALDO : 000000 CUP \n💳 CUENTA :  CUP \n💳TARJETA DE CRÉDITO: XXXX XXXX XXXX XXXX'
    },
    "refer": {
        "keyboard": [
            [InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="principal")]
        ],
        "reply_text": '🎁 Menú de Referidos:\n\n❌ Esta sección todavía no está disponible'
    },
    "support": {
        "keyboard": [
            [InlineKeyboardButton("💬 Contactar al admin", url=ADMIN)],
            [InlineKeyboardButton("❔ Preguntas Frecuentes", callback_data="faq")],
            [InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="principal")]
        ],
        "reply_text": '¡Hola! 👋 ¿Necesitas ayuda? \n\nEstamos aquí para ayudarte con cualquier duda o problema que puedas tener.'
    },
    "options": {
        "keyboard": [
            [InlineKeyboardButton("💳 Agregar Tarjeta de Crédito", callback_data="agregar_tarjeta")],
            [InlineKeyboardButton("📊 Historial de apuestas", callback_data="historial")],
            [InlineKeyboardButton("🔙 VOLVER", callback_data="menu_cuenta"), InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="menu_principal")]
        ],
        "reply_text": 'Opciones de tu cuenta Wolfbettings 🐺: \n\n💳 Gestiona tu tarjeta de crédito \n📊 Revisa tu historial de apuestas'
    },
    "soccer": {
        "keyboard": [
            [InlineKeyboardButton("🇪🇸 ESPAÑA", callback_data="españa"), 
             InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 INGLATERRA", callback_data="inglaterra")],
            [InlineKeyboardButton("🇫🇷 FRANCIA", callback_data="francia"), 
             InlineKeyboardButton("🇩🇪 ALEMANIA", callback_data="alemania")],
            [InlineKeyboardButton("🇮🇹 ITALIA", callback_data="italia"), 
             InlineKeyboardButton("🇺🇸 ESTADOS UNIDOS", callback_data="estados_unidos")],
            [InlineKeyboardButton("🔙 VOLVER", callback_data="bets"), 
             InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="principal")]
        ],
        "reply_text": '¡Prepárate para la emoción del fútbol! \n\n🤩 Elige a tu liga favorita y realiza tus apuestas 🏟'
    },
}
"""
Contains the information of the menus by the next format:\n
```
{
    "menuName": {
        "keyboard" [
            # Keys to show in the keyboard
        ],
        "reply_text": "Text to show in the menu reply message"
    }
}
```
"""

async def show_menu(update, menu_options):
    """Shows a menu by the menu_options param"""
    print(menu_options)
    reply_markup = InlineKeyboardMarkup(menu_options['keyboard'])
    query = update.callback_query
    if query:
        await query.answer()
        await query.edit_message_text(
            menu_options['reply_text'],
            reply_markup=reply_markup
        )
    else: 
        await update.message.reply_text(menu_options['reply_text'],reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Method that runs at the program start and displays the principal menu"""
    await show_menu(update=update, menu_options=menus['principal'])

async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handles request and displays the corresponding menus.\n
    For example: `query.data == 'principal'` shows the principal menu
    """
    query = update.callback_query
    await query.answer()

    # Navegación entre menús
    try:
        await show_menu(update=update, menu_options=menus[query.data])
    except:
        await query.message.reply_text(f'Todavía no se ha definido nada para esta opción: {query.data}')

# CONFIGURACIÓN DEL BOT Y HANDLERS
def main():
    load_dotenv()  

    application = ApplicationBuilder().token(os.getenv("TOKEN")).build()

    # Handlers para comandos y navegación
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(menu_handler))
    
    # Inicia el bot
    print("Bot iniciado...")
    application.run_polling()

if __name__ == "__main__":
    main()
