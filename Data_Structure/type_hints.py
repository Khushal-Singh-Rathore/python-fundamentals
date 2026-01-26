userName: str = "Khushal"
age: int = 25
is_developer: bool = True
user_id:int = 11

def getUser(userId:int) -> str:
    return "Active"

def process_items(*,items: list[str])-> int:
    return len(items)

print(process_items(items=["pen","book"]))