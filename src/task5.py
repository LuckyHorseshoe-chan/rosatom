def compare_versions(A, B):
  if A == B:
    return 0
  A_lst = [int(x) for x in A.split('.')]
  B_lst = [int(x) for x in B.split('.')]
  length = min(len(A_lst), len(B_lst))
  for i in range(length):
    if A_lst[i] > B_lst[i]:
      return 1
    if A_lst[i] < B_lst[i]:
      return -1
  if len(A_lst) > len(B_lst):
    return 1
  return -1


print(compare_versions("1.10", "1.1"), compare_versions("1.10", "2.1"), compare_versions("1.1", "1.1"))