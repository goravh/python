var = {}
print(type(var))
    
##var = {"dhoni",33,"india"}
##print(type(var))

##var = {"name":"dhoni","Age":33,"country":"india"}
##print(var)
##print(type(var))
#python dictionary is called key value pair
#no index based manipulation
#keys wwe store should be unique

var = {"name":"dhoni","Age":33,"country":"india"}
print(var[0])

##var = {"name":"dhoni","Age":33,"country":"india"}
##print(var["name"])

##var = {"name":"dhoni","Age":33,"name":"india"}
##print(var["name"])

##var = {"name":"dhoni","Age":33,"country":"india"}
##var["name"] = "kohli"
##print(var)

##var = {"name":"dhoni","Age":33,"country":"india"}
##output = var["team"]
##print(output)

##var = {"name":"dhoni","Age":33,"country":"india"}
##output = var.get("team","sorry")
##print(output)
##print("welcome to india")

##var = {"name":"dhoni"}
##var1 = {"Age":33}
##output = var +var1
##print(output)

##var = {"name":"dhoni"}
##var1 = {"Age":33}
##var.update(var1)
##print(var)

##var = {"name":"dhoni"}
##var1 = {"Age":33}
##output = {**var, **var1}
##print(output)

##var = {"name":"dhoni",3:"rohit",4.5:"ashwin",("a","b"):"welcome",["a"]:"pant"}
##print(var)


##var = {"name":"dhoni",3:"rohit",4.5:"ashwin",("a","b"):"welcome"}

##var = {"name":"dhoni",3:"rohit",4.5:"ashwin",("a","b"):"welcome"}
##for x in var():
##    print(x)

##
##var = {"name":"dhoni",3:"rohit",4.5:"ashwin",("a","b"):"welcome"}
##for x in var.items():
##    print(x)
##
##var = {"name":"dhoni",3:"rohit",4.5:"ashwin",("a","b"):"welcome"}
##for x in var.values():
##    print(x)

##var = {"name":"dhoni",3:"rohit",4.5:"ashwin",("a","b"):"welcome"}
##for x in var.keys():
##    print(x)        

##for x in range(10):
##    print(x)          

##for x in range(1,10,2):
##    print(x)      


##for x in range(10,1,-1):
##    print(x)
##
##
##
##my_list = []
##for x in range(10):
##    if x%2 ==0:
##        my_list.append(x)
##        
##print(my_list)

##my_list = [x for x in range(10) if x%2 ==0]
##print(my_list)

##my_dict = {}
##for x in range(4):
##    my_dict[x] = x*x
##print(my_dict)

my_dict = {x:x*x for x in range(4)}
print(my_dict)



























##my_list = []
##for x in range(10)
##    if x%2 ==0:
##        my list.append(x)
#print(my_list)
##
##my_list = [x for x in range(10) if x%2 ==0]
##print(my_list)


#output = {0:0.1:1,2:4,3:9}

##my_dict = {}
##for x in range(4):
##    my_dict[x] = x*x
##print(my_dict)
##
##my_dict = {x:x*x for x in range(4)}
##print(my_dict)







