from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base, User

# engine = create_engine(url='sqlite:///:memory:')
engine = create_engine(url='sqlite:///db.sqlite')
Base.metadata.create_all(engine)
DatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def find_user_by_id(tg_id):
#     with DatabaseSession() as session:
#         return session.query(User).filter_by(tg_id=tg_id).one_or_none()


def find_user_by_tg_id(tg_id: int) -> User | None:
    with DatabaseSession() as session:
        return session.query(User).filter_by(tg_id=tg_id).one_or_none()


def save_user(tg_id, skills):
    with DatabaseSession() as session:
        user = User(
            tg_id=tg_id,
            pwn=skills.get('Pwn', 0),
            rev=skills.get('Reverse', 0),
            web=skills.get('Web', 0),
            crypto=skills.get('Crypto', 0),
            forensic=skills.get('Forensic', 0),
            ppc=skills.get('PPC', 0),
            pentest=skills.get('Pentest', 0)
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
