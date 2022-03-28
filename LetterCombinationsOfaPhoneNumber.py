def letterCombinations(digits: str):
    dict_num_letters = {"2":["a","b","c"],
                       "3":["d","e","f"],
                       "4":["g","h","i"],
                       "5":["j","k","l"],
                       "6":["m","n","o"],
                       "7":["p","q","r","s"],
                       "8":["t","u","v"],
                       "9":["w","x","y","z"]}
    if len(digits) == 0:
        return ""
    if len(digits) == 1:
        return dict_num_letters[digits]
    res= dict_num_letters[digits[0]]
    x = 1
    while x<len(digits):
        res = [i+j for j in dict_num_letters[digits[x]] for i in res ]
        x+=1
    return res