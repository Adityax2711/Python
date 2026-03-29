to_do_list=["Buy groceries", "Clean the house", "Pay bills", "Finish project", "Call mom", "Read a book"]
to_do_list.append("Exercise")
to_do_list.append("finish hoomework")
to_do_list.append("plan vacation itinerary")
to_do_list.append("attend team meeting")
to_do_list.append("schedule doctor appointment")
to_do_list.append("organize garage")
print(to_do_list)
if "Pay bills" in to_do_list:
    print("Pay bills")
else:
    print("Task not found.")
to_do_list.remove("Call mom")
for task in to_do_list:
    print(task)
to_do_list.sort()

print("Sorted To-Do List:") 
for task in to_do_list:
    print(task)
#explain the code 
#In this code, we first create a to-do list and add several tasks to it.
#  We then check if a specific task ("Pay bills") is in the list and print it if found. 
# Next, we remove a task ("Call mom") from the list and print all remaining tasks. 
# We sort the list alphabetically and print it, then reverse the order and print it again. 
# Finally, we count the total number of tasks in the list.


to_do_list.reverse()
print("Reversed To-Do List:")
for task in to_do_list:
    print(task)
print(f"Total tasks: {len(to_do_list)}")
completed_tasks = to_do_list[:3]
print("Completed Tasks:")


#create a list grade students
students=["Alice", "Bob", "Charlie", "David", "Eve"]
grades=[85, 92, 78, 90, 88]
grades.append(95)
grades.append(80)
grades.append(82)
grades.append(91)
grades.append(87)
grades.remove(78)
#finding the average grade
average_grade = sum(grades) / len(grades)
print(f"Average Grade: {average_grade}")
#finnd thhe highest and lowest grade 
highest_grade = max(grades)
lowest_grade = min(grades)
print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")  

#create a list of shopping items
shopping_list=["Milk","eggs","bread","fruits","vegetables","meat","cereal","snacks","toiletries","cleaning supplies","pet food","stationery","clothing","electronics","furniture"]
shopping_list.append("shoes")
shopping_list.append("bags")
shopping_list.append("accessories")
shopping_list.append("books")
shopping_list.append("toys")    
shopping_list.remove("toys")
print("Shopping List:")
if "bread" in shopping_list:
    print("bread")
else:
    print("Item not found.")
print("Total items in shopping list:", len(shopping_list))

if "toys" in shopping_list:
    print("toys")
else:
    print("Item not found.")
for item in shopping_list:
    print(item)
shopping_list.sort()
print("Sorted Shopping List:")
for item in shopping_list:
    print(item)
shopping_list.reverse()
print("Reversed Shopping List:")
for item in shopping_list:
    print(item)
print(f"Total items: {len(shopping_list)}")


#create a list of favorite movies
favorite_movies=["Inception","The Dark Knight","Interstellar","Pulp Fiction","The Shawshank Redemption","The Godfather","The Matrix","Forrest Gump","Fight Club","The Lord of the Rings"]
favorite_movies.append("The Social Network")
favorite_movies.append("Gladiator") 
favorite_movies.append("Avatar")
favorite_movies.append("Titanic")
favorite_movies.append("Endgame")
favorite_movies.remove("Fight Club")
print("Favorite Movies:")
if "Inception"in favorite_movies:
    print("Inception")
else:
    print("Movie not found.")
for movie in favorite_movies:
    print(movie)
favorite_movies.sort()
print("Sorted Favorite Movies:")
for movie in favorite_movies:
    print(movie)
favorite_movies.reverse()
print("Reversed Favorite Movies:")
for movie in favorite_movies:
    print(movie)
for movie in favorite_movies:
    print(movie)
for task in completed_tasks:
    print(task)













































































































