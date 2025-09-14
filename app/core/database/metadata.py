from sqlmodel import SQLModel

from .weapon import *

def get_target_metadata():
    return SQLModel.metadata