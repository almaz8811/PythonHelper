class MyList(list):
    def __str__(self):
        return super().__str__().replace(',', ',\n')


if __name__ == '__main__':
    print([1, 2, 3])
    mylist = MyList([1, 2, 3])
    print(mylist)
    print(mylist[1])
    mylist.extend([4, 5])
    print(mylist)
