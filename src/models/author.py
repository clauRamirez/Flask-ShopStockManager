class Author:
    def __init__(self, name: str, id: int = None) -> None:
        self.name = name
        self.id = id

    def __repr__(self) -> str:
        return f"Author: {{id: {self.id}, name: {self.name}}}"
    
    def __str__(self) -> str:
        return self.__repr__
