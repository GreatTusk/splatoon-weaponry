from fastapi import FastAPI
from app.feature.weapon.controller import weapon_controller

app = FastAPI()
app.include_router(weapon_controller.router)


@app.get("/")
def main():
    return {'message': 'Welcome!'}
