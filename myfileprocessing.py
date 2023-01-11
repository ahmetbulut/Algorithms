try:
    f = open('sample/mydataXYZ.txt', 'r')
    #f.write("Trying ...")
except FileNotFoundError:
    raise ValueError("Why not!")

