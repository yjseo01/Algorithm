
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    tmp = input()
    matrix.append([int(c) for c in tmp])

rec1, rec2, rec3 = 0, 0, 0
mul_max = 0

if n >= 3:
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for row in range(m):
                for col in range(i + 1):
                    rec1 += matrix[col][row]

                for col in range(i + 1, j + 1):
                    rec2 += matrix[col][row]

                for col in range(j + 1, n):
                    rec3 += matrix[col][row]

            mul_max = max(mul_max, rec1 * rec2 * rec3)
            rec1, rec2, rec3 = 0, 0, 0

if m >= 3:
    for i in range(m - 2):
        for j in range(i + 1, m - 1):
            for col in range(n):
                for row in range(i + 1):
                    rec1 += matrix[col][row]

                for row in range(i + 1, j + 1):
                    rec2 += matrix[col][row]

                for row in range(j + 1, m):
                    rec3 += matrix[col][row]

            mul_max = max(mul_max, rec1 * rec2 * rec3)
            rec1, rec2, rec3 = 0, 0, 0

if n >= 2 and m >= 2:
    for i in range(m - 1):
        for j in range(n - 1):

            #
            for col in range(j + 1):
                for row in range(m):
                    rec1 += matrix[col][row]

            for col in range(j + 1, n):
                for row in range(i + 1):
                    rec2 += matrix[col][row]

                for row in range(i + 1, m):
                    rec3 += matrix[col][row]

            mul_max = max(mul_max, rec1 * rec2 * rec3)
            rec1, rec2, rec3 = 0, 0, 0

            #
            for col in range(j + 1):
                for row in range(i + 1):
                    rec1 += matrix[col][row]

                for row in range(i + 1, m):
                    rec2 += matrix[col][row]


            for col in range(j + 1, n):
                for row in range(m):
                    rec3 += matrix[col][row]

            mul_max = max(mul_max, rec1 * rec2 * rec3)
            rec1, rec2, rec3 = 0, 0, 0

            #
            for row in range(i + 1):
                for col in range(n):
                    rec1 += matrix[col][row]

            for row in range(i + 1, m):
                for col in range(j + 1):
                    rec2 += matrix[col][row]

                for col in range(j + 1, n):
                    rec3 += matrix[col][row]

            mul_max = max(mul_max, rec1 * rec2 * rec3)
            rec1, rec2, rec3 = 0, 0, 0

            #
            for row in range(i + 1):
                for col in range(j + 1):
                    rec1 += matrix[col][row]
                for col in range(j + 1, n):
                    rec2 += matrix[col][row]

            for row in range(i + 1, m):
                for col in range(n):
                    rec3 += matrix[col][row]

            mul_max = max(mul_max, rec1 * rec2 * rec3)
            rec1, rec2, rec3 = 0, 0, 0

print(mul_max)
