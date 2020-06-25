def getUniqueElements(*elements):
  arr = []
  i = 0
  while(i < len(elements)):
    if elements[i] not in arr:
      arr.append(elements[i])
    i += 1
  return arr


print(getUniqueElements(13,15,13,1,4,6))
