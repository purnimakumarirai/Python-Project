
with open(r"file.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
