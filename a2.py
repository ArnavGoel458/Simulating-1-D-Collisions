class MinHeap:
    
    def __init__(self, size):
        self.heap=[]
        self.indextrack=[i for i in range(0,size)]
    def heapdown(self, i):
        minimum=i
        li=2*i+1
        ri=2*i+2
        if li<len(self.heap):
            if self.heap[2*i+1][0]<self.heap[minimum][0]:
                minimum=li
            elif self.heap[2*i+1][0]==self.heap[minimum][0] and self.heap[2*i+1][3]<self.heap[minimum][3]:
                minimum=li
        if ri<len(self.heap):
            if self.heap[2*i+2][0]<self.heap[minimum][0]:
                minimum=ri
            elif self.heap[2*i+2][0]==self.heap[minimum][0] and self.heap[2*i+2][3]<self.heap[minimum][3]:
                minimum=ri
        if minimum!=i:
            self.indextrack[self.heap[minimum][3]]=i
            self.indextrack[self.heap[i][3]]=minimum
            self.heap[minimum], self.heap[i]=self.heap[i], self.heap[minimum]
            self.heapdown(minimum)
    def buildheap(self):
        for i in range(len(self.heap)//2,-1,-1):
            self.heapdown(i)
    def heapup(self,i):
        if i>0:
            if self.heap[(i-1)//2][0]==self.heap[i][0] and self.heap[(i-1)//2][3]>self.heap[i][3]:
                self.indextrack[self.heap[(i-1)//2][3]]=i
                self.indextrack[self.heap[i][3]]=(i-1)//2
                self.heap[(i-1)//2], self.heap[i]= self.heap[i], self.heap[(i-1)//2]
            elif self.heap[(i-1)//2][0]>self.heap[i][0]:
                self.indextrack[self.heap[(i-1)//2][3]]=i
                self.indextrack[self.heap[i][3]]=(i-1)//2
                self.heap[(i-1)//2], self.heap[i]= self.heap[i], self.heap[(i-1)//2]
            self.heapup((i-1)//2)
    
    
def listCollisions(M,x,v,m,T):
    usheap=MinHeap(len(M))
    for i in range(len(M)):
        if i==len(M)-1:
            usheap.heap.append([2*T,v[i],x[i], i])
        elif  v[i]>v[i+1]:
            t=(x[i+1]-x[i])/(v[i]-v[i+1])
            usheap.heap.append([t, v[i], x[i], i])
        else:
            usheap.heap.append([2*T,v[i],x[i], i])
    usheap.buildheap()
    count=0
    time=0
    finallist=[]
    timelist=[0]*len(M)
    timecheck=0
    while count<m and timecheck<=T:
        timecheck=usheap.heap[0][0]
        if timecheck<=T:
            coltime=usheap.heap[0][0]
            colposition=usheap.heap[0][2]+ usheap.heap[0][1]*(coltime-timelist[usheap.heap[0][3]])
            timelist[usheap.heap[0][3]]=coltime
            timelist[usheap.heap[0][3]+1]=coltime
            main_index=usheap. heap[0][3]
            finallist.append((round(coltime,4), usheap.heap[0][3],round(colposition,4))) 
            count+=1
            time=coltime
            ind_i1=usheap.indextrack[usheap.heap[0][3]+1]
            m1=M[usheap.heap[0][3]]
            m2=M[usheap.heap[ind_i1][3]]
            v1=usheap.heap[0][1]
            v2=usheap.heap[ind_i1][1]
            usheap.heap[0][1]=((m1-m2)/(m1+m2))*v1 + ((2*m2)/(m1+m2))*v2
            usheap.heap[ind_i1][1]=((2*m1)/(m1+m2))*v1 - ((m1-m2)/(m1+m2))*v2
            usheap.heap[0][0]=2*T
            usheap.heap[0][2]=colposition
            usheap.heap[ind_i1][2]=colposition
            usheap.heapdown(0)
            if main_index-1>=0 and main_index+2<=len(M)-1:
                ind_i1_=usheap.indextrack[main_index-1]
                if usheap.heap[ind_i1_][1]> usheap.heap[usheap.indextrack[main_index]][1]:
                    usheap.heap[ind_i1_][0]=(usheap.heap[usheap.indextrack[main_index]][2]-(usheap.heap[ind_i1_][2]+usheap.heap[ind_i1_][1]*(time-timelist[usheap.heap[ind_i1_][3]])))/(usheap.heap[ind_i1_][1]-usheap.heap[usheap.indextrack[main_index]][1])+time
                else:
                    usheap.heap[ind_i1_][0]=2*T
                usheap.heapup(usheap.indextrack[main_index-1])
                ind_i1=usheap.indextrack[main_index+1]
                ind_i2=usheap.indextrack[main_index+2]
                if usheap.heap[ind_i1][1]> usheap.heap[ind_i2][1]:
                    usheap.heap[ind_i1][0]=(usheap.heap[ind_i2][2]+usheap.heap[ind_i2][1]*(time-timelist[usheap.heap[ind_i2][3]])-usheap.heap[ind_i1][2])/(usheap.heap[ind_i1][1]-usheap.heap[ind_i2][1])+ time
                else:
                    usheap.heap[ind_i1][0]=2*T
                usheap.heapup(usheap.indextrack[main_index+1])
            elif main_index-1>=0 and main_index+2>len(M)-1:
                ind_i1_=usheap.indextrack[main_index-1]
                if usheap.heap[ind_i1_][1]> usheap.heap[usheap.indextrack[main_index]][1]:
                    usheap.heap[ind_i1_][0]=(usheap.heap[usheap.indextrack[main_index]][2]-(usheap.heap[ind_i1_][2]+usheap.heap[ind_i1_][1]*(time-timelist[usheap.heap[ind_i1_][3]])))/(usheap.heap[ind_i1_][1]-usheap.heap[usheap.indextrack[main_index]][1])+time
                else:
                    usheap.heap[ind_i1_][0]=2*T
                usheap.heapup(usheap.indextrack[main_index-1])
            elif main_index-1<0 and main_index+2<=len(M)-1:
                ind_i1=usheap.indextrack[main_index+1]
                ind_i2=usheap.indextrack[main_index+2]
                if usheap.heap[ind_i1][1]> usheap.heap[ind_i2][1]:  
                    usheap.heap[ind_i1][0]=(usheap.heap[ind_i2][2]+usheap.heap[ind_i2][1]*(time-timelist[usheap.heap[ind_i2][3]])-usheap.heap[ind_i1][2])/(usheap.heap[ind_i1][1]-usheap.heap[ind_i2][1])+time
                else:
                    usheap.heap[ind_i1][0]=2*T
                usheap.heapup(usheap.indextrack[main_index+1])
    return finallist


        

print(listCollisions([10000.0, 1.0, 100.0], [0.0, 1.0, 2.0], [0.0, 0.0, -1.0], 6, 1.505))





