a=[5,10,15,20,25]
def PointlessFunction():
	b=a[0],a[-1]
	print(b)
#PointlessFunction()
d=0
c=[1,1,8,13,21,34,2,3,5,55,89]
def PointlessFunction2(bla):
	e=[]
	for elms in c:
		if elms < bla:
			e.append(elms)
	print(e)
PointlessFunction2(3)

