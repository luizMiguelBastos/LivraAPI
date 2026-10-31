from fastapi import FastAPI
from router.autores_router import router as autores_router
from router.livros_router import router as livros_router

app = FastAPI()

app.include_router(autores_router, prefix="/autores", tags=["autores"])
app.include_router(livros_router, prefix="/livros", tags=["livros"])




