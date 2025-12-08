

if __name__ == "__main__":
    pass
import re

class User:
    def __init__(self, uid, name, email):
        self.uid = uid
        self.name = name
        self.email = email
    
    def has_name(self, text):
        return text.lower() in self.name.lower()
    
    def is_valid_email(self):
        return bool(re.match(r'^\S+@\S+\.\S+$', self.email))
    
    def __str__(self):
        return f"{self.name} {self.email}"

class CSVUser(User):
    def __init__(self, data):
        uid, name, email = data.split(';')
        super().__init__(uid, name, email)

class JSONUser(User):
    def __init__(self, data):
        import json
        d = json.loads(data)
        super().__init__(d['uid'], f"{d['first_name']} {d['last_name']}", d['contacts']['email'])

class RawUser(User):
    def __init__(self, data):
        parts = data.split()
        super().__init__('raw', ' '.join(parts[:-1]), parts[-1])

class UserSystem:
    def __init__(self):
        self.users = []
    
    def add(self, data, fmt):
        try:
            user = {'csv': CSVUser, 'json': JSONUser, 'raw': RawUser}[fmt](data)
            self.users.append(user)
        except:
            print(f"Ошибка: {fmt} {data}")
    
    def emails(self):
        return [u.email for u in self.users]
    
    def find(self, name):
        return [u for u in self.users if u.has_name(name)]
    
    def invalid(self):
        return [u for u in self.users if not u.is_valid_email()]

#Пример 
system = UserSystem()
system.add('123;Иван Иванов;ivan@example.com', 'csv')
system.add('{"uid":"42","first_name":"Petr","last_name":"Petrov","contacts":{"email":"petr@example.com"}}', 'json')
system.add('Сидоров Алексей alex@bad', 'raw')

print("Все email:", system.emails())
print("Поиск 'Иван':")
for u in system.find('Иван'):
    print(f"  {u}")
print("Невалидные:")
for u in system.invalid():
    print(f"  {u}")
# Ваш код здесь
