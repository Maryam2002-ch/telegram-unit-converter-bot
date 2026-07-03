# 🔁 Unit Converter Bot

A Telegram bot for converting length and weight units easily.

Available in **English** and **Persian** 🇬🇧🇮🇷.

---

## ✨ Features

- 📏 Length conversion:
  - meters, centimeters, millimeters, micrometers

- ⚖️ Weight conversion:
  - kilograms, grams, milligrams

- 🔄 Compatible unit conversion only
- 📘 Built-in guide (`/guide` or `/راهنما`)
- ❌ Error handling for invalid inputs

---

## 🚀 How to Use / نحوه استفاده

### English 🇬🇧
Send your request in this format: <br>
`number from_unit to to_unit`

Example: `10 meters to centimeters`

---

### Persian 🇮🇷
درخواست خود را به این شکل ارسال کنید: <br>
`عدد واحد_مبدا به واحد_مقصد`

مثال: `10 متر به سانتی متر`


---

## 📁 Project Structure

unit_conversion_bot/ <br>
├── unit_conversion(E)/ # English version <br>
│ ├── unit_conversion_bot.py <br>
│ ├── length_unit_conversion.py <br>
│ └── weight_unit_conversion.py <br>
├── unit_conversion(P)/ # Persian version 🇮🇷 <br>
│ ├── unit_conversion_bot.py <br>
│ ├── length_unit_conversion.py <br>
│ └── weight_unit_conversion.py <br>
├── .gitignore <br>
└── README.md 


---

## 🛠️ Technologies

- Python 3
- pyTelegramBotAPI (telebot)
- python-dotenv

---

## 🔧 Setup

1. Clone the repository:
```bash
git clone https://github.com/Maryam2002-ch/telegram-unit-converter-bot.git
```
2. Install dependencies:
```bash
pip install pyTelegramBotAPI python-dotenv
```
3. Create a .env file: <br>
`token=YOUR_BOT_TOKEN`

4. Run the bot:
```bash
python unit_conversion.py
```
---
⭐ If you found this useful, give it a star!


