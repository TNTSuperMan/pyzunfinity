import random

def MakeModel(array):
    ret = dict()
    for idx in range(len(array)):
        if idx == 0:
            continue
        if not array[idx - 1] in ret:
            ret[array[idx - 1]] = list()
        ret[array[idx - 1]].append(array[idx])
    return ret

def MakeMarkovText(model, first="", end=""):
    keys = list()
    for key, value in model.items():
        keys.append(key)
    last = random.choice(keys)
    if first != "":
        last = first
    ret = last
    while True:
        if not last in model or last == end:
            rettmp = ret.split(" ")
            ret = "".join(rettmp)
            return ret
        last = random.choice(model[last])
        ret += last