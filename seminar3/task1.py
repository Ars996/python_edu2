# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def d_list(array: list[int]) -> list[int]:
    res=set()
    for el in array:
        counter= array.count(el)
        if counter > 1:
            res.add(el)
    return list(res)
print(d_list([1,2,3,4,2,2,4]))