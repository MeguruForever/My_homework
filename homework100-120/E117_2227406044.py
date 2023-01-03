with open('filenames.txt') as f:
    a = f.readlines()
    for i in range(len(a)):
        m=a[i].strip()
        with open(m, 'wt') as d:
            d.write(a[i - 1])