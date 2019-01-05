from threading import Timer

def call_f_after(f, n):
    t = Timer(n/1000 ,f)
    t.start()

def test():
    print('hello,world')