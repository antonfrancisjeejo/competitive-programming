def permutation(name):
  permutation1(name,'')
  
def permutation1(name,prefix):
  if(len(name)==0):
    print(prefix)
  else:
    for i in range(len(name)):
      rem = name[0:i] + name[i+1:]
      permutation1(rem,prefix+name[i])
      
permutation('123')
