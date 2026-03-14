#metode 1 ------------

i = 0

a = [8, 5, 2, 6, 12]

for _ in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            b = a[i+1]
            a[i+1] = a[i]
            a[i] = b

print(a)

#metode 2 --------------

c = [1, 2, 6, 3, 8, 10, 45]

def sortering(liste):
    if len(c) % 2 == 0:
            
                 

#ChatGPT sin versjon av QuickSort ------

def quick_sort(liste):
    if len(liste) <= 1:
        return liste  # base case – ferdig hvis listen er tom eller har 1 element

    pivot = liste[0]  # velg første element som pivot
    mindre = [x for x in liste[1:] if x <= pivot]
    større = [x for x in liste[1:] if x > pivot]

    return quick_sort(mindre) + [pivot] + quick_sort(større)

# Test:
data = [8, 3, 1, 7, 0, 10, 2]
print(quick_sort(data))