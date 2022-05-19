from bs4 import BeautifulSoup


class AdvertisementDataParser:

    def __int__(self):
        self.soup = None

    @property
    def post_id(self):
        id_tag = self.soup.select_one(
            'div.col-xxs-6:nth-child(2) > span:nth-child(2)'
        )
        if id_tag:
            return id_tag.text
        return None

    @property
    def property_type(self):
        property_tag = self.soup.select_one(
            'div.col-xxs-6:nth-child(3) > span:nth-child(2)'
        )
        if property_tag:
            return property_tag.text
        return None

    @property
    def floors(self):
        floors_tag = self.soup.select_one(
            '#file-table-md-lg > tr:nth-child(2) > td:nth-child(1)'
        )
        if floors_tag:
            return floors_tag.text
        return None

    @property
    def rooms(self):
        rooms_tag = self.soup.select_one(
            '#file-table-md-lg > tr:nth-child(2) > td:nth-child(3)'
        )
        if rooms_tag:
            return rooms_tag.text
        return None

    @property
    def foundation(self):
        tag = self.soup.select_one(
            '#file-table-md-lg > tr:nth-child(2) > td:nth-child(2)'
        )
        if tag:
            return tag.text
        return None

    @property
    def total_price(self):
        price_tag = self.soup.select_one(
            'div.col-xxs-12:nth-child(15) > span:nth-child(2)'
        )
        if price_tag:
            return price_tag.text.replace('تومان', '').strip()
        return None

    @property
    def unit_price(self):
        price_tag = self.soup.select_one(
            'div.col-xxs-12:nth-child(16) > span:nth-child(2)'
        )
        if price_tag:
            return price_tag.text.replace('تومان', '').strip()
        return None

    @property
    def address(self):
        address_tag = self.soup.select_one(
            'div.row:nth-child(7) > div:nth-child(10) > span:nth-child(2)'
        )
        if address_tag:
            return address_tag.text
        return None

    @property
    def date(self):
        date_tag = self.soup.select_one(
            'div.col-xs-4:nth-child(1) > span:nth-child(2)'
        )
        if date_tag:
            return date_tag.text
        return None

    def parse(self, html_data):
        self.soup = BeautifulSoup(html_data, 'html.parser')
        data = dict(
            post_id=self.post_id, property_type=self.property_type,
            address=self.address, date=self.date, floors=self.floors,
            rooms=self.rooms, foundation=self.foundation,
            unit_price=self.unit_price, total_price=self.total_price,
        )
        return data
