#Sorting Algoritms
#Buble Sort
def BubbleSort(arr:list):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

        print(arr)
#Selection Sort
def SelectionSort(arr:list):
    for i in range(len(arr)):
        min_ind=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[j],arr[min_ind]=arr[min_ind],arr[i]
    print(arr)

#Insertion Sort
def InsertionSort(arr:list):
    for i in range(1,len(arr)):
        x=arr[i]
        j=i-1
        while j>=0 and x<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=x
    print(arr)
#Quick Sort
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
ls=[4,2,3,4,6,3,55,7,3,6,8,3,5,7,4,444]
#BubbleSort(ls)
#SelectionSort(ls)
#InsertionSort(ls)
QuickSort(ls,0,len(ls)-1)
print(ls)

