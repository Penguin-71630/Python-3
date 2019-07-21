for i in range(int(input())):
    gnome = [int(i) for i in input().split()][1:]
    for index, item in enumerate(gnome, start=gnome[0]):
        if index != item:
            print(gnome.index(item) + 1)
            break
