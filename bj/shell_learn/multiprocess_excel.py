#!/usr/bin/python2.6 
#-*-encoding:utf-8-*-

# -*- coding: utf-8 -*- 
'''
import  xdrlib ,sys
import xlrd
def open_excel(file= 'test.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file= 'test.xlsx',colnameindex=0,by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list
'''
def main():
   ''' 
   tables = excel_table_byindex()
   for row in tables:
       print row
   '''
   tables = excel_table_byname()
   for row in tables:
       print row

#thread threading mutithreading
from time import ctime , sleep
import threading, time

def now():
    return str(time.strftime('%Y-%m-%d %H;%M:%S',time.localtime()))

def music(func):
    for i in range(2):
        print "I was listening to %s. %s" % (func, ctime())
        sleep(4)

def move(func):

    for i in range(2):
        print "I was at %s... %s" % (func, ctime())
        sleep(5)

def my_threads():
    """do something`"""
    print "start at %s" % now()
    threads = []
    t1 = threading.Thread(target=move,args=('阿凡达',))
    t2 = threading.Thread(target=music,args=('让我们荡起双桨',))
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

    print "all is over %s" % ctime()
    print "end at %s " % now()

from multiprocessing import Process
import os
import time

def sleeper(name, seconds):
    print "Process ID# %s" % (os.getpid())
    print "Parent Process ID# %s" % (os.getppid())
    print "%s will sleep for %d seconds" % (name, seconds)
    time.sleep(seconds)

def test_process():
    procs = []
    child_proc = Process(target=sleeper, args=('xqz',5,)) #the comma in the tail is needed
    procs.append(child_proc)
    child_proc2 = Process(target=move, args=('生死之恋',))
    child_proc3 = Process(target=music, args=('让我们荡起双桨',))
    procs.append(child_proc3)
    procs.append(child_proc2)
    for proc in procs:
        proc.start()

    proc.join()
    print "the parent's Parent process : %s,time:%s" % (os.getppid(),now())
    #child_proc.start()

from multiprocessing import Process, Queue

def offer(queue):
    queue.put("Hello World")
    queue.put("This is ZYP zone...")

def Queue_Process():
    q = Queue()
    p = Process(target=offer, args=(q,))
    p.start()
    print q.get()
    #q.pop() # non attr pop
    print q.get()

from multiprocessing import Process, Pipe

def send(conn):
    conn.send("Hello World!!!")
    conn.send("zyp!!!")
    conn.close()

def Pipe_Process():
    parent_conn, child_conn = Pipe()
    p = Process(target=send, args=(child_conn,))
    p.start()
    print parent_conn.recv()
    print parent_conn.recv()

from multiprocessing import Process, Lock

def l(lock, num):
    lock.acquire()
    print "Hello Num: %s" % (num)
    lock.release()
def ll(no,num):
    print "Hello Num: %s" % (num)
    sleep(2)
    print "$$$$ %s" % (num)
def lock_process():
    #lock = Lock()
    lock = 1

    for num in range(20):
        Process(target=ll, args=(lock, num)).start()

if __name__=="__main__":
    #main()
    Pipe_Process()
    lock_process()
    '''
    music('让我们荡起双桨')
    move('阿凡达')
    print "all over %s" % ctime()让我们荡起双桨
    
    child_proc = Process(target=sleeper, args=('xqz',5))
    child_proc2 = Process(target=move, args=('生死之恋',))
    child_proc.start()
    #child_proc.join()
    child_proc2.start()
    child_proc2.join()
    print "the parent's Parent process : %s" % (os.getppid())
    #child_proc.start()
    '''

    #test_process()
    Queue_Process()




