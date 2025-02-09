ft_list = ["Hello", "tata!"] #dynamic arrays
ft_tuple = ("Hello", "toto!") #fixed memory block stored on program's stack
ft_set = {"Hello", "tutu!"} #hash table (content is hashed to definite each key)
ft_dict = {"Hello" : "titi!"} #hash table with personalized keys to order content

#your code here
ft_list[1] = "World!"

ft_tuple = ("Hello", "France!")

ft_set.remove("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"
#--

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)