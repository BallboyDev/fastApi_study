from fastapi from FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origin = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/hello')
def hello():
    return {'message':"Hello FastApi World"}