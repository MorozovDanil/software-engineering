def find(inp_tuple: tuple, find_id: int) -> tuple:
   start_index = -1
   finish_index = len(inp_tuple)
   k = 0

   for i in range(len(inp_tuple)):
       if find_id == inp_tuple[i]:
           start_index = i
           k += 1
           break
   if k != 0:
       for i in range(start_index + 1, len(inp_tuple)):
           if find_id == inp_tuple[i]:
               finish_index = i + 1
               break

   if start_index != -1:
       return inp_tuple[start_index:finish_index]
   else:
       return ()

print(find((1, 8, 3, 4, 8, 8, 9, 2), 8))