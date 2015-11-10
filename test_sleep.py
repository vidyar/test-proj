import time

def test_sleep(n):
    time.sleep(1/n)
    if n == 40:
        time.sleep(3600 * 4)
