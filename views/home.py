import fastapi
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from starlette.templating import Jinja2Templates

router = fastapi.APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('home/index.html', {'request': request})


@router.get('/favicon.ico')
def favicon():
    return RedirectResponse(url='/static/img/favicon.ico')
