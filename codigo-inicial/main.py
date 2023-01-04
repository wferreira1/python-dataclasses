import uuid

def generate_id() -> str:
    return str(uuid.uuid4())

class Person:

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.agr = age
    
    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

def main() -> None:
    person = Person(first_name='Wesley', last_name='Oliveira', age=35)
    print(person)

if __name__ == '__main__':
    main()