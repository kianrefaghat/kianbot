from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# =========================
# BOT CONFIG
# =========================

TOKEN = "8751283530:AAFvbBLjxpErRTjBrUHq5MwyKoDycc-CW14"
TELEGRAM_USERNAME = "kian_ref"
PHONE_NUMBER = "09213596215"

CERTIFICATE_1 = (
    "https://uploadkon.ir/uploads/4f2a26_26photo-5891108045666849368-y.jpg"
)

CERTIFICATE_2 = "https://example.com/certificate2"
PROJECT_LINK = "https://example.com"


# =========================
# MAIN MENU
# =========================

def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("👤 درباره من", callback_data="about"),
            InlineKeyboardButton("💼 نمونه‌کارها", callback_data="portfolio"),
        ],
        [
            InlineKeyboardButton("🛠 خدمات من", callback_data="services"),
            InlineKeyboardButton("📄 رزومه و مدارک", callback_data="documents"),
        ],
        [
            InlineKeyboardButton("🧠 توانایی‌های من", callback_data="skills"),
        ],
        [
            InlineKeyboardButton("📞 تماس با من", callback_data="contact"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


# =========================
# START
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
╔══════════════════════╗
      KIAN REFA... 
╚══════════════════════╝

💻 Python Developer
🤖 Telegram Bot Developer
⚙️ Backend & Automation

به پورتفولیوی شخصی من خوش آمدید.

از منوی زیر می‌توانید اطلاعات،
نمونه‌کارها، خدمات و راه‌های ارتباطی
را مشاهده کنید.
"""

    await update.message.reply_text(
        text,
        reply_markup=main_menu()
    )


# =========================
# ABOUT
# =========================

async def about(update, context):

    text = """
👤 درباره من

سلام! من کیان رفاقت هستم.

💻 Python Developer — سطح بالا
🤖 Telegram Bot Developer
⚙️ Backend Developer

در زمینه توسعه نرم‌افزار و ساخت
ابزارهای کاربردی فعالیت می‌کنم.

تمرکز من روی ساخت پروژه‌های:

• سریع
• تمیز
• قابل توسعه
• کاربردی
• قابل اعتماد

🔗 GitHub
به‌زودی...
"""

    keyboard = [
        [InlineKeyboardButton("🏠 منوی اصلی", callback_data="home")]
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# PORTFOLIO
# =========================

async def portfolio(update, context):

    text = """
💼 نمونه‌کارها

🤖 Kian Portfolio Bot

ربات تلگرام شخصی برای معرفی
مهارت‌ها، خدمات، مدارک و نمونه‌کارها.

━━━━━━━━━━━━━━

🐍 Python Automation Tool

ابزارهای اتوماسیون با Python
برای ساده‌سازی کارهای تکراری.

━━━━━━━━━━━━━━

⚙️ REST API Project

پروژه Backend و طراحی API
با تمرکز روی ساختار تمیز و قابل توسعه.

━━━━━━━━━━━━━━

📌 پروژه‌های بیشتر
به‌زودی اضافه می‌شوند.
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "🔗 مشاهده پروژه",
                url=PROJECT_LINK
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# SERVICES
# =========================

async def services(update, context):

    text = """
🛠 خدمات من

🤖 ساخت ربات تلگرام
ساخت ربات‌های کاربردی و حرفه‌ای.

🐍 Python Development
توسعه نرم‌افزار و ابزار با Python.

⚙️ Backend Development
طراحی و توسعه بخش Backend پروژه‌ها.

🔄 Automation
خودکارسازی فرآیندهای تکراری.

🌐 REST API Development
طراحی و توسعه APIهای کاربردی.
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 شروع یک پروژه",
                callback_data="project_request"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# SKILLS
# =========================

async def skills(update, context):

    text = """
🧠 توانایی‌های من

🐍 Python
🤖 Telegram Bot Development
⚙️ Backend Development
🌐 REST API
🔄 Automation
🧹 Clean Code
⚡ Performance
🔐 توجه به امنیت
📈 ساختار قابل توسعه
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ]
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# DOCUMENTS
# =========================

async def documents(update, context):

    text = """
📄 رزومه و مدارک

🏆 دارای دو مدرک رسمی Python

برای مشاهده مدارک روی
دکمه زیر کلیک کنید.
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "📂 مشاهده مدارک",
                callback_data="certificate_list"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# CERTIFICATES
# =========================

async def certificate_list(update, context):

    text = """
🏆 مدارک و گواهینامه‌ها

مدرک Python — ۱
مدرک Python — ۲
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "🏆 مدرک Python — ۱",
                url=CERTIFICATE_1
            )
        ],
        [
            InlineKeyboardButton(
                "🏆 مدرک Python — ۲",
                url=CERTIFICATE_2
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="documents"
            )
        ],
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# CONTACT
# =========================

async def contact(update, context):

    text = f"""
📞 تماس با من

💬 Telegram:
@{TELEGRAM_USERNAME}

📱 Phone:
{PHONE_NUMBER}

برای ارتباط مستقیم می‌توانید
از دکمه زیر استفاده کنید.
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "💬 پیام در تلگرام",
                url=f"https://t.me/{TELEGRAM_USERNAME}"
            )
        ],
        [
            InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="home"
            )
        ],
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# PROJECT REQUEST
# =========================

async def project_request(update, context):

    text = """
🚀 شروع یک پروژه

برای شروع همکاری، اطلاعات زیر را
برای من ارسال کنید:

1️⃣ نوع پروژه
2️⃣ توضیح کوتاه پروژه
3️⃣ امکانات مورد نیاز
4️⃣ زمان تقریبی تحویل

سپس از طریق تلگرام با من
در ارتباط باشید.
"""

    keyboard = [
        [
            InlineKeyboardButton(
                "💬 ارتباط در تلگرام",
                url=f"https://t.me/{TELEGRAM_USERNAME}"
            )
        ],
        [
            InlineKeyboardButton(
                "🔙 بازگشت",
                callback_data="services"
            )
        ],
    ]

    await update.callback_query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# HOME
# =========================

async def home(update, context):

    await update.callback_query.edit_message_text(
        "🏠 منوی اصلی\n\nلطفاً یک گزینه را انتخاب کنید:",
        reply_markup=main_menu()
    )


# =========================
# BUTTON HANDLER
# =========================

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "about":
        await about(update, context)

    elif query.data == "portfolio":
        await portfolio(update, context)

    elif query.data == "services":
        await services(update, context)

    elif query.data == "skills":
        await skills(update, context)

    elif query.data == "documents":
        await documents(update, context)

    elif query.data == "certificate_list":
        await certificate_list(update, context)

    elif query.data == "contact":
        await contact(update, context)

    elif query.data == "project_request":
        await project_request(update, context)

    elif query.data == "home":
        await home(update, context)


# =========================
# ERROR HANDLER
# =========================

async def error_handler(update, context):

    print("ERROR:", context.error)


# =========================
# MAIN
# =========================

def main():

    print("BOT IS STARTING...")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    app.add_error_handler(error_handler)

    print("BOT IS RUNNING...")

    app.run_polling()


# =========================
# RUN
# =========================

if __name__ == "__main__":
    main()