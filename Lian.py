
# coding: utf-8



zi_mu_biao='ABCDEFGHIJKLMNOPQRSTUVWXYZ'#大写字母表
#将所有字母转换成大写
def da_xie(ming1):
    st=''
    for i in ming1:
        if ord(i) in range(97,123):
            c=ord(i)-32
            st+=chr(c)
        else:
            st+=i
    return st
#将所有字母转换成小写
def xiao_xie(mi1):
    ct=''
    for i in mi1:
        if ord(i) in range(65,91):
            c=ord(i)+32
            ct+=chr(c)
        else:
            ct+=i
    return ct
#加密      
def jia_mi(ming):
    ming2=da_xie(ming) #将明文字母转换成大写
    mi0=''
    for k in range(len(ming2)):                     #将明文中的字母
        for i in range(len(zi_mu_biao)): #对应到字母表里的字母
            if zi_mu_biao[i]==ming2[k]:        #
                if k==0:           #第一个字母直接用自己的索引作为密钥
                    mi0=mi0+zi_mu_biao[(i+i)%26] 
                    j=(i+i)%26                  #返回第一个字母加密后的密文对应的索引
                else:
                    mi0=mi0+zi_mu_biao[(i+j)%26] #后面的字母都是以前面字母加密后的密文字母的索引作为密钥
                    j=(i+j)%26                  
    return mi0
#解密
def jie_mi(mi1):
    mi2=da_xie(mi1) #转换成大写
    ming0=['','']
    for k in range(len(mi2)):                       #遍历密文
        for i in range(len(zi_mu_biao)): #再遍历字母表，将密文对应到字母表中
            if zi_mu_biao[i]==mi2[k]:        #
                if k==0:           #设第一个字母密钥为x，则2x%26=i
                    ming0[0]+=zi_mu_biao[i-(i//2)]#算出密钥x
                    ming0[1]+=zi_mu_biao[i-(i//2+13)]
                    j=i                         #返回当前字母的索引作为下一密文的密钥
                else:                              #后面的算法一样
                    ming0[0]+=zi_mu_biao[i-j] #利用前面字母的索引作为密钥向左移动
                    ming0[1]+=zi_mu_biao[i-j]
                    j=i
    return xiao_xie(ming0[0])+'或'+xiao_xie(ming0[1]) #明文为小写，因此此处转换为小写
def main():
    choice=int(input("加密请按'1'，解密请按'2':")) 
    if choice==1:
        ming=input('请输入明文：')
        print('加密后：',jia_mi(ming))
    else:
        mi=input('请输入密文：')
        print('解密后：',jie_mi(mi))   
if __name__=="__main__":
    main()


def lian_suo():
    s=inp.get()
    if text=='加密' :
        txt.insert(END, jia_mi(s)) 
        inp.delete(0, END)
    else:
        txt.insert(END,jie_mi(s))
        inp.delete(0,END)
def jiami():
    if chooce.current==0:
        lian_suo()
    
    

