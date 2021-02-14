L=100;i=p=2
while i<L**.5:[p:=p|1<<x for x in range(i*i,L,i)];i+=1
[print(n)for n in range(2,L)if~p&1<<n]