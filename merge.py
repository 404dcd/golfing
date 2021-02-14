def q(a):
 o=[]
 while len(a)>1:
  o.append([])
  while all(a[:2]):o[-1]+=[a[a[0][0]>=a[1][0]].pop(0)]
  o[-1]+=a.pop(0)+a.pop(0)
 return q(o+a)if len(o+a)-1 else o+a
m=lambda i:q([[x]for x in i])[0]