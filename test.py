def test_yield():
    print("Jump into function, test_yield()")
    i = 1
    while True:
        rtn = yield i
        # print(f"rtn: {rtn}")
        i+=1