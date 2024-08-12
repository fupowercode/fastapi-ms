from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import Product
from typing import List

app = FastAPI()

# Configurar Jinja2
templates = Jinja2Templates(directory="app/templates")

products = []

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Renderizar la página de inicio con instrucciones."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/products/", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product

@app.get("/products/", response_model=List[Product])
def get_products():
    return products

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            del products[index]
            return {"message": "Product deleted"}
    raise HTTPException(status_code=404, detail="Product not found")
