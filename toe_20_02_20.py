def getBert(input):
    text = input.lower()
    x = text.split("bert")
    if text.count("bert") != 2:
        return ""
    z = x[1]
    z = z[::-1]
    return z

print(getBert("jgfjdnberthellotherWbertsksd"))