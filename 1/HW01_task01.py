'''Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника 
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.'''


a, b, c = int(input()), int(input()), int(input())

if a + b < c or a + c < b or c + b < a:
    print('Треугольника с заданой величиной сторон не существует')
elif a == b == c:
    print('Вы построите равносторонний треугольник')
elif a == b or b == c or a == c:
    print('Вы построите равнобедренный треугольник')
else:
    print('Вы можете построить треугольник с заданными сторонами')