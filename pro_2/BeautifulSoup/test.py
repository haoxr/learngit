#import py3_effective_url
import random

if (1,2) is set():
    print('OK')
print(set())
# py3_effective_url.get_local_pages()


def test():
    page = set()
    for i in range(5):
        a = random.randint(1,10)
        if a not in page:
            page.add(a)
    return page


for i in range(2):
    print('第%s遍：' % i,test())


