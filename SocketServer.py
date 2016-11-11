#coding:utf-8
#-*-coding='utf-8'-*-
__author__ = 'shenghui'
#!/usr/bin/python
import socket      #导入socket模块
import commands     #导入执行系统命令模块
HOST='192.168.0.109'
PORT = 60001
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP
s.bind((HOST,PORT))
# 套接字绑定IP与端口
s.listen(1)    #开始TCP监听
while 1:
    conn,addr = s.accept()  #接受TCP连接，并返回新的套接字与IP地址
    print('Connected by',addr)
    while 1:
        data=conn.recv(1024) # 把接收的数据实例化
        cmd_status,cmd_result = commands.getstatusoutput(data)  #commands.getstatusoutput执行系统命令（shell命令），返回两个结果，
                                                                # 第一个是状态，成功为0，第二个是执行成功或失败的输出信息
        if len(cmd_result.strip()) == 0:
            conn.sendall('Done.')                   #如果输出结果长度为0，则告诉用户‘完成’
        else:
            conn.sendall(cmd_result)
conn.close()          #关闭连接

