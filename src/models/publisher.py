class Publisher:
    def __init__(
        self,
        name: str,
        website: str,
        salesperson: str = "No salesperson, order via website",
        contact: str = None,
        id: int = None
    ):
        self.name = name
        self.website = website
        self.salesperson = salesperson
        self.contact = contact
        self.id = id
        
    def __repr__(self) -> str:
        return f"Publisher: {{id: {self.id}, name: {self.name}, website: {self.website}, \
            salesperson: {self.salesperson}, contact: {self.contact} \
        }}"
            