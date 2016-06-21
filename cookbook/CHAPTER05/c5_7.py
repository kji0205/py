'''압축된 데이터 파일 읽고 쓰기'''

import gzip
with gzip.open('u_ex150703.log.gz', 'rt', encoding='utf-8') as f:
    text = f.read()

with gzip.open('u_ex150703.log.gz', 'wt') as f:
    f.write('test')
