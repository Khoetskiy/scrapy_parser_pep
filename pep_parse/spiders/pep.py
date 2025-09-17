import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Парсит главную страницу PEP и собирает ссылки на отдельные PEP."""
        links = (
            response.xpath('//section[@id="index-by-category"]')
            .xpath('.//a[@class="pep reference internal"]/@href')
            .getall()
        )
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсит отдельные страницы PEP."""
        title = response.xpath('//section[@id="pep-content"]/h1/text()').get()

        if not title:
            return

        try:
            number = int(title.split()[1])
            name = title.split('–')[-1].strip()
        except (IndexError, ValueError):
            return

        status = response.xpath(
            '//dl/dt[contains(., "Status")]/following-sibling::dd[1]/abbr/text()'  # noqa: E501
        ).get()

        yield PepParseItem(number=number, name=name, status=status)
