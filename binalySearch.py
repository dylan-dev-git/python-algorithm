data = [1,2,3,4,5,6,7,8,9,10]
count = len(data)
mid = 0
low = 0
high = len(data) -1

key = 4

while(low <= high):
  mid = int((low + high)/2)
  if data[mid] == key:
    print("located " + str(mid))
    break

  if data[mid] < key:
    low = mid+1
  else:
    high = mid-1