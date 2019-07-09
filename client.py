# -*- coding: utf-8 -*-
# @Time    : 07/01/2019 23:38
# @Author  : weiziyang
# @FileName: client.py
# @Software: PyCharm

from tkinter import *
from socket import *


def encode(string, e, n):
    ciphertext = ''
    for each in string:
        num = ord(each)
        temp = num ** e % n
        code = str(temp).zfill(4)
        ciphertext += code
    return ciphertext


class Encrypyter(object):
    def __init__(self, ip):
        self.ip = ip
        root = Tk()
        root.title("RSA client")
        root.geometry('1000x450')
        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        title = Label(root, text='RSA Client', font=("Arial", 24), width=18, height=2)
        title.grid(row=0, column=1)
        l1 = Label(root, text="        Input e:    ", font=("Arial", 12), width=18, height=2)
        l1.grid(row=1, column=0)
        self.e1 = Entry(root, textvariable=var1)
        self.e1.grid(row=1, column=1)
        l2 = Label(root, text="        Input n:     ", font=("Arial", 12), width=18, height=2)
        l2.grid(row=1, column=2)
        self.e2 = Entry(root, textvariable=var2)
        self.e2.grid(row=1, column=3)
        self.l3 = Label(root, text="        Input your message:    ", font=("Arial", 12), width=18, height=4)
        self.l3.grid(row=2, column=0)

        self.t = Entry(root, textvariable=var3, width=60)
        self.t.grid(row=2, column=1, )
        self.text = Text(root, height=4, width=80)
        l4 = Label(root, text="        CipherText:    ", font=("Arial", 12), width=18, height=6)
        l4.grid(row=3, column=0)
        self.text.grid(row=3, column=1, rowspan=1)
        l5 = Label(root, text='The encryption process')
        l5.grid(row=4, column=0)
        self.process_text = Text(root, height=10, width=80)
        self.process_text.grid(row=4, column=1, rowspan=5)
        b = Button(root, text='Send the message', width=30, height=2, command=self.encrypt)
        b.grid(row=9, column=0, columnspan=4)
        var1.set("17")
        var2.set('2773')
        self.t.insert(END, 'Attack on the Perl harbor at 9 a.m')
        self.tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        print('start connect')
        self.tcp_client_socket.connect((ip, 5000))
        print('connect success!')
        self.cipher_process = ''
        sock = self.tcp_client_socket.recv(4096).decode()
        var1.set(sock.split(',')[1])
        var2.set(sock.split(',')[0])
        root.mainloop()

    def encrypt(self):
        self.text.delete(1.0, END)
        e = int(self.e1.get())
        n = int(self.e2.get())
        text = self.t.get()
        cipyter_text = self.encode(e, n, text)
        self.process_text.insert(END, self.cipher_process)
        self.text.insert(END, cipyter_text)
        bytes_text = cipyter_text.encode()
        self.tcp_client_socket.send(bytes_text)

    def encode(self, e, n, string):
        ciphertext = ''
        cipher_process = """ """
        for each in string:
            temp_string = str(each) + '\t->\tASCII='
            num = ord(each)
            temp_string += str(num) + '\t->\t{num}^{e} % {n}='.format(num=num, e=e, n=n)
            temp = num ** e % n
            temp_string += str(temp) + '\t->\t'
            code = str(temp).zfill(4)
            temp_string += code + '\n'
            ciphertext += code
            cipher_process += temp_string
        self.cipher_process = cipher_process
        return ciphertext + '\r\n'


if __name__ == "__main__":
    obj = Encrypyter('10.14.184.195')