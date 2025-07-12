from app.routers.players import router as players_router
from app.routers.tournaments import router as tournaments_router
from app.routers.matchs import router as matches_router
from app.routers.sets import router as sets_router

routers = [
    players_router,
    tournaments_router,
    matches_router,
    sets_router]