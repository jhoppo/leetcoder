def sol1(n: int):
    res_print = [f"{' ' * (n - i)}{' '.join(map(str, str(11 ** i)))}" for i in range(n)]
    for i in res_print:
        print(i)
    return res_print

def sol2(n:int):
    """
    fuck you many bugs XD
    """
    output_list=[]
    for i in range(n):
        tmp_list = [1]
        if i == 0:
            output_list.append([1])
            if n == 1:
                return output_list
        if i == 1:
            output_list.append([1,1])
            if n == 2:
                return output_list
        if i > 1:
            prev_row=output_list[i-1]
            for j in range(len(prev_row)-1,0,-1):
                tmp_out = (prev_row[j]+prev_row[j-1])%10 + (prev_row[j]+prev_row[j+1])//10 if j < len(prev_row)-1 else (prev_row[j]+prev_row[j-1])%10
                tmp_list.insert(0, tmp_out)
            tmp_list.insert(0, prev_row[0]+(prev_row[0]+prev_row[1])//10 if (prev_row[0]+prev_row[1])>=10 else prev_row[0])
            output_list.append(tmp_list)
    res = list(map(lambda x:[str(i) for i in x] , output_list ))
    res_print = [ f"{' '*(len(res)-i)}{' '.join(res[i])}" for i in range(len(res)) ]
    for rp in res_print: print(rp)
    return res_print
def sol3(n:int):
    # n=4
    return list(map(lambda x:[x], range(n)))