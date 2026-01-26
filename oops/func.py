# multivalue return

def get_user_data():
    return "Khushal", 23

# print(get_user_data())



def chk_age(*,name:str, age:int)-> str:
    if age >= 18:
        return f"Hello {name}, you are an adult."
    else:
        return f"Hello {name}, you are an minor."
    
# print(chk_age(name="khushal",age=23))

def logger(func):
    def wrapper():
        print("--- API Request Started ---")
        func()
        print("--- API Request Finished ---")
    return wrapper

@logger
def get_user_profile():
    print("Fetching data for: Khushal")

get_user_profile()
