
def solvefor(tb,top):
    final = 1
    if top:
        for i in tb[1]:
            final = final * i
        for i in tb[0]:
            final = final / i
    else:
        for i in tb[0]:
            final = final * i
        for i in tb[1]:
            final = final / i
    return final

def main():
    curtb = [[raw_input("P >> "),raw_input("V >> ")],[raw_input("n >> "),raw_input("R >> "),raw_input("T >> ")]]
    for j in range(2):
        i = len(curtb[j]) - 1
        while i >= 0:
            try:
                curtb[j][i] = float(curtb[j][i])
            except ValueError:
                curtb[j].pop(i)
            i -= 1
    top = "" in curtb[0]
    print(solvefor(curtb,top))

if __name__ == "__main__":
    main()
