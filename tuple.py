# Tuple
my_tuple = (1, 5, 8)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

# Tuple neumí měnit hodnoty narozdíl od listu. Lze jen definovat na začátku.
# Tuple lze změnit na list, int, str atp.

tuple_to_list = list(my_tuple)
print(tuple_to_list)
tuple_to_list[0] = 12
print(tuple_to_list)