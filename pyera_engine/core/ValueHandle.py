# 将一个列表中每一个元素逐个追加进另一个列表
def listAppendToList(ifList,ofList):
    ifListMax = len(ifList)
    for i in range(0,ifListMax):
        ofList.append(ifList[i])
    return ofList