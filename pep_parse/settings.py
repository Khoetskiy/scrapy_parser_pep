from pep_parse.constants import BOT_NAME, RESULTS_PATH

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]


ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}


FEED_EXPORT_ENCODING = 'utf-8'

FEEDS = {
    f'{RESULTS_PATH}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    },
}
