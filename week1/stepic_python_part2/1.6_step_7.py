# https://stepik.org/lesson/24462/step/7?unit=6768


# Формат входных данных

# В первой строке входных данных содержится целое число n - число классов.

# В следующих n строках содержится описание наследования классов. В i-й строке указано 
# от каких классов наследуется i-й класс. Обратите внимание, что класс может 
# ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
# что класс не наследуется явно от одного класса более одного раза.

# В следующей строке содержится число q - количество запросов.

# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

# Формат выходных данных

# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.


def isancestor(parent, child, tree):
    if child == parent:
        return True
    else:
        for inheritor in tree[child]:
            if isancestor(parent, inheritor, tree):
                return True

        return False


tree = {}
SEP = ':'

n = int(input())
for _ in range(n):
    data = input()

    if SEP in data:
        child, _, *parents = data.split()
    else:
        child, parents = data, list()
    tree[child] = parents

q = int(input())
for _ in range(q):
    parent, child = input().split()
    if isancestor(parent, child, tree):
        print('Yes')
    else:
        print('No')
