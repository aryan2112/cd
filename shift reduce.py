grammer={}
var= [k for k in input("Enter The Variable in
Grammer:").split(" ")]
ter =[k for k in input("Enter The Terminal in
Grammer:").split(" ")]
for v in var:
 grammer[v]=[k for k in input("Enter the
production of "+v+" Separated by space:").split("
")]
inpbuff=input("Enter The String to pass:")
inpbuff=inpbuff
inp2=inpbuff
stack=''
print("==============================================
=======")
print("STACK\t\tINPUT\t\tACTION")
print("==============================================
=======")
reduced=0
for i in inpbuff:
 reduced=1
 while(reduced==1):
 for v in var:
 for prod in grammer[v]:
 if prod in stack:
 if prod[-1]==stack[-1]:
 stack=stack.replace(prod,v)

print(stack,"\t\t",inp2,"\t\tReduced!!")
 reduced=1
 else:
 reduced=0
 stack+=i
 inp2=inp2[1:len(inp2)]
 print(stack,"\t\t",inp2,"\t\tShifted!!")
