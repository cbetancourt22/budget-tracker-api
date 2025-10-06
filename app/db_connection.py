from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class ServiceFactory:
    def __init__(self, service_cls):
        self.service_cls = service_cls

    def __call__(self, db: Session = Depends(get_db)):
        return self.service_cls(db)
