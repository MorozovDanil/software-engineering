def count_most(a):
   numcount = {}
   for i in a:
       numcount[i] = numcount.get(i, 0) + 1
   most_common = sorted(numcount.items(), key=lambda x: x[1], reverse=True)[:3]
   result_dict = {key: value for key, value in sorted(most_common)}
   return result_dict
input_string=input()
print(count_most(input_string))

def most_frequent(a):
    return max(set(a), key=a.count)
result = tuple(input_string)
print(most_frequent(list(result)))