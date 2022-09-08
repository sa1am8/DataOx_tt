import asyncio
import datetime

import httpx
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker

from models import Apartment
from postgress import engine


async def parse_html(count: int):
    if count < 0:
        raise ValueError

    urls = [f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page + 1}/c37l1700273'
            for page in range(count)]
    urls[0] = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'
    print(urls)

    async with httpx.AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        res = await asyncio.gather(*tasks)

    return res


Session = sessionmaker(bind=engine)
session = Session()

for page in asyncio.run(parse_html(2)):
    soup = BeautifulSoup(page.text, "html.parser")
    for each_ad in soup.find_all('div', {"class": "clearfix"})[1:]:
        bedrooms = each_ad.find('span', {"class": "bedrooms"}).text.strip()
        bedrooms = ' '.join(bedrooms.split())
        img_source = each_ad.img['src'].strip()
        title = each_ad.find('a', {"class": "title"}).text.strip()
        location = each_ad.find('div', {"class": "location"}).span.text.strip()
        description = each_ad.find('div', {"class": "description"}).text.strip()
        cost = each_ad.find('div', {"class": "price"}).text.strip()
        currency = cost[0]

        date = each_ad.find('span', {"class": "date-posted"}).text.strip()
        if 'ago' in date:
            now = datetime.datetime.now()
            if 'minutes' in date:
                if now.minute < int(date.split()[1]) and now.hour == 0:
                    now = now - datetime.timedelta(1)

            elif 'hour' in date:
                if now.hour - int(date.split()[1]) < 0:
                    now = now - datetime.timedelta(1)

            date = now.strftime("%d-%m-%Y")

        apartment = Apartment(bedrooms=bedrooms, img_source=img_source, title=title, location=location,
                              description=description, cost=cost, currency=currency, date=date)
        print(apartment)
        session.add(apartment)
        #break
    #break

session.commit()
engine.dispose()
