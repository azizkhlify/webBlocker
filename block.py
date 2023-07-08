from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication



def is_blocked(link:str):
    with open('C:\Windows\System32\drivers\etc\hosts','r') as file :
         blocked_links=[]
         for line in file.readlines():
           if '127'in line and '#' not in line :
               blocked_links.append(line)
    for blocked_link in blocked_links :
        if link in blocked_link:return True
    return False
def block(link:str):
    with open('C:\Windows\System32\drivers\etc\hosts','a') as write_file:
        line='\n127.0.0.1 '+link
        write_file.write(line)

def inblock(link):
    with open('C:\Windows\System32\drivers\etc\hosts','r') as rf:
         lines = rf.readlines()
    with open('C:\Windows\System32\drivers\etc\hosts','w') as write_file:
        for line in lines:
           if link in line :
             pass
           else:
              write_file.write(line)





app=QApplication([])
blocker=loadUi('weblock.ui')
blocker.show()

if is_blocked('facebook'):
    fac=False
    blocker.face.setText('blocked')
else:
    fac=True
    blocker.face.setText('unblocked')
def fac_fun():
    global fac
    if fac:
        block('www.facebook.com') 
        fac=False
        blocker.face.setText('blocked')
    else :
        inblock('www.facebook.com')
        fac=True
        blocker.face.setText('unblocked')

blocker.face.clicked.connect(fac_fun)

if is_blocked('insta'):
    ins=False
    blocker.insta.setText('blocked')
else:
    ins=True
    blocker.insta.setText('unblocked')
def ins_fun():
    global ins
    if ins:
        block('www.instagram.com') 
        ins=False
        blocker.insta.setText('blocked')
    else :
        inblock('www.instagram.com')
        ins=True
        blocker.insta.setText('unblocked')

blocker.insta.clicked.connect(ins_fun)

def blo_fun ():
    link=blocker.new_link.text()
    if  (link[:4]!='www.') or not ('.'  in link[5:-1]):
        blocker.done.clear()
        blocker.already.clear()
        blocker.already.setText('It\'s not a link')
    else:
        if  not is_blocked(link):
           blocker.done.clear()
           blocker.already.clear()
           msg='Done '
           blocker.done.setText(msg)
           block(blocker.new_link.text())
           blocker.new_link.clear()
        else :
           blocker.done.clear()
           blocker.already.clear()
           msg=' already blocked'
           blocker.already.setText(msg)
           blocker.new_link.clear()




blocker.block.clicked.connect(blo_fun)

app.exec_()