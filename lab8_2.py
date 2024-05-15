from PIL import Image

holiday_cards = {
    "день рождения": "birthday.jpg",
    "рождество": "christmas.jpg",
    "пасха": "easter.jpg",
    }
holiday = input("К какому празднику вам нужна открытка? День рождения, Рождество или Пасха?").lower()

if holiday in holiday_cards:
    card_filename = holiday_cards[holiday]
    image = Image.open(card_filename)
    image.show()
else:
    print("Извините, открытки для этого праздника не найдено.")







