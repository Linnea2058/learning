#***********计算最小割集********
def minmalCutSet(d,s,l,mc):
    #求最小割集，与门-增加最小割集的阶数，或门-增加最小割集的个数
    len1 = len(mc)
    len2 = len(l)
    if s=='and':#实现类似将列表[[1,2],[1,5]]的1替换成[8,9]得：[[1,8,9],[1,8,9]]功能
        #查看d上是否在mc里出现过
        l1 = []  # 记录mc中有d的列表的位置下标
        for i in range(len1):
            if d in mc[i]:
                l1.append(i)
                k = mc[i].index(d)  # 返回的在mc[i]中的下标位置
                del mc[i][k]
                #把d替换成l
                for j in range(len2):
                    mc[i].insert(0,l[j])#与门:增加最小割集的阶数
    else:
        #实现类似将列表[[1,2,3]，[1,5,6],[2,4]]的1替换成[8,9]里的元素得：[[8,2,3],[9,2,3],[8,5,6],[9,5,6],[2,4]]功能
        mcc = []
        l1 = []#记录mc中有d的列表的位置下标
        for i in range(len1):
            if d in mc[i]:
                l1.append(i)
                k=mc[i].index(d)#返回的在mc[i]中 的下标位置
                del mc[i][k]
                y=mc[i].copy()
                a = [y.copy() for _ in range(len2)]
                for j in range(len2):
                    a[j].insert(0,l[j])
                    mcc.append(a[j])
        for i in l1[::-1]:
            del mc[i]

        for j in range(len(mcc)):
            mc.append(mcc[j])
    return mc

#***********故障树中没有重复事件,直接分布算法********
#与门结构发生的概率计算公式
def andStructure(n,di):#n-底事件的个数,li-记录与门相连的事件的概率
    p=1
    for i in di:
        p = p * di[i]
    return p

#或门结构发生的概率计算公式
def orStructure(n,di):#n-底事件的个数
    p=1
    for i in di:
        p = p * (1-di[i])
    p=1-p
    return p


#***********故障树中有重复事件,基于最小割集求顶事件概率：***********
def T_minmalCutSet():#二阶近似法计算底事件
    #将每个最小割集放入dict
    dict1={'x1':0.2,'x2':0.2}
    dict2={'x4':0.25,'x5':0.25}
    dict3={'x4':0.25,'x6':0.1}

    #割集里与门相连，割集间或门相连
    # 一阶
    p1=andStructure(2, dict1)#割集里与门相连
    p2=andStructure(2, dict2)
    p3=andStructure(2, dict3)
    sum=p1+p2+p3#割集间或门相连
    print('一阶近似法得顶事件概率：',sum)

    #二阶 任意两个割集合并
    #dict1+dict2、dict1+dict3、dict2+dict3
    d1=dict1.copy()
    d1.update(dict2)#将dict1和dict2合并
    n=len(d1)
    p1 = andStructure(n, d1)

    d2 = dict1.copy()
    d2.update(dict3)  # 将dict1和dict3合并
    n = len(d2)
    p2 = andStructure(n, d2)

    d3 = dict2.copy()
    d3.update(dict3)  # 将dict2和dict3合并
    n=len(d3)
    p3 = andStructure(n, d3)

    sum -= (p1 + p2 + p3)  # 一阶+二阶
    print('一阶近似法得顶事件概率：',sum)
def result(x,i):
    y = x[3] * x[2] + x[3] * x[0] * x[4] + x[1] * x[2] + x[1] * x[4]#根据最小割集得到的表达式
    if i==0:
        y = x[3] * x[2] + x[3] * x[1] * x[4] + x[0] * x[2] + x[0] * x[4]
        #print(x, y)
        if y != 0:
            return 1
    if i==1:#交换表达式中x[0]和x[1]的位置
        y = x[3] * x[2] + x[3] * x[0] * x[4] + x[1] * x[2] + x[1] * x[4]
        #print(x, y)
        if y != 0:
            return 1
    if i==2:
        y = x[3] * x[0] + x[3] * x[1] * x[4] + x[2] * x[0] + x[2] * x[4]
        #print(x, y)
        if y != 0:
            return 1
    if i==3:
        y = x[0] * x[2] + x[0] * x[1] * x[4] + x[3] * x[2] + x[3] * x[4]
        #print(x, y)
        if y != 0:
            return 1
    if i==4:
        y = x[3] * x[2] + x[3] * x[1] * x[0] + x[4] * x[2] + x[4] * x[0]
        #print(x, y)
        if y != 0:
            return 1
    return 0
