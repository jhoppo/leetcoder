def my_range(begin:float, end:float, step:float) -> list:
    while begin < end:
        yield begin
        begin += step
