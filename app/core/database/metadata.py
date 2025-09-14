from sqlmodel import SQLModel

# import models here

def get_target_metadata():
    return SQLModel.metadata