from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:27122008@localhost/avtoSELL'
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()

