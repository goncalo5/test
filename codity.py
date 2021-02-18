import unittest


def solution1(N):
    binary = bin(N)[2:]
    # print("binary", binary)
    lengths = binary.split("1")
    max_length = 0
    if lengths[-1] != "":
        lengths.pop()
    for length in lengths:
        try:
            int(length)
        except:
            continue
        if len(length) > max_length:
            max_length = len(length)
    return max_length

def solution_lesson2_1(A, K):
    length = len(A)
    if length == 0:
        return []
    # print(A)
    K = K % length
    second_part = A[-K:]
    first_part = A[:-K]
    # print(first_part)
    # print(second_part)
    res = second_part + first_part
    # print(res)
    return res

def solution_lesson2_2(A):
    i = 1
    length = len(A)
    if length == 1:
        return A[0]
    A = sorted(A)
    for i in range(0, length, 2):
        try:
            if A[i] != A[i + 1]:
                return A[i]
        except:
            return A[i]

def solution_lesson3_1(X, Y, D):
    from math import ceil
    return ceil((Y - X) / D)

def solution_lesson3_2(A):
    if not A:
        return 1
    A = sorted(A)
    if A[0] == 2:
        return 1
    try:
        for i, n in enumerate(A):
            if n + 1 != A[i + 1]:
                return n + 1
    except:
        return A[-1] + 1

def solution_lesson3_3(A):
    _min = 9**999
    length = len(A)
    for p in range(1, length):
        # print(p)
        # print(A[:p], A[p:])
        first = sum(A[:p])
        second = sum(A[p:])
        # print(first, second)
        diff = abs(first - second)
        if diff < _min:
            _min = diff
    return _min

def solution_lesson4_1(X, A):
    zeros = [0] * X
    n_of_zeros = X
    for i, n in enumerate(A):
        # print(i, n)
        if zeros[n - 1] == 0:
            zeros[n - 1] = n
            n_of_zeros -= 1
            if n_of_zeros == 0:
                return i
        # if 0 not in zeros:
        #     return i
    # print(zeros)
    return -1

def solution_lesson4_2(N, A):
    # length = len(A)
    sol = [0] * N
    cur_max = 0
    last_upd_max = 0

    for n in A:
        if n > N:
            # sol = [max(sol)] * N
            sol = [cur_max] * N
        else:
            sol[n - 1] += 1
            if cur_max < sol[n - 1]:
                cur_max = sol[n - 1]
        # print(i, n, sol)
    return sol
# def solution_lesson4_2(N, A):
#     B = [0] * N

#     cur_max = 0
#     last_upd_max = 0

#     for a in A:
#         print(a)
#         if a > N:
#             print("a > N", cur_max)
#             last_upd_max = cur_max
#         if a <= N:
#             print("B[a-1]", B[a-1])
#             if B[a-1] < last_upd_max:
#                 B[a-1] = last_upd_max
#                 B[a-1]+=1
#             if cur_max < B[a-1]:
#                 print("cur_max < B[a-1]")
#                 cur_max = B[a-1]

#             for i in range(0,len(B)):
#                 print("i", i, last_upd_max)
#                 if B[i] < last_upd_max:
#                     B[i] = last_upd_max
#         print(B)

#     return B


