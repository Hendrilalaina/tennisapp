from app.routers.players import router as players_router
from app.routers.tournaments import router as tournaments_router

routers = [
    players_router,
    tournaments_router]