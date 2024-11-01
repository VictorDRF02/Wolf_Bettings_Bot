import os
from dotenv import load_dotenv 
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler, 
    ContextTypes, MessageHandler, filters
)

# Enlaces a los grupos de Telegram
GRUPO_1 = "https://t.me/alejesuszcryptos"
GRUPO_2 = "https://t.me/alejesusz_comunidad"
ADMIN = "https://t.me/alejesusz"

# menu_0. MENÚ PRINCIPAL (Solo al iniciar el bot)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🏆 APUESTAS 🏆", callback_data="menu_apuestas")],
        [InlineKeyboardButton("👤 CUENTA", callback_data="menu_cuenta")],
        [InlineKeyboardButton("🎁 BONO REFERIDO", callback_data="menu_referidos")],
        [InlineKeyboardButton("💬 SOPORTE", callback_data="menu_soporte")],
        [InlineKeyboardButton("📢 CANAL", url=GRUPO_1)],
        [InlineKeyboardButton("👥 COMUNIDAD", url=GRUPO_2)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f'¡𝖧𝗈𝗅𝖺! 👋 {update.effective_user.first_name} \n \n🐺 ¡𝖡𝗂𝖾𝗇𝗏𝖾𝗇𝗂𝖽𝗈 a Wolf Bettings! 🏆 Preparate para una experiencia de apuestas 𝖾𝗆𝗈𝖼𝗂𝗈𝗇𝖺𝗇𝗍𝖾𝗌, llena de accion y oportunidaddes para ganar. 🤩 \n \n¡Que la suerte te 𝖺𝖼𝗈𝗆𝗉𝖺𝗇‌𝖾! 🍀', 
        reply_markup=reply_markup)

# menu_0 Función para mostrar el Menú Principal desde cualquier lugar
async def mostrar_menu_principal(query):
    keyboard = [
        [InlineKeyboardButton("🏆 APUESTAS 🏆", callback_data="menu_apuestas")],
        [InlineKeyboardButton("👤 CUENTA", callback_data="menu_cuenta")],
        [InlineKeyboardButton("🎁 BONO REFERIDO", callback_data="menu_referidos")],
        [InlineKeyboardButton("💬 SOPORTE", callback_data="menu_soporte")],
        [InlineKeyboardButton("📢 CANAL", url=GRUPO_1)],
        [InlineKeyboardButton("👥 COMUNIDAD", url=GRUPO_2)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        f'¡𝖧𝗈𝗅𝖺! 👋 {query.from_user.first_name} \n \n🐺 ¡𝖡𝗂𝖾𝗇𝗏𝖾𝗇𝗂𝖽𝗈 a Wolf Bettings! 🏆 Preparate para una experiencia de apuestas 𝖾𝗆𝗈𝖼𝗂𝗈𝗇𝖺𝗇𝗍𝖾𝗌, llena de accion y oportunidaddes para ganar. 🤩 \n \n¡Que la suerte te 𝖺𝖼𝗈𝗆𝗉𝖺𝗇‌𝖾! 🍀', 
        reply_markup=reply_markup)

# menu_1. MENÚ DE APUESTAS
async def menu_apuestas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎫 Ver apuestas activas", callback_data="ver_apuestas")],
        [InlineKeyboardButton("⚽️ FÚTBOL", callback_data="futbol"), InlineKeyboardButton("🏀 BALONCESTO", callback_data="baloncesto")],
        [InlineKeyboardButton("⚾️ BEISBOL", callback_data="beisbol"), InlineKeyboardButton("🏈 F. AMERICANO", callback_data="futbol_americano")],
        [InlineKeyboardButton("🎾 TENIS", callback_data="tenis"), InlineKeyboardButton("🏒 HOCKEY", callback_data="hockey")],
        [InlineKeyboardButton("🤝 Apuesta combinada",  callback_data="combinada")],
        [InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="menu_principal")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Unete a la diversion 🎉 Apuesta ahora en tu deporte favorito 🏈 ¡𝖤𝗌 hora de jugar! 🎲", 
        reply_markup=reply_markup)

# menu_2. MENÚ DE CUENTA
async def menu_cuenta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📥 DEPOSITAR", callback_data="depositar"), InlineKeyboardButton("📤 RETIRAR", callback_data="retirar")],
        [InlineKeyboardButton("⚙️ OPCIONES", callback_data="menu_opciones")],
        [InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="menu_principal")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        f"Mi cuenta Wolfbettings 🐺 \n\n👤Nombre: {query.from_user.first_name} \n🆔ID: {query.from_user.id} \n\n🎟Apuestas activas: XXXX \n\n💰SALDO : 000000 CUP \n💳 CUENTA :  CUP \n💳TARJETA DE CRÉDITO: XXXX XXXX XXXX XXXX", 
        reply_markup=reply_markup)

# menu_3. MENÚ DE REFERIDOS
async def menu_referidos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="menu_principal")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("🎁 Menú de Referidos:\n\n❌ Esta sección todavía no está disponible", reply_markup=reply_markup)

