#Импортируйте в него класс 
from user import User

my_user = User("Имя", "Фамилия")
print(my_user.print_first_name())
print(my_user.print_last_name())
print(my_user.print_full_name())