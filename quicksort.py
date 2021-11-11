def quickSort(arr,left,right):
  pivot = arr[int((left + right)/2)]
  i = left
  j = right
  if (left<right):
    while(1):
      while (arr[i] < pivot): i += 1
      while (arr[j] > pivot): j -= 1
      if (i>=j): break
      t = arr[i]
      arr[i] = arr[j]
      arr[j] = t
    quickSort(arr,left,i-1)
    quickSort(arr,j+1,right)
  

arr = [2,10,4,7,3,1,9,6,5,8]

print(arr)

quickSort(arr,0, len(arr)-1)
print(arr)
