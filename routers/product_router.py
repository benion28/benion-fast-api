from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.product_model import Product
from schemas.product_schema import ProductCreate
from core.dependencies import get_current_user, get_db
from sqlalchemy import func
from core.index import ApiResponse

router = APIRouter(prefix="/products")


@router.post("/")
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_product = Product(
        title=product.title,
        price=product.price,
        creator_id=current_user.id
    )
    db.add(db_product)
    db.commit()

    return ApiResponse.success(
        data=db_product,
        message="Product created"
    )


@router.get("/")
def list_products(db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.deleted_at == None).all()
    return ApiResponse.success(
        data=products,
    )


@router.delete("/{id}")
def delete_product(id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == id).first()
    product.deleted_at = func.now()
    db.commit()
    return ApiResponse.success(
        message="Product deleted"
    )
