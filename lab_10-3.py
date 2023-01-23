# Creator JM 1/23/23

def double_stuff(list):
    for i, v in enumerate(list):
        list[i] = v * 2
    print(list)

double_stuff([1,2,3])
double_stuff([1,2.22,3])
double_stuff([1,2.22,'hi'])
