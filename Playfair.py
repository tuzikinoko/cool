
# coding: utf-8

# In[ ]:


##Playfair算法
#字母表
letter_list='ABCDEFGHIKLMNOPQRSTUVWXYZ'
#密码表
T_letter=['','','','','']
#根据密钥建立密码表
def Create_Matrix(key):
    key=Remove_Duplicates(key)  #移除密钥中的重复字母
    key=key.replace(' ','') #去除密钥中的空格
  
    for ch in letter_list:  #根据密钥获取新组合的字母表
        if ch not in key:
            key+=ch
  
    j=0
    for i in range(len(key)): #将新的字母表里的字母逐个填入密码表中，组成5*5的矩阵
        T_letter[j]+=key[i]     #j用来定位字母表的行
        if 0==(i+1)%5:
            j+=1
#移除字符串中重复的字母
def Remove_Duplicates(key):
    key=key.upper() #转成大写字母组成的字符串
    _key=''
    for ch in key:
        if ch=='J':
            ch='I'
        if ch in _key:
            continue
        else:
            _key+=ch
    return _key
 
#获取字符在密码表中的位置
def Get_MatrixIndex(ch):
    for i in range(len(T_letter)):
        for j in range(len(T_letter)):
            if ch==T_letter[i][j]:
                return i,j #i为行，j为列
 #加密
def jia_mi4(s,T_letter):
    ciphertext=''
  
    if len(s) % 2 !=0:  #如果新的明文长度为奇数，在其末尾添上'Z'
        s+='X'
    i=0
    while i<len(s): #对明文进行遍历
        if True==s[i].isalpha():  #如果是明文是字母的话，
            j=i+1                           #则开始对该字母之后的明文进行遍历，
            while j<len(s):         #直到遍历到字母，进行加密
                if True==s[j].isalpha():
                    if 'J'==s[i].upper():             #
                        x=Get_MatrixIndex('I')                  #
                    else:                                     #
                        x=Get_MatrixIndex(s[i].upper()) #对字符在密码表中的坐标
                    if 'J'==s[j].upper():             #进行定位,同时将'I'作为
                        y=Get_MatrixIndex('I')                #'J'来处理
                    else:                                     #
                        y=Get_MatrixIndex(s[j].upper()) #
          
                    if x[0]==y[0]:    #如果在同一行
                        ciphertext+=T_letter[x[0]][(x[1]+1)%5]+T_letter[y[0]][(y[1]+1)%5]
                    elif x[1]==y[1]:  #如果在同一列
                        ciphertext+=T_letter[(x[1]+1)%5][x[0]]+T_letter[(y[1]+1)%5][y[0]]
                    else:             #如果不同行不同列
                        ciphertext+=T_letter[x[0]][y[1]]+T_letter[y[0]][x[1]]
                    break;  #每组明文对加密完成后，结束本次对明文的遍历
                j+=1
            i=j+1  #每次对明文的遍历是从加密过后的明文的后一个明文开始的,结束本次循环
            continue
        else:
            ciphertext+=s[i]  #如果明文不是字母，直接加到密文上
        i+=1 
    return ciphertext
 #解密
def jie_mi4(s,T_letter):
    plaintext=''
    if len(s) % 2 !=0:  #如果新的密文长度为奇数，在其末尾添上'Z'
        s+='X'
    i=0
    while i<len(s): #对密文进行遍历
        if True==s[i].isalpha():  #如果是密文是字母的话，
            j=i+1                            #则开始对该字母之后的密文进行遍历，
            while j<len(s):         #直到遍历到字母，进行解密
                if True==s[j].isalpha():
                    if 'J'==s[i].upper():              #
                        x=Get_MatrixIndex('I')                    #
                    else:                                       #
                        x=Get_MatrixIndex(s[i].upper())  #对字符在密码表中的坐标
                    if 'J'==s[j].upper():              #进行定位,同时将'I'作为
                        y=Get_MatrixIndex('I')                  #'J'来处理
                    else:                                       #
                        y=Get_MatrixIndex(s[j].upper())  #
          
                    if x[0]==y[0]:    #如果在同一行
                        plaintext+=T_letter[x[0]][(x[1]-1)%5]+T_letter[y[0]][(y[1]-1)%5]
                    elif x[1]==y[1]:  #如果在同一列
                        plaintext+=T_letter[(x[1]-1)%5][x[0]]+T_letter[(y[1]-1)%5][y[0]]
                    else:             #如果不同行不同列
                        plaintext+=T_letter[x[0]][y[1]]+T_letter[y[0]][x[1]]
                    break;  #每组密文对解密完成后，结束本次对密文的遍历
                j+=1
            i=j+1  #每次对密文的遍历是从解密过后的密文的后一个密文开始的,结束本次循环
            continue
        else:
            plaintext+=s[i]  #如果密文不是字母，直接加到明文上
        i+=1
    return plaintext
def main():
    a=int(input('加密请按1，解密请按2：'))
    if a==1:
        s=input('请输入明文：')
        k=input('请输入密钥：')
        Create_Matrix(k)
        print(jia_mi4(s,T_letter))
    else:
        s=input('请输入密文：')
        k=input('请输入密钥：')
        Create_Matrix(k)
        print(jie_mi4(s,T_letter))
if __name__=="__main__":
    mian()

