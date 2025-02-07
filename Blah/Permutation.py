q=2
result=[]
def permut():
    for iteration in range(q):
        ans = True

        n, k = map(int, input().split())

        A = input().split()

        for i in range(n):
            A[i] = int(A[i])

        B = input().split()

        for i in range(n):
            B[i] = int(B[i])

        print(A)
        print(B)

        for i in range(n):
            for j in range(n - i - 1):
                if A[j] > A[j + 1]:
                    temp = A[j]
                    A[j] = A[j + 1]
                    A[j + 1] = temp

        A1 = A

        for i in range(n):
            for j in range(n - i - 1):
                if B[j] < B[j + 1]:
                    temp = B[j]
                    B[j] = B[j + 1]
                    B[j + 1] = temp

        B1 = B

        print(A1)
        print(B1)

        for i in range(n):
            if A1[i] + B1[i] >= k:
                continue
            else:
                ans = False
                break

        if ans == True:
            result.append("YES")
        else:
            result.append("NO")

permut()

for i in result:
    print(i)