with open('Names.txt', 'r') as f:
    names = f.readlines()
new_name = input('请输入名字：')
if new_name not in names:
    for i, name in enumerate(names):
        if new_name < name:
            names.insert(i, new_name)
            break
    else:
        names.append(new_name)
with open('new_word.txt', 'w') as f:
    f.writelines(names)