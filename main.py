import datetime
import random

date = datetime.datetime.now().date()
max_length = 60
MESSAGE = [
    'welcome to password maker',
    '密码生成器',
    'author is 4usei ',
    'version =1.1',
    'System Time :' + str(date),
]
print('#' * max_length)
for msg in MESSAGE:
    print('{0:^{1}s}'.format(msg, max_length))
print('#' * max_length)
count = 1
h1 = ['<--', '!!!', '^^^', '$$$', '###', '@@@', '~~~', '***', '+++', '---']
h2 = ['8', '0', '1']
e = ['-->', '!!!', '^^^', '$$$', '###', '@@@', '~~~', '***', '+++', '---']
res=''
#long =max(h1)
while True:
    #command = input("随机生成密码输入（M/m）。输入(E/e)：手动选择密码格式。")
    command = 'xz'#测试用（需删）
    if command.lower() in ['m']:
        # todo 写一个函数 里面使用randon 在设置好的列表随机选择符号<-进行密码位数的设置
        n = input('for which net/为哪个网站设置：')
        while (count <= 4):
            print(str(count) + ':')
            count += 1
            s = random.randint(0, 9)
            p = random.randint(0, 2)  # todo 尝试修改成每个列表的长度再进行操作max_length
            print(h1[s] * 2 + h2[p] * 3 + '(' + n + ')' + h2[p] * 3 + e[s] * 2)
    elif command.lower() in ['xz']:
        print("选择样式0-9：")
        for n in range(len(h1)):
            print(f"{n}.{h1[n]}",end=" ")
        print( )
        print('输入quit返回上一级')
        c = input("请输入：")
        if c.isdigit() and 0 <= int(c) <= 9:
            print("输入的字符是0到9之间的数字。")
            c=int(c)
            res+=h1[c]
            print(res)
        else:
            print('已退出')
            break
else:
    print('wrong input ')
