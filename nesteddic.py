car = {
"brand" : "Ford",
"model" : "Mustang",
"year" : 1964
}
for x in car:
  print(x)
for x in car.values():
  print(x)
for x in car.keys():
  print(x)
for x, y in car.items():
  print(x,y)

myfamily = {
"child1" :{
"name" : "Email",
"year" : 2004
},
"child2" :{
"name" : "Tobias",
"year" : 2007
},
"child3" :{
"name" : "Linus",
"year" : 2011
}
}

child1 = {
"name" : "Email",
"year" : 2004
}
child2= {
"name" : "Tobias",
"year" : 2007
}
child3 = {
"name" : "Linus",
"year" : 2011
}
myfamily = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}
print(myfamily)
