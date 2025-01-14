# 请在下面的 Begin-End 之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 使用 with 语句读取文件中指定位置的内容
path = input()
start = int(input())     # 读取内容的开始位置
end = int(input())     # 读取内容的结束位置
with open(path,"r",) as f:
    f.seek(start)
    value = end - start
    print(f.read(value))
########## End ##########