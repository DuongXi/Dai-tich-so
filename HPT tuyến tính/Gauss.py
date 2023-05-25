import numpy as np

def gaussThuan(matrix):
    #Trả về ma trận đã được biến đổi qua quá trình thuận cảu thuật toán Gauss
    print("Các bước biến đổi: ")
    for j in range(0,len(matrix)-1):
        for i in range(j+1,len(matrix)):
            if int(matrix[j,j])==0:
                swap(matrix,j)
            matrix[i] = matrix[i] - (matrix[i,j]/matrix[j,j])*matrix[j]
        print(matrix)
        print()
            
def gaussNghich(matrix):
    #Tìm nghiệm hệ phương trình qua quá trình nghịch của thuật toán Gauss
    size = len(matrix)
    for i in range(0,size):
        k=len(kq)-1
        sum = 0
        for j in range(size-i,size):
            sum += matrix[size-1-i,j]*kq[k]
            k-=1 
        n = ((matrix[size-1-i,size])-sum)/matrix[size-1-i,size-1-i]
        kq.append(n)
        
def swap(matrix,j):
    #thay hàng có phần tử vị trí (i,i) bằng 0 bằng một sau nó có vị trí (i,i+k) khác 0
    for i in range(j+1,len(matrix)):
        if matrix[i,j] != 0:
            tmp = matrix[i].copy()
            matrix[i] = matrix[j]
            matrix[j] = tmp
        return

#main-----------------------------------------------------------------------
file = open('data.txt', 'r')
matrix = np.loadtxt("data.txt")
file.close()
kq = []
gaussThuan(matrix)
gaussNghich(matrix)
kq.reverse()
print("Nghiẹm của hệ phương trình là: ")
print(kq)