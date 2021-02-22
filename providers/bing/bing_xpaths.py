ALL_RECORDS = ['//li[@class="b_algo"]']

TITLE = ['//h2[1]/a[1]/text()']

DESCRIPTION = [
    '//p[@class="b_paractl"]/text()',
    '//p/strong/text()',
    '//p//strong/text()',
    '//p/text()',
    '//div[@class="b_caption"]//p/*[not(@class="news_dt")]/text()',
    '/span[@class="aCOpRe"]/span/text()',
    '//div[@class="sa_uc"]/@text',
    '//ol[@class="b_dList"]//descendant-or-self::*/text()',
    '//span[@class="aCOpRe"]'
]

URL = [
    '//cite[1]/a[1]/@href/text()',
    '//li[@class="b_algo"][1]/h2[1]/a[1]/@href/text()',
    '//h2/a/@href'
]