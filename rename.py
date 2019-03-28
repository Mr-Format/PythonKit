import os
def reName(fpath,st=''):
	lt = os.listdir(fpath)
	i = 1
	abslt = []
	for x in lt:
		abslt.append(os.path.join(fpath,x))
	for x in abslt:
		if os.path.isfile(x):
			s = os.path.splitext(x)[1]
			os.rename(x,'{}\\{}{}{}'.format(fpath,st,i,s))
			i += 1
print("该程序将目标目录下的文件（不包含文件夹）全部格式化重命名！！！")
ld = input("请输入文件所在目录（如：D:\\program\\下载...）：")
ls = input("""
	请输入格式化名称，可以不输入直接按回车键
	如：输入name，则目录下全部文件改名为name1，name2，...
	:""")
reName(ld,ls)
input("输入任意键结束：")