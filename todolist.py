import sys
import socket

Tlist = []
Mlist = []

def Home():
    print(todolist)
    msg = input('add = /add\ncheck = 番号\n\n\n')
    if msg == '/add':
        todoname = input('Todo name plz:')
        TorM = input('T or M?:')
        if TorM == 'T' or 't':
            Tlist.append(todoname)
        elif TorM == 'M' or 'm':
            Mlist.append(todoname)
        else:
            return
