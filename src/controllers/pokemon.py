from fastapi import APIRouter

router = APIRouter(
    prefix="/pokemon",
)


@router.get("")
async def root():
    return {"message": "Hello World"}
