import fastapi
import uvicorn
from fastapi.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from weather import weather_api
from views import home

api = fastapi.FastAPI()


def configure():
    configure_routes()


def configure_routes():
    # this is to mount all the static files
    api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == '__main__':
    configure()
    uvicorn.run(api, port=8000, host='127.0.0.1')
else:
    configure()
