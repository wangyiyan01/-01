lib = [{'name':'三国演义','author':'罗贯中','price':'100','number':10},
       {'name':'西游记','author':'吴承恩','price':'90','number':0},
       {'name':'水浒传','author':'施耐庵','price':'108','number':20},
       {'name':'红楼梦','author':'曹雪芹','price':'150','number':15},
       {'name':'神雕侠侣','author':'金庸','price':'50','number':55}]
borrow = []
print("欢迎进入图书管理系统!")
while True:
    x = eval(input("1.借书\n2.还书\n3.显示所有书名\n4.退出系统\n"))
    if x == 1:
        a = input("请输入书籍名称或作者名字:")
        for i in range(len(lib)):
            if a == lib[i]['name'] or a == lib[i]['author']:
                print("查找完毕！目前此书还有",lib[i].get('number',0),"本")
                borrow.append(lib[i])
                #b = lib[i].get('number')
                #b -= 1
                lib[i]['number']-=1
                print("成功借阅",lib[i].get('name'),'',lib[i].get('author'),"著 目前此书还有",lib[i].get('number', 0), "本")
            else:
                continue

    elif x == 2:
        a = input("请输入要归还的书籍名称")
        for i in range(len(lib)):
            if a == lib[i]['name']:
                print("查找完毕！目前此书还有", lib[i].get('number', 0), "本")
                #b = lib[i].get('number')
                #b+=1
                lib[i]['number'] +=1
                print("成功归还! 目前此书还有", lib[i].get('number', 0), "本" )
            else:
                print("无法找到该书籍")

    elif x == 3:
        for idx,name in enumerate(lib):
            print("该书籍在图书馆序号为:",idx+1,"其图书信息为:",name)

    elif x == 4:
        break