# menu_4. MENÚ DE SOPORTE
async def menu_soporte(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💬 Contactar al admin", url=ADMIN)],
        [InlineKeyboardButton("❔ Preguntas Frecuentes", callback_data="faq")],
        [InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="menu_principal")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "¡Hola! 👋 ¿Necesitas ayuda? \n\nEstamos aquí para ayudarte con cualquier duda o problema que puedas tener. ", 
        reply_markup=reply_markup)

# menu_1.1. MENÚ DE FUTBOL (Dentro de Apuestas)
async def menu_futbol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🇪🇸 ESPAÑA", callback_data="españa"), InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 INGLATERRA", callback_data="inglaterra")],
        [InlineKeyboardButton("🇫🇷 FRANCIA", callback_data="francia"), InlineKeyboardButton("🇩🇪 ALEMANIA", callback_data="alemania")],
        [InlineKeyboardButton("🇮🇹 ITALIA", callback_data="italia"), InlineKeyboardButton("🇺🇸 ESTADOS UNIDOS", callback_data="estados_unidos")],
        [InlineKeyboardButton("🔙 VOLVER", callback_data="menu_apuestas"), InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="menu_principal")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "¡𝖯𝗋𝖾𝗉𝖺𝗋𝖺𝗍𝖾 para la 𝖾𝗆𝗈𝖼𝗂𝗈́𝗇 del 𝖿𝗎́𝗍𝖻𝗈𝗅! \n\n🤩 Eige a tu liga favorita y realiza tus apuestas 🏟", 
        reply_markup=reply_markup)

# menu_2.1. MENÚ DE OPCIONES (Dentro de Cuenta)
async def menu_opciones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💳 Agregar Tarjeta de Crédito", callback_data="agregar_tarjeta")],
        [InlineKeyboardButton("📊 Historial de apuestas", callback_data="historial")],
        [InlineKeyboardButton("🔙 VOLVER", callback_data="menu_cuenta"), InlineKeyboardButton("🔝 MENÚ PRINCIPAL", callback_data="menu_principal")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "Opciones de tu cuenta Wolfbettings 🐺: \n\n💳 Gestiona tu tarjeta de crédito \n📊 Revisa tu historial de apuestas", 
        reply_markup=reply_markup)

# CONTROLADOR DE NAVEGACIÓN ENTRE MENÚS
async def menu_navigation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Navegación entre menús
    if query.data == "menu_principal":
        await mostrar_menu_principal(query)

    elif query.data == "menu_apuestas":
        await menu_apuestas(update, context)
    elif query.data == "menu_cuenta":
        await menu_cuenta(update, context)
    elif query.data == "menu_referidos":
        await menu_referidos(update, context)
    elif query.data == "menu_soporte":
        await menu_soporte(update, context)
    
    elif query.data == "futbol":
        await menu_futbol(update, context)
    elif query.data == "menu_opciones":
        await menu_opciones(update, context)
    

    # Opciones adicionales (ejemplo)
    elif query.data == "ver_apuestas":
        await query.message.reply_text("Aquí están las apuestas disponibles.")
        
    elif query.data == "baloncesto":
        await query.message.reply_text("Todavía no hay partidos disponibles")
    elif query.data == "beisbol":
        await query.message.reply_text("Todavía no hay partidos disponibles")
    elif query.data == "futbol_americano":
        await query.message.reply_text("Todavía no hay partidos disponibles")
    elif query.data == "tenis":
        await query.message.reply_text("Todavía no hay partidos disponibles")
    elif query.data == "hockey":
        await query.message.reply_text("Todavía no hay partidos disponibles")
    elif query.data == "combinada":
        await query.message.reply_text("Todavía no hay partidos disponibles")

    elif query.data == "españa":
        await query.message.reply_text("Todavía no hay partidos disponibles en españa")
    elif query.data == "inglaterra":
        await query.message.reply_text("Todavía no hay partidos disponibles en inglaterra")
    elif query.data == "francia":
        await query.message.reply_text("Todavía no hay partidos disponibles en francia")
    elif query.data == "alemania":
        await query.message.reply_text("Todavía no hay partidos disponibles en alemania")
    elif query.data == "italia":
        await query.message.reply_text("Todavía no hay partidos disponibles en italia")
    elif query.data == "estados_unidos":
        await query.message.reply_text("Todavía no hay partidos disponibles en estados unidos")
         
    elif query.data == "depositar":
        await query.message.reply_text("¿Cuánto deseas depositar?")
    elif query.data == "retirar":
        await query.message.reply_text("¿Cuánto deseas retirar?")
    elif query.data == "agregar_tarjeta":
        await query.message.reply_text("Agregando tarjeta de crédito...")
    elif query.data == "historial":
        await query.message.reply_text("Historial de transacciones.")

    elif query.data == "faq":
        await query.message.reply_text("❌ LAs preguntas frecuentes no estan diponibles.")

# CONFIGURACIÓN DEL BOT Y HANDLERS
def main():
    load_dotenv()  

    application = ApplicationBuilder().token(os.getenv("TOKEN")).build()

    # Handlers para comandos y navegación
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(menu_navigation))
    
    # Inicia el bot
    print("Bot iniciado...")
    application.run_polling()

if __name__ == "__main__":
    main()
