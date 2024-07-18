from pydantic import BaseModel


class BalanceBase(BaseModel):
    id: int
    amount: float
    user_id: int


class BalanceResponse(BaseModel):
    id: int
    amount: float

    class Config:
        from_attributes = True
