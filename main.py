from fastapi import FastAPI
from deps import routers
import uvicorn


app = FastAPI()


app.include_router(routers.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

