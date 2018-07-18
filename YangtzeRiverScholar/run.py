from scrapy import cmdline

name = 'yangzeRiverScholar'
cmd = 'scrapy crawl {0}'.format(name)

cmdline.execute(cmd.split())