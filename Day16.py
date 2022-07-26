def add_last1(m1, n1):
    m1 += n1

t1 = (1, 3)
add_last1(t1, (5, 7))
print(t1)



def add_last2(m, n):
    m += n
    return m

t2 = (1, 3)
t2 = add_last2(t2, (5, 7))
print(t2)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[0], a[-1])

a = []
a.append(1)
a.append(10)
a.append(25)
a.append(7)
a.append(99)
a.append(8)
a.append(57)
a.append(33)
a.append(96)
a.append(2)
a.append(48)
print(a)
a.sort()
print(a)

# 여러분 문제입니다. 다음에 나와있는 리스트에서 가장 큰 값과
# 가장 작은 값을 출력하는 함수를 정의하세요 !
# 단, 원본의 순서를 변경시키지 않아야 합니다.
l = [3, 1, 5, 4, 7, 6]
def min_max(a):
    a.sort()
    print(a[0], a[-1], sep = ', ')

print(l)
min_max(l)
print(l)

# 여러분 문제입니다. 다음에 나와있는 리스트에서 가장 큰 값과
# 가장 작은 값, 큰 값을 출력하는 함수를 정의하세요 !
# 단, 원본의 순서를 변경시키지 않아야 합니다.

b = [3, 1, 5, 4, 7, 6]
def minMax(a):
    a = list(a)
    a.sort()
    print(a[0], a[-1], sep = ', ')

minMax(b)
print(b)
c = (3, 1, 5, 4, 7, 6)
minMax(c)
print(c)
