list_ = input('Enter list: ')
list_ = list_.split(',')
def func(list_):
    for i in list_:
        print(list_.count(i))
    

func(list_)