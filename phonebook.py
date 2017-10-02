
class PhoneBook(object):
    def __init__(self,pbname):
        self.name = pbname
        self.contacts = {}
    def addperson(self,name,number):
        self.contacts[name] = number
    def getnum(self,name):
        try:
            return self.contacts[name]
        except:
            print "Name not found"
            return False
    def getperson(self,num):
        for i in self.contacts:
            if self.contacts[i] == num:
                return i
        print "Number not found"
        return False
    def remperson(self,inp):
        if type(inp) is str:   del self.contacts[inp]
        elif type(inp) is int: del self.contacts[self.getperson(inp)]
        else: return False
    def printbook(self):
        print self.name
        for i in self.contacts:
            print i, "\t:", self.contacts[i]

def main():
    people = PhoneBook("Peeps")
    people.addperson("Leo Kastenberg",5555555555)
    people.addperson("Will Bagel",5318008000)
    people.addperson("Shomas Thaw",4514510451)
    people.printbook()
    print
    people.remperson("Shomas Thaw")
    people.printbook()
    print
    print people.getperson(5555555555)
    print people.getnum("Leo Kastenberg")

if __name__ == "__main__":
    main()
