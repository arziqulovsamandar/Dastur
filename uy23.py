'''def InsertionSort(arr:list):
    for i in range(1,len(arr)):
        x=arr[i]
        j=i-1
        while j>=0 and x<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=x
    print(arr)
    #l3.extend(arr)
def partition(arr:list,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def QuickSort(arr:list,low,high):
    if low<high:
        x=partition(arr,low,high)
        QuickSort(arr,low,x-1)
        QuickSort(arr,x+1,high)
ls=[4,2,3,4,6,3,55,7,3,'bunyod',6,'A','Hayr','Dunyo',8,3,5,7,4,444] 
l3=[]
#ls=str(ls)
l=[]
l1=[]
for i in ls:
    i=str(i)
    if i.isdigit():
        l.append(i)
    elif i.isalpha():
        l1.append(i)
print(l,l1)
InsertionSort(l)
QuickSort(l1,0,len(l1)-1)
#print(l1)
l3.extend(l1)
#print(l3)'''
ls = [5, 1, 35, 21, 'salom', 5, 'A', 'Hayr', 12]

raqam1 = []
char = []
word = []

for i in ls:
    i = str(i)
    if i.isdigit():
        raqam1.append(i)
    elif i.isalpha() and len(i) == 1:
        char.append(i)
    else:
        word.append(i)

a = []
raqam = []

for i in raqam1:
    i = int(i)
    raqam.append(i)


def SelectionSort(arr: list):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    #print(arr)


SelectionSort(raqam)


def SelectionSortWord(arr: list):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    #print(arr)


SelectionSortWord(word)


def SelectionSortLetter(arr: list):
    for i in range(len(arr)):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_ind]:
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    #print(arr)


SelectionSortLetter(char)


a.extend(raqam)
a.extend(char)
a.extend(word)

print(a)