from fastapi import FastAPI, status, HTTPException
import datetime
from typing import Any
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

@app.get("/transactions")
async def get_transactions(id: int | None = None) -> Any:

    if id is None:
        return transactions
    
    if id not in transactions:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transaction not found"
        )

    return transactions[id]


@app.post("/transaction")
async def create_transaction(data: dict[str, Any], note: str = "No Notes" ) -> Any:
    amount =  data["amount"]
    category = data["category"]

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
        "date": datetime.datetime.now(),
        "currency": "eur"

    }

    return {"Status": "Transaction added - 200"}


@app.put("/transcation")
async def update_transaction(id: int, amount: int, category: str, note: str = "No Notes") -> dict[str, Any]:
    found_item = transactions[id]
    found_item["amount"] = amount
    found_item["category"] = category
    found_item["note"] = note
    return found_item


@app.get("/transaction/{field}")
async def get_transaction_field(field: str, id: int) -> Any:
    return transactions[id][field]




