from dataclasses import dataclass

@dataclass
class Person:
        full_name: str = None
        email: str = None
        current_address: str = None
        permanent_address: str = None

@dataclass
class Table:
        first_name: str = None
        last_name: str = None
        email: str = None
        age: int = None
        salary: int = None
        department: str = None
