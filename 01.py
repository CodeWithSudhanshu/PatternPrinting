# def pattern1(n):
#     for i in range(n):
#         for j in range(n):
#             print("* " , end = "")
#         print()
# pattern1(5)
# def pattern2(n):
#     for i in range(0,n):
#         for j in range(i+1):
#             print("* " , end = "")
#         print()
# pattern2(5)
# def pattern3(n):
#     for i in range(1 , n+1):
#         for j in range(1 , i+1):
#             print(j , end = "")
#         print()
# pattern3(5)
# def pattern4(n):
#     for i in range(1 , n+1):
#         for j in range(1 , i+1):
#             print(i , end = " ")
#         print()
# pattern4(5)
# def pattern5(n):
#     for i in range(n):
#         for j in range(1,n-i+1):
#             print("* " , end = "")
#         print()
# pattern5(5)
# def pattern6(n):
#     for i in range(1,n+1):
#         for j in range(1,n-i+2):
#             print(j , end = " ")
#         print()
# pattern6(5)
# def pattern7(n):
#     for i in range(0,n):
#         for j in range(n-i-1): #spaces
#             print(" " , end = " ")
#         for j in range(2*i+1): #stars
#             print("*" , end = " ")
#         for j in range(n-i-1): #spaces
#             print(" " , end = " ")
#         print()
# pattern7(9)
def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" " , end = " ")
        for j in range(2*n-(2*i+1)):
            print("*" , end = " ")
        for j in range(i):
            print(" " ,end=" ")
        print()
pattern8(6)
