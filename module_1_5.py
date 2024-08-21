immutable_var = (2024, 'Urban', True, 36.6, [0, 1])
print('Immutable var:',(immutable_var))
mutable_list = [2024, 'Urban', True, 36.6, [0, 1]]
mutable_list[1] = 'University'
print('Mutable list:', mutable_list)
immutable_var[1] = 'University' # элементы кортежа нельзя изменять после добавления в кортеж, т.к. сам кортеж является неизменяемым типом данных.
print(immutable_var)

