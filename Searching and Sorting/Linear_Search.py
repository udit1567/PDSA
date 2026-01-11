def naivesearch(L,v):
  for i in range(len(L)):
    if v == L[i]:
      return i
  return(False)



L = [5,7,9,2,4,10]
v=9

print(naivesearch(L,v))