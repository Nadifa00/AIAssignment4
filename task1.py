#AI-suggested code
def sort_list_of_dicts(list_of_dicts, key):
  return sorted(list_of_dicts, key=lambda x: x[key])

#Manual Implementation using bubble sort algorithm
def sort_list_of_dicts_manual(list_of_dicts, sort_key):
  n = len(list_of_dicts)
  for i in range(n):
    for j in range(0, n - i - 1):
      if list_of_dicts[j][sort_key] > list_of_dicts[j + 1][sort_key]:
        list_of_dicts[j], list_of_dicts[j + 1] = list_of_dicts[j + 1], list_of_dicts[j]
  return list_of_dicts