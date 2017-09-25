
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
    print curtb[0]
    print curtb[1]
    for j in range(2):
        for i in range(len(curtb[j])):
            try:
                curtb[j][i] = float(curtb[j][i])
                print "did " + str(curtb[j][i])
            except ValueError:
                print "except " + str(curtb[j][i])
                curtb[j].pop(i)
    print curtb
    top = "" in curtb[0]
    print(solvefor(curtb,top))

if __name__ == "__main__":
    main()
