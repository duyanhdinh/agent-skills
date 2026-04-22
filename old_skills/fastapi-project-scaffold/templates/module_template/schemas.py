from pydantic import BaseModel


class {{ module_class }}Create(BaseModel):
    pass


class {{ module_class }}Read(BaseModel):
    id: int
