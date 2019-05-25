# Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.

# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

# Вашей программе на вход подаются следующие запросы:

#     create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
#     add <namespace> <var> – добавить в пространство <namespace> переменную <var>
#     get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует

# формально, результатом работы get <namespace> <var> является

#     <namespace>, если в пространстве <namespace> была объявлена переменная <var>
#     get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>, если переменная не была объявлена
#     None, если не существует <parent>, т. е. <namespace>﻿ – это global

# Формат входных данных

# В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
# В каждой из следующих n строк дано по одному запросу.
# Запросы выполняются в порядке, в котором они даны во входных данных.
# Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных латинских букв.
# Формат выходных данных

# Для каждого запроса get выведите в отдельной строке его результат.


def scope_sim(n):
    scope = {'global': [None]}

    def create(namespace, parent):
        scope[parent].append(namespace)
        scope[namespace] = [parent]

    def add(namespace, x):
        scope.setdefault(namespace, list()).append(x)

    def get(namespace, x):
        if x in scope.get(namespace, [None]):
            return print(namespace)
        try:
            return get(scope[namespace][0], x)
        except KeyError:
            return print(None)

    commands = {'add': add, 'create': create, 'get': get}
    for _ in range(n):
        command, *arg = input().split()
        commands[command](*arg)


n = int(input())
scope_sim(n)
