from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from ...models import Product


class Command(BaseCommand):
    help = 'Parse rozetka.com'

    def handle(self, *args, **options):
        url = 'https://rozetka.com.ua/ua/notebooks/c80004/'

        responce = requests.get(url)
        html = BeautifulSoup(responce.content,'html.parser')
        
        items = html.find_all(class_='goods-tile__inner')
        for item in items:
            product_name = item.find(class_='goods-tile__heading').span.text
            image = item.find(class_='goods-tile__picture').img['src']

            product_url = item.find(class_='goods-tile__heading')['href']
            product_url += 'characteristics/'

            product_responce = requests.get(product_url)
            product_html = BeautifulSoup(product_responce.content,'html.parser')

            characteristiksCheck = product_html.find_all(class_='characteristics-full__label')
            characteristiks = product_html.find_all(class_='characteristics-full__sub-list')

            seria = characteristiks[0].li.text
            if characteristiksCheck[0].span.text == 'Серія':
                seria = 'None'

            screen_type = characteristiks[2].li.text
            if characteristiksCheck[2].span.text != 'Тип екрана':
                screen_type = 'None'

            video_card = characteristiks[6].li.text
            if characteristiksCheck[6].span.text != 'Відеокарта':
                video_card = 'None'

            ssd_amount = characteristiks[7].li.text
            if characteristiksCheck[7].span.text != 'Обсяг SSD':
                ssd_amount = 'None'

            hdd_amount = characteristiks[7].li.text
            if characteristiksCheck[7].span.text != 'Обсяг HDD':
                hdd_amount = 'None'


            processor = characteristiks[8].li.text
            if characteristiksCheck[8].span.text != 'Процесор':
                processor = 'None'


            ram_amount = characteristiks[10].li.text
            if characteristiksCheck[10].span.text != "Обсяг оперативної пам'яті":
                ram_amount = 'None'


            color = characteristiks[18].li.text
            if characteristiksCheck[18].span.text != 'Колір':
                color = 'None'


            country = characteristiks[24].li.text
            if characteristiksCheck[24].span.text != 'Країна реєстрації бренду':
                country = 'None'

            product = Product(
                product_name = product_name,
                image = image,
                seria = seria,
                screen_type = screen_type,
                video_card = video_card,
                ssd_amount = ssd_amount,
                hdd_amount = hdd_amount,
                processor = processor,
                ram_amount = ram_amount,
                color = color,
                country = country,
            )

            product.save()

        if options['count']:
            print(options['count'])

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--count',
            action='store',
            default=False,
            help='Parse items count',
            required=False,
        )