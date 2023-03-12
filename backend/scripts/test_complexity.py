from datetime import datetime

from backend.services.subtitle import SubtitleSegmenter


doc = ' '.join(['hello world' for _ in range(500)])
ten_doc = ' '.join([doc for _ in range(10)])
hundred_doc = ' '.join([ten_doc for _ in range(10)])



def test_base():
    s.segement('title', doc)
    
def test_ten():
    s.segement('title', ten_doc)

def test_hundred():
    s.segement('title', hundred_doc)

def testit(case, func):
    start = datetime.now()
    for _ in range(100):
        func()    
    print(f'{case} spent {datetime.now() - start}')
    

if __name__ == '__main__':
    s = SubtitleSegmenter({})
    s._save_to_db = lambda x, y: None
    testit('500 words', test_base)
    testit('5000 words', test_ten)
    testit('50000 words', test_hundred)