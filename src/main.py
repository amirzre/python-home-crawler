import sys
from crawl import LinkCrawler, DataCrawler


if __name__ == '__main__':
    switch = sys.argv[1]
    if switch == 'find_links':
        crawler = LinkCrawler()
        crawler.start(store=True)
    elif switch == 'extract_data':
        crawler = DataCrawler()
        crawler.start(store=True)
