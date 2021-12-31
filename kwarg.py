import time
def kwarg_linear_search(l,q,**kw):
    status = False
    pos = 0
    for k,v in kw.items():
        if k == "search" and v == True:
            while pos < len(l):
                print(l[pos])
                
                if l[pos] == q:
                    print(f'found : {q} at index : {l.index(pos)}')
                    status = True
                pos += 1
                time.sleep(0.1)
            

        else:
            print(f"list : {l} |\a|  query : {q}")
    print(f'Search Status : {status}')

arr = [1,2,3,4,5,4]

kwarg_linear_search(arr, 4,search=True)