class TestFunctions(unittest.TestCase):

    def test_solution_lesson4_2(self):
        self.assertEqual(solution_lesson4_2(5, [3, 4, 4, 6, 1, 4, 4]), [3, 2, 2, 4, 2])
        self.assertEqual(solution_lesson4_2(5, [3]), [0, 0, 1, 0, 0])
        self.assertEqual(solution_lesson4_2(5, [6]), [0, 0, 0, 0, 0])
        self.assertEqual(solution_lesson4_2(5, [1, 6]), [1, 1, 1, 1, 1])
        self.assertEqual(solution_lesson4_2(5, [1, 6, 2]), [1, 2, 1, 1, 1])
        self.assertEqual(solution_lesson4_2(1, [1, 2, 2]), [1])
        self.assertEqual(solution_lesson4_2(1, [1]), [1])
        self.assertEqual(solution_lesson4_2(2, [1, 3]), [1, 1])

    # def test_solution_lesson4_1(self):
    #     self.assertEqual(solution_lesson4_1(5, [1, 3, 1, 4, 2, 3, 5, 4]), 6)
    #     self.assertEqual(solution_lesson4_1(5, [1, 3, 1, 4, 2, 3, 2, 4]), -1)
    #     self.assertEqual(solution_lesson4_1(5, [1]), -1)
    #     self.assertEqual(solution_lesson4_1(1, [1]), 0)
    #     self.assertEqual(solution_lesson4_1(3, [1, 3]), -1)
    #     self.assertEqual(solution_lesson4_1(1, [1, 1, 1, 1]), 0)
    #     self.assertEqual(solution_lesson4_1(2, [1, 1, 1, 1]), -1)

    # def test_solution_lesson3_2(self):
    #     self.assertEqual(solution_lesson3_3([3, 1, 2, 4, 3]), 1)
    #     self.assertEqual(solution_lesson3_3([1, 2]), 1)
    #     self.assertEqual(solution_lesson3_3([1, 2, 3]), 0)
    #     self.assertEqual(solution_lesson3_3([1, 1]), 0)
    #     self.assertEqual(solution_lesson3_3([1, 1, 1]), 1)
    #     self.assertEqual(solution_lesson3_3([1, 1, 1, 1]), 0)
    #     self.assertEqual(solution_lesson3_3([-1, 1]), 2)
    #     self.assertEqual(solution_lesson3_3([-1, 1, -10]), 8)

    # def test_solution_lesson3_2(self):
    #     self.assertEqual(solution_lesson3_2([2, 3, 1, 5]), 4)
    #     self.assertEqual(solution_lesson3_2([2]), 1)
    #     self.assertEqual(solution_lesson3_2([2, 3]), 1)
    #     self.assertEqual(solution_lesson3_2([1]), 2)
    #     self.assertEqual(solution_lesson3_2([1, 3]), 2)
    #     self.assertEqual(solution_lesson3_2([1, 2]), 3)
    #     self.assertEqual(solution_lesson3_2([]), 1)

    # def test_solution_lesson2_2(self):
    #     self.assertEqual(solution_lesson3_1(10, 85, 30), 3)
    #     self.assertEqual(solution_lesson3_1(0, 10, 8), 2)
    #     self.assertEqual(solution_lesson3_1(0, 10, 11), 1)
    #     self.assertEqual(solution_lesson3_1(0, 10, 5), 2)
    #     self.assertEqual(solution_lesson3_1(10, 10, 5), 0)
    #     self.assertEqual(solution_lesson3_1(10, 100, 10), 9)
    #     self.assertEqual(solution_lesson3_1(1, 10, 1), 9)

    # def test_solution_lesson2_2(self):
    #     self.assertEqual(solution_lesson2_2([9,3,9,3,9,7,9]), 7)
    #     self.assertEqual(solution_lesson2_2([1]), 1)
    #     self.assertEqual(solution_lesson2_2([1, 2, 2, 3, 3]), 1)
    #     self.assertEqual(solution_lesson2_2([-1]), -1)
    #     self.assertEqual(solution_lesson2_2([-1, 2, -2, -1, 2]), -2)
    #     self.assertEqual(solution_lesson2_2([2, 2, 3, 3, 4]), 4)

    # def test_solution_lesson2_1(self):
    #     self.assertEqual(solution_lesson2_1([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
    #     self.assertEqual(solution_lesson2_1([0, 0, 0], 1), [0, 0, 0])
    #     self.assertEqual(solution_lesson2_1([1, 2, 3, 4], 4), [1, 2, 3, 4])
    #     self.assertEqual(solution_lesson2_1([1, 2, 3, 4], 5), [4, 1, 2, 3])
    #     self.assertEqual(solution_lesson2_1([], 5), [])

    # def test_solution1(self):
    #     self.assertEqual(solution1(9), 2)
    #     self.assertEqual(solution1(529), 4)
    #     self.assertEqual(solution1(20), 1)
    #     self.assertEqual(solution1(15), 0)
    #     self.assertEqual(solution1(32), 0)
    #     self.assertEqual(solution1(1041), 5)
    #     self.assertEqual(solution1(32), 0)


if __name__ == "__main__":
    unittest.main()