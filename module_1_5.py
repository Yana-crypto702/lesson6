immutable_tuple= (1, 2, 'a', 'b')
print(immutable_tuple)
#immutable_tuple[0]=200
#print(immutable_tuple)  #мы не сможем вывести на экран такое действие, т.к. кортеж-является неизменным объектом
Mutablelist=([1, 2, 'a', 'b',], 'Modified')
print(Mutablelist)
Mutablelist[0][0]=46
print(Mutablelist)