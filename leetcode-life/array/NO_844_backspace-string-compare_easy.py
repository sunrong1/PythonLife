def backspaceCompare(s: str, t: str) -> bool:
    sStack = []
    tStack = []
    for i in s:
        if i != '#':
            sStack.append(i)
        else:
            if sStack:
                sStack.pop()
    for i in t:
        if i != '#':
            tStack.append(i)
        else:
            if tStack:
                tStack.pop()
    if ''.join(sStack) == ''.join(tStack):
        return True
    return False


def backspaceCompare2(s: str, t: str) -> bool:
    sIndex = len(s) - 1
    tIndex = len(t) - 1
    # 从尾部向前后退，后退到第一个字母
    sShartCount = 0
    while sIndex >= 0 or tIndex >= 0:
        while sIndex >= 0:
            if s[sIndex] != '#':
                if sShartCount > 0:
                    sIndex -= 1
                    sShartCount -= 1
                else:
                    break
            else:
                sShartCount += 1
                sIndex -= 1

        tShartCount = 0
        while tIndex >= 0:
            if t[tIndex] != '#':
                if tShartCount > 0:
                    tIndex -= 1
                    tShartCount -= 1
                else:
                    break
            else:
                tShartCount += 1
                tIndex -= 1
        if sIndex < 0 and tIndex < 0:
            return True
        if sIndex < 0 or tIndex < 0:
            return False
        if s[sIndex] != t[tIndex]:
            return False
        sIndex -= 1
        tIndex -= 1
    return True


s = "ab#c"
t = "ad#c"

s = "xywrrmp"
t = "xywrrmu#p"

# s = "bbbextm"
# t = "bbb#extm"

s = "nzp#o#g"
t = "b#nzp#o#g"
print(backspaceCompare2(s, t))
