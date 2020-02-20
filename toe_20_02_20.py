def getBert(input):
    text = input.lower()
    x = text.split("bert")
    if text.count("bert") != 2:
        return ""
    z = x[1]
    z = z[::-1]
    return z


def getBert2(input):
    text = input.lower()
    if text.count("bert") != 2:
        return ""
    return ((text.split("bert"))[1])[::-1]

print(getBert2("jgfjdnberthellotherWbertsksd"))