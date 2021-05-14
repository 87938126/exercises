# 第一步 导入包
from tkinter import * #导入包
from tkinter import messagebox # 弹出消息框

# 功能：应用按钮控件和弹出对话框控件
# 作者：摘星

# 第二步  创建顶层窗口对象，并设置相关数据
root =Tk()   #创建一个主窗口，所有的控件都是放在这里面的
root.title("我的第一个gui窗体")  # 标题
root.geometry("600x600+200+100")   #控制主窗口的大小和位置（宽x高+距左边位置+据上边位置）

# 第三步  创建相关控件
btn01=Button(root)   #创建一个(对象)按钮控件，将对象放进主窗口中
btn01["text"]="开始按钮"  #给这个按钮取个名字

# 第四步  确定控件放置位置，并设置单击事件 
btn01.pack()   # 这东西负责布局，就是控件放在主窗口中的位置，如果没有会看不见

def hy(e):
    #这个必须有参数的

    '''单击按钮会发生的事情'''
    messagebox.showinfo("欢迎","欢迎你进入gui的世界")

btn01.bind("<Button-1>", hy) #绑定单击事件

