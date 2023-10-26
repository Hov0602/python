import re
def username(fn):
    def wrap(**kwargs):
        username = kwargs.get('username' , '')       
        if not isinstance(username , str) or isinstance(username ,int):
            print('please input alpha numeric')
        if  'user' in username or 'root' in username or 'admin' in username:
            print('do not use admin and user ,root')
        if not len(username) >= 5 and len(username) <=20:
            print('length is false')
        return fn(**kwargs) 
    return wrap

def email(fn):
     def wrap(**kwargs):
        email = kwargs.get('email', '')
        patern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.search(patern , email):
            raise ValueError('Invalid email format')
        return fn(**kwargs)
     return wrap

def phone(fn):
    def wrap(**kwargs):
        phone = kwargs.get('phone' , '')
        pattern = r"^(\+374[0-9]{8})|(0[0-9]{8})$"
        if not re.search(pattern , phone):
           raise ValueError('Invalid phone format')
        return fn(**kwargs)
    return wrap

def password(fn):
    def wrap(**kwargs):
        password = kwargs.get('password' ,'')
        if not len(password) >= 8:
            raise ValueError('invalid password length')
        if not re.search(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])' , password):
            print(' one digit one upper one lower')
        return fn(**kwargs)
    return wrap

def pass_repeat(fn):
    def wrap(**kwargs):
        
        pass_repeat = kwargs.get('pass_repeat' ,'')
        if not pass_repeat == kwargs.get('password' ,''):
            raise ValueError('invalid password repeat')
        return fn(**kwargs)
    return wrap

@pass_repeat
@password
@phone
@email
@username

def user(username , email ,phone ,password, pass_repeat):
    return username , email ,phone , password


print(user(username = 'hovHHs6' , email = 'askdbfashdf@il.com' ,phone = '058633155', password = 'Hovo1999' , pass_repeat='Hovo1999'))



        
