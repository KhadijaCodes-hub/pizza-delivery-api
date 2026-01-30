from fastapi import APIRouter

order_router=APIRouter(
    prefix="/orders",
    tags=['Orders']
)

@order_router.get("/")
async def greet():
    return {"message":"Hello World"}