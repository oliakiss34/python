#Импортируйте в него класс 
from user import User

my_user = User("Имя", "Фамилия")
print(my_user.get_first_name())
print(my_user.get_last_name())
print(my_user.get_full_name())