from threading import Timer

def job_scheduler(f, n):
    t = Timer(n/1000 ,f)
    t.start()

def test():
    print('hello,world')