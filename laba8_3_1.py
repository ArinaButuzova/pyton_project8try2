from PIL import Image, ImageDraw, ImageFont
import sys


holiday_cards = {
    "день рождения": "birthday_card.jpg",
    "рождество": "christmas_card.jpg",
    "пасха": "easter_card.jpg",
    }
holiday = input("К какому празднику вам нужна открытка? День рождения, Рождество или Пасха?").lower()
name = input("Кого вы хотите поздравить? Введите имя")
if holiday in holiday_cards:
    card_filename = holiday_cards[holiday]
    image = Image.open(card_filename)
    idraw = ImageDraw.Draw(image)
    text = name + ", поздравляю"

    font = ImageFont.truetype("comic.ttf", size=60)

    idraw.text((390, 30), text, fill=(255, 0, 0), font=font, bold=True)

    image.save('card_new.png')
    image.show()
else:
    print("Извините, открытки для этого праздника не найдено.")
