#Week 1
#---------------
Notebook: LabNotebooks\23Jun2022\DeepLearningLab1_V1.ipynb

Completed the following
1. Install numpy and pandas
2. Do Matrix operation of addition, subtraction and multiplication of 3x3 using numpy
3. Use dot product in numpy for different dimensions of matrix of your choice
4. Implement an example of tensor. What is the difference between tensor and matrix

##Results:
##----------

Some of the results are:


##Installation:
##----------
!pip install numpy
!pip install pandas

##Creation:
##----------

a = np.array([[1, 2, 3],[3,4, 5],[6,7,8]])
b = np.array ([[4,5,8],[9,6,2],[3,2,6]])
c = np.array([[4,9],[3,6],[2,5]])
print(a)
print(b)
print(c)

[[1 2 3]
 [3 4 5]
 [6 7 8]]
[[4 5 8]
 [9 6 2]
 [3 2 6]]
[[4 9]
 [3 6]
 [2 5]]


# creating a array of ones
d = np.ones((3,5), dtype=np.int64)
d

array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=int64)


add = np.add(a,b)
print(a)
print (b)
print(add)

[[1 2 3]
 [3 4 5]
 [6 7 8]]
[[4 5 8]
 [9 6 2]
 [3 2 6]]
[[ 5  7 11]
 [12 10  7]
 [ 9  9 14]]

 sub = np.subtract(a,b)
print(a)
print (b)
print(sub)
[[1 2 3]
 [3 4 5]
 [6 7 8]]
[[4 5 8]
 [9 6 2]
 [3 2 6]]
[[-3 -3 -5]
 [-6 -2  3]
 [ 3  5  2]]

 mult = np.multiply(a,b)
print(a)
print (b)
print(mult)
[[1 2 3]
 [3 4 5]
 [6 7 8]]
[[4 5 8]
 [9 6 2]
 [3 2 6]]
[[ 4 10 24]
 [27 24 10]
 [18 14 48]]

 d2 = np.dot(a,c)
print(a)
print (c)
print(d2)
[[1 2 3]
 [3 4 5]
 [6 7 8]]
[[4 9]
 [3 6]
 [2 5]]
[[ 16  36]
 [ 34  76]
 [ 61 136]]

 ##Implement an example of tensor. What is the difference between tensor and matrix

 ### tensors are a generalization of matrices and are represented using n-dimensional arrays.
#Tensor Addition
T1=a+b
print(a)
print(b)
print(T1)
[[1 2 3]
 [3 4 5]
 [6 7 8]]
[[4 5 8]
 [9 6 2]
 [3 2 6]]
[[ 5  7 11]
 [12 10  7]
 [ 9  9 14]]

 # Tensor Hadamard Product
T3=a*b
print(a)
print(b)
print(T3)
[[1 2 3]
 [3 4 5]
 [6 7 8]]
[[4 5 8]
 [9 6 2]
 [3 2 6]]
[[ 4 10 24]
 [27 24 10]
 [18 14 48]]