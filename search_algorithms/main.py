from utils.HrefExtractor import HrefExtractor

test = HrefExtractor('https://ufu.com.br')
print('ORIGIN:\t' + test.url)
print('HREFs:')
for href in test.hrefs:
    print('\t' + href)