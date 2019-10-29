import tkinter
import tkinter.messagebox


'''
创建一个顶层窗口对象并用它来承载整个GUI应用。
在顶层窗口对象上添加GUI组件。
通过代码将这些GUI组件的功能组织起来。
进入主事件循环(main loop)。
'''


def main():
    flag=True
    def change_label_text():
        nonlocal flag
        flag=not flag
        color,msg=('red','Hello,world!')\
            if flag else ('blue','Goodbye,world!')
        label.config(text=msg,fg=color)

    def confirm_to_quit():
        #tkinter的自带事件
        if tkinter.messagebox.askokcancel('warning', 'RU sure?'):
            top.quit()

    # 创建顶层窗口
    top=tkinter.Tk()
    top.geometry('240x160')
    top.title('Game')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    # 点这个button 会调用哪个函数,这个函数对所有对象都可以操作
    button1=tkinter.Button(panel,text='modify',command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    top.mainloop()

if __name__ == '__main__':
    main()
