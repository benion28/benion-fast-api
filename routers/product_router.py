from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate
from dependencies import get_current_user, get_db

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
    return {"success": True, "message": "Product created"}

@router.get("/")
def list_products(db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.deleted_at == None).all()
    return {"success": True, "data": products}

@router.delete("/{id}")
def delete_product(id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == id).first()
    product.deleted_at = func.now()
    db.commit()
    return {"success": True, "message": "Product deleted"}
