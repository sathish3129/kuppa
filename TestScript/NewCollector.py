from urllib.request import urlopen, Request
import re
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                         'AppleWebKit/537.11 (KHTML, like Gecko) '
                         'Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}


def get_href(line=''):
    res_set = re.match(r'^.*href="(.*?)".*$', line)
    if res_set:
        return res_set.group(1)
    return 'Null'

for i in range(1, 250):

    reg_url = 'https://tamilrockers.ws/index.php/forum/116-tamil-bluray-hd-movies/page-' + \
              str(i) + '?prune_day=100&sort_by=Z-A&sort_key=last_post&topicfilter=all'
    try:
        req = Request(url=reg_url, headers=headers)
        readhtml = urlopen(req).read()
    except:
        logging.warning("Ended at {}".format(i))
        exit(1)

    readhtml = urlopen(req).read()
    for d in str(readhtml).split(r'\n'):
        # itemprop="name"
        # print(d)
        res_set = re.match(r'^.*itemprop="name">(.*Maya.*?)<.*$', d)
        if res_set:
            logging.info(res_set.group(1) + ' - ' + get_href(line=prev_line))

        prev_line = d

logging.info('Done')
