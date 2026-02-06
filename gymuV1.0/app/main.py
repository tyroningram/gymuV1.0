# Getting Started, Added CRUD, Path & Query Parameter
#=====================================================

# Data Validation, Added Pydantic
#=================================

from enum import Enum
from fastapi import FastAPI, status, HTTPException
import datetime
from typing import Any

from app.schemas import Transaction, TransactionsCategories

app = FastAPI()


transactions = {
    100 : {
        "amount": 1000,
        "category": "food & groceries",
        "note": "Aldi",
        "date": "2026-02-05 16:03:31.880763",
        "currency": "eur"

    }, 
    101 : {
        "amount": 200,
        "category": "food & groceries",
        "note": "Lidl",
        "date": "2026-02-05 17:53:31.880763",
        "currency": "eur"

    }
}

@app.get("/transaction", response_model=Transaction)
async def get_transactions(id: int):
    if id not in transactions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    return transactions[id]

@app.post("/transaction")
async def create_transaction(transaction: Transaction ) -> Any:
    amount =  transaction.amount
    category = transaction.category
    note = transaction.note
    date = transaction.date
    currency = transaction.currency

    if amount > 9999999:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Max. amount is 99999.99 EUR."
        )
    
    new_id = max(transactions.keys()) + 1
    transactions[new_id] = {
        "amount": amount,
        "category" : category,
        "note": note,
        "date": date,
        "currency": currency
    }

    return {"Status": "Transaction added - 200"}


@app.put("/transcation")
async def update_transaction(id: int, amount: int, category: str, note: str = "No Notes") -> dict[str, Any]:
    found_item = transactions[id]
    found_item["amount"] = amount
    found_item["category"] = category
    found_item["note"] = note
    return found_item

 

@app.patch("/transcation")
async def update_transaction(id: int, body: dict[str, TransactionsCategories]) -> dict[str, Any]:
    transactions[id].update(body)
    return transactions[id]


@app.delete("/transaction")
async def delete_transaction(id: int) -> Any:
    transactions.pop(id)
    return {
        "message": f"Transaction #{id} deleted."
    }

#=====================================================================

@app.get("/transactionDONT/{field}")
async def get_transaction_field(field: str, id: int) -> Any:
    return transactions[id][field]

@app.patch("/transcationDONT")
async def update_transaction(id: int, amount: int | None = None, category: str | None = None, note: str | None = None) -> dict[str, Any]:
    found_transaction = transactions[id]
    if amount: 
        found_transaction["amount"] = amount
    if category: 
        found_transaction["category"] = category
    if note:
        found_transaction["note"] = note
    transactions[id] = found_transaction
    return found_transaction


