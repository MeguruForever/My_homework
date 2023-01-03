with open('largefile.txt', 'rb') as f:     
    line_count =0
    for line in f:
        line_count += 1
    print(f"文件的行数：{line_count}")
while True:
    line_number = int(input('请输入行号：'))
    with open('largefile.txt', 'rb') as f:
        f.seek(line_number * 2)
        line = f.readline().decode()
        print(line)