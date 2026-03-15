from fastapi import APIRouter
from routes.merchant import router as merchant_router
from routes.address import router as address_router
from routes.receipt import router as receipt_router

router = APIRouter()   

router.include_router(merchant_router)
router.include_router(address_router)
router.include_router(receipt_router)