my_dict={"Дмитрий":1981, "Ольга":1985, "Валерия":2012}
print(my_dict)
print(my_dict["Дмитрий"])
print(my_dict.get("Василий","Такого ключа нет"))
my_dict.update({"Наталья":1973,"Василий":1972})
print(my_dict)
a=my_dict.pop("Василий")
print(a)
print(my_dict)
my_set=[1,10,"Дмитрий",10,11,1,"Ольга",11]
print(set(my_set))
my_set.extend([2,3])
my_set.remove("Ольга")
print(set(my_set))