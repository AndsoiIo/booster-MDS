# https://stepik.org/lesson/24462/step/8?unit=6768


# Реализуйте структуру данных, представляющую собой расширенную структуру стек.
# Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека,
# и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.

# Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1),
# затем снимается следующий верхний элемент (top2), и затем как результат операции сложения на вершину стека кладется элемент, равный top1 + top2.

# Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и целочисленного деления (top1 // top2).

# Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.


class ExtendedStack(list):
    def sum(self):
        self.append(self.pop(-1) + self.pop(-1))

    def sub(self):
        self.append(self.pop(-1) - self.pop(-1))

    def mul(self):
        self.append(self.pop(-1) * self.pop(-1))

    def div(self):
        self.append(self.pop(-1) // self.pop(-1))
