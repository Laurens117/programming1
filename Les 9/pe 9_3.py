def studentencijfers(cijfers):
    for i in cijfers:
        if cijfers[i]>9:
            print(i, cijfers[i])

cijfers={'Laurens': 10, 'Jan': 6.6,'Henk': 4,'Jean': 4.2,'Jody': 9.9,'Charlie': 9,'Nikki': 9.5,'Mickey': 6.8}

studentencijfers(cijfers)