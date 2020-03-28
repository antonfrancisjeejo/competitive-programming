class Stack:
  def __init__(self):
    self.items=[]
  def push(self,item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def isEmpty(self):
    return self.items==[]
  
def isSame(p1,p2):
  if p1=='(' and p2==')':
    return True
  elif p1=='[' and p2==']':
    return True
  elif p1=='{' and p2=='}':
    return True
  else:
    return False

def isBalanced(string):
  index=0
  isBal=True
  s=Stack()
  while index<len(string) and isBal:
    check=string[index]
    if check in '{[(':
      s.push(check)
    else:
      if s.isEmpty():
        isBal=False
      else:
        top=s.pop()
        if not isSame(top,check):
          isBal=False
    index+=1
  if s.isEmpty() and isBal:
    return True
  else:
    return False

print(isBalanced('[{}()]'))
