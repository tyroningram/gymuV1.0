from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime

class TransactionsCategories(str, Enum):
    rent = "Rent"
    food_and_groceries = "Food/Grocery"
    gym = "Gym"
    entertainment = "Entertainment"
    lifestyle = "Lifestyle"
    utility = "Utility"
    subscriptions = "Subscriptions"
    phone_bill = "Phone Bill"
    education = "Education"
    travel = "Travel"
    savings = "Savings"
   

class Transaction(BaseModel):
    amount: int = Field(description="Amount in Cent" ,gt=10, le=9999999)
    category: TransactionsCategories
    note: str = Field(default="", max_length=50)
    date: datetime = Field(default_factory=datetime.now)
    currency: str = Field(default="eur")

