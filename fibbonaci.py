def fibbonaci_n(fibIndex):
  if fibIndex==1 or fibIndex==2: 
    return 1
  return fibbonaci_n(fibIndex-1)+fibbonaci_n(fibIndex-2)

print(fibbonaci_n(10))
