immutable_var=5,10,"Дмитрий",False
print(immutable_var)
mutable_list=[5,10,"Дмитрий",False]
print(mutable_list)
mutable_list[2]="Ольга"
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend("Дмитрий")
print(mutable_list)
mutable_list.extend(["нравиться мне это дело"])
print(mutable_list)
mutable_list.remove("Д")
print(mutable_list)