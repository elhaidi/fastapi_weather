import json
from pathlib import Path

import fastapi
import uvicorn
from fastapi.responses import RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from services import weather_service
from weather import weather_api
from views import home

api = fastapi.FastAPI()


def configure():
    configure_routes()
    configure_api_key()


def configure_api_key():
    # open the settings.json check for error
    file = Path('setings.json').absolute()
    # check if the file exist
    if not file.exists():
        print(
            f"WARNING: {file} file not found, you cannot continue, please see settings_template.json")
        raise Exception(
            "settings.json file not found, you cannot continue, please see settings_template.json")
    with open(file) as s:
        settings = json.load(s)
        weather_service.api_key = settings.get('api_key')


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
