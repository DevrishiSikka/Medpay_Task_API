# -----------------------------------

# Name: Devrishi Sikka
# API Link: http://127.0.0.1:8000/redoc

# -----------------------------------

from routers import CategoryOperations, SKUOperations, Transactions
from fastapi import FastAPI

app = FastAPI()

# Including all the paths to the main file
app.include_router(Transactions.router)
app.include_router(SKUOperations.router)
app.include_router(CategoryOperations.router)


# This is a dummy operation to test if the API is running or not
@app.get('/')
def Ping():
    return {"message" : "Welcome"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8000)
