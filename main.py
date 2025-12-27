import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.auth.route.auth_route import auth_router
from app.user.route.user_route import user_router
from app.user.model.user_model import User
from app.todo.model.todo_model import Todo

openapi_tags = [
    {
        "name": "Users",
        "description": "description",
    },
    {
        "name": "Health Check",
        "description": "Application Health check",
    }
]
app = FastAPI(openapi_tags=openapi_tags)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            str(origin).strip() for origin in settings.BACKEND_CORS_ORIGINS
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

app.include_router(auth_router, prefix=settings.API_PREFIX)
app.include_router(user_router, prefix=settings.API_PREFIX, tags=["Users"])
@app.get("/health")
async def read_root():
    return {"health": "true"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)