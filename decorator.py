def ToLower(func):
    def newFunc(args):
        oldResult = func(args)
        newResult = oldResult.lower()
        return newResult
    return newFunc

@ToLower
def UserPrint(say: str) -> str:
    return say