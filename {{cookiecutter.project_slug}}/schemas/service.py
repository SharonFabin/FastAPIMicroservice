from pydantic import BaseModel


class ServiceScheme(BaseModel):
    variable: float | None