def assign(k,b,x,n,i):#将x[s:e]的元素赋值（不包括e），其中有k个为1，其余的为0  x[0]=b(1/0)
    if k==0:#0个1
        x = [0 for i in range(n)]
        x[0] = b
        return result(x,i)
    if k == 1:
        c1=0
        for j in range(1,n):#x[j]=1
            x = [0 for i in range(n)]
            x[0]=b
            x[j]=1
            c1=c1+result(x,i)
        return c1
    if k==2:
        c1=0
        for m in range(1,n):
            for m2 in range(m+1,n):
                x = [0 for i in range(n)]
                x[0] = b
                x[m]=1
                x[m2]=1
                c1 = c1 + result(x,i)
        return c1
    if k==3:
        c1=0
        for m in range(1,n):
            for m2 in range(m+1,n):
                for m3 in range(m2 + 1, n):
                    x = [0 for i in range(n)]
                    x[0] = b
                    x[m]=1
                    x[m2]=1
                    x[m3] = 1
                    c1 = c1 + result(x,i)
        return c1
    if k==4:
        c1=0
        for m in range(1,n):
            for m2 in range(m+1,n):
                for m3 in range(m2 + 1, n):
                    for m4 in range(m3 + 1, n):
                        x = [0 for i in range(n)]
                        x[0] = b
                        x[m]=1
                        x[m2]=1
                        x[m3] = 1
                        x[m4] = 1
                        c1 = c1 + result(x,i)
        return c1
    return 0
##############计算结构重要度###################
def structural_importance(n):#n个底事件
    #给出故障树的表达式：根据最小割集写表达式，割集里乘号连接，割集之间加号连接
    x = [0 for i in range(n)]
    #计算底事件x[i]的结构重要度,需要分别计算x[i]=0/1时的情况，若i!=0,将表达式中x[i]和x[0]交换，转换成计算x[0]=0/1时的情况
    for i in range(n):#计算底事件x[i]的结构重要度
        c1=0#记录结果为1的个数
        b = 0
        # x[]除去x[0]，其他底事件x[1~n]中有且仅有k个为1
        for k in range(n):#k=0~n-1
            c1=c1+assign(k,b, x, n,i)
        c2=0
        b = 1
        # x[]除去x[0]，其他底事件x[1~n]中有且仅有k个为1
        for k in range(n):  # k=0~n-1
            c2 = c2 + assign(k, b, x, n,i)
        print('事件x[{}]的结构重要度{}'.format(i,(c2-c1)/pow(2,n-1)))

def demo():
    #修改a,b的取值，选择要实现的功能
    a=4
    b=1
    print("******************************************")
    print('a=1时：直接分布算法（故障树中没有重复事件）计算顶事件的概率')
    print('a=2时：基于最小割集（故障树中有重复事件）计算顶事件的概率')
    print('a=3时：列出故障树的最小割集')
    print('a=4时：根据最小割集简化故障树，求各底事件的结构重要度')
    print('b=1时：顶事件 与门连接 后面的事件')
    print('b=2时：顶事件 或门连接 后面的事件')
    print("******************************************")

    # 直接分布算法（故障树中没有重复事件）计算顶事件的概率
    if a==1: #从下往上逐步计算顶事件概率
        p1=andStructure(2,{'x1':0.01,'x9':0.01})
        print('与门顶事件的概率为',p1)
        p2=andStructure(2,{'x2':0.01,'x3':0.01})
        print('与门顶事件的概率为',p2)
        p3=andStructure(5,{'x4':0.01,'x5':0.01,'x6':0.01,'x7':0.01,'x8':0.01})
        print('与门顶事件的概率为',p3)
        p4=orStructure(3,{'E1':p1,'E2':p2,'E3':p3})
        print('或门顶事件的概率为',p4)

    #基于最小割集（故障树中有重复事件）计算顶事件的概率
    if a==2:
        T_minmalCutSet()
    if a==3:#求最小割集
        if b==1:#顶事件 与门连接 后面的事件
            mc=[['M1','x1','M2']]#初始化，顶事件 与门连接 后面的事件
            mc=minmalCutSet('M1','or',['x2','M3'],mc)
            print(len(mc), mc)
            mc = minmalCutSet('M2', 'or', ['x3', 'M4'], mc)
            print(len(mc), mc)
            mc = minmalCutSet('M3', 'or', ['x4','x5','x6'], mc)
            print(len(mc), mc)
            mc = minmalCutSet('M4', 'or', ['x7', 'x8', 'x9'], mc)
            print(len(mc),mc)
        if b==2:#顶事件 或门连接 后面的事件
            mc = [['M1'], ['x1'], ['M2']]# 初始化
            mc = minmalCutSet('M1', 'and', ['x2', 'x3'], mc)
            mc = minmalCutSet('M2', 'or', ['x4', 'x5','x6'], mc)
            print(len(mc), mc)

    if a==4:
        print('使用该函数前需要修改：')
        print('1.assign函数中k==1,2,3,...的操作')
        print('2.result(x,i)函数中的表达式也需要根据最小割集修改')
        structural_importance(5)#故障树的底事件个数为5，若不为5，
demo()