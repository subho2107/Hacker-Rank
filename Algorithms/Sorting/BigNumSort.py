arr = ["1","3","2","8","4"]
arr.sort(key = lambda x:(len(x),x))
print(arr)