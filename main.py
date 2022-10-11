from fastapi import FastAPI
import stripe
from pydantic import BaseModel

stripe.api_key = "sk_test_51Lq1d0Fb3RklvSdcbUhJPGkAVU7s0xBSfs0BpFytf8nGnWkvidzOyVcKqTPpE8fkiIcF9FQq9ablQWM6KDu5oEvd00HSlH0Zvy"
app = FastAPI()

class Info(BaseModel):
    origin : str
    total: float

@app.post("/webhook")
async def root(info : Info):
    print(info)

    intent = stripe.PaymentIntent.create(
        amount=int(info.total * 100),
        currency="mxn",
        payment_method_types=["card"],
    )

    return {
               "client_secret": intent.get('client_secret'),
               "amount": info.total
           }


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
