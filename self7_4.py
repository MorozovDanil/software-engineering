with open("censorship.txt", "r") as file:
   line = list(file.readline().split())

   input_str = ("Hello, world! Python IS the programming language of thE future. My EMAIL is...\n"
                "PYTHON is awesome")
   index_next_line = input_str.index("\n")
   print(index_next_line)
   input_list = input_str.split()

   for i in range(len(input_list)):
       for k in range(len(line)):
           if line[k] in input_list[i].lower():
               for j in line[k]:
                   input_list[i] = input_list[i].lower().replace(j, "*")

   out_string = ""
   for i in input_list:
       out_string += i + " "
       if len(out_string) == index_next_line + 1:
           out_string += "\n"
   print(out_string)