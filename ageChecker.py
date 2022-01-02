
class ageChecker:

    def __init__(self,ages,agelimit,**args):
        self.ageLimit = agelimit
        self.checked = [x for x in ages if int(x) >= self.ageLimit]
        self.checkedf = [x for x in ages if int(x) <= self.ageLimit]

        for k,v in args.items():
            if k == "sort" and v == True:
                self.checked = sorted(self.checked,key=int)

    def ac_list(self,values):
        created = {None}
        for v in values:

            created.add(v)

        created.remove(None)
        return list(created)

    def age_check(self,**p):
        for k,v in p.items():
            if k == "print" and v == True:
                print(self.checked)
            
            if k == "printf" and v == True:
                if len(self.checkedf) == 0:
                    print(None)
                else:
                    print(self.checkedf)

        return self.checked


if __name__ == '__main__':
    ac = ageChecker([55,70,16,24],30,sort=True)
    ac_arr = ac.ac_list([34,30,57,76,24,36])

    ac2 = ageChecker(ac_arr,40,sort=True)
    ac2.age_check(print=True,printf=True)
