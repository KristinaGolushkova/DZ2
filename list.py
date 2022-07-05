# удалить пустые строки
a = ["1", "", "3", "4", ""]

a = list(filter(None, a))

print(a)

# квадраты чисел

b = [1, 2, 6, 10, 35]
b = [i ** 2 for i in b]
print(b)

# удалить все вхождения числа 20
c = [2, 20, 33, 20, 66, 20]
d = 20

for i in c:
    if(i == d):
        c.remove(d)
print(c)

# список в обратном порядке
c = [2, 20, 33, 20, 66, 20]
c.reverse()
print(c)

# поменять местами самый большой и самый маленький элементы списка.
x = a.index(max(a))
o = a.index(min(a))
a[x], a[o] = a[o], a[x]
print(a)

# oпределить, есть ли в списке повторяющиеся элементы(честно- подсмотрено)

w = [2, 20, 33, 20]
u = set([i for i in w if w.count(i) > 1])
print(*(u if len(u) > 0 else ["нет"]))


# найти сумму и произведение элементов списка
import math

num = [1, 5, 3, 6, 5]

print(math.prod(num))
print(sum(num))








