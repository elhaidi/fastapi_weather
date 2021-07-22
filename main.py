import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.templating import Jinja2Templates


api = fastapi.FastAPI()
templates = Jinja2Templates('templates')

api.mount('/static', StaticFiles(directory='static'), name='static')


@api.get('/')
def index(request: Request):
    # the underlining templates need the request object rom starlette
    return templates.TemplateResponse('index.html', {'request': request})


if __name__ == '__main__':
    uvicorn.run(api, port=8000, host='127.0.0.1')
