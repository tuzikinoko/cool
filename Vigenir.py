
# coding: utf-8

# In[ ]:


def jia_mi3(s,k):      #维吉尼亚加密
    resault=''     #放结果
    row=len(k)     #key长度作为行
    column=len(s)   #明文作为列数
    for i in range(0,column):    # 循环message
        a=i%row       #确认密文对应的key中的字母
        c=(ord(s[i])+ord(k[a])-129)
        #通过明文和key计算密文中z之前的密文
        if c>90:        #计算密文中z之后的的密文
            d=chr(c-26)
        else:
            d=chr(c)
        resault+=d
    return resault
def jie_mi3(s,k):       # 维吉尼亚解密
    resault=''
    row=len(k)
    column=len(s)
    for i in range(column):
        a=i%row
        b=(ord(s[i])+32-ord(k[a]))
        if b>=0: #通过密文和key计算明文中z前的明文
            c=chr(b+97)
        else:   #通过密文和key计算明文中z之后的明文
            c=chr(97+b+26)
        resault+=c
    return resault

def main():
    a=int(input('加密输1，解密输2:'))
    if a==1:
        s=input('请输入明文：')
        k=input('请输入密钥：')
        print(jia_mi3(s,k))
    else:
        s=input('请输入密文：')
        k=input('请输入密钥：')

