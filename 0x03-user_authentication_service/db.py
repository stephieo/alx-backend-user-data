#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User
# from typing import TypeVar


# T = TypeVar('T', bound=Base)  #  for annotating all ORM objects

class DB:
    """DB class. Handler for Database

       Methods:
            add_user: Add user to User table
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """creates and saves a user to the user table in database"""
        session = self._session
        user = User(email=email, hashed_password=hashed_password)
        session.add(user)
        session.commit()
        return user

    def find_user_by(self, **kwargs: dict) -> User:
        """sends a query to the users table"""
        for key, value in kwargs.items():
            if key not in User.__dict__:
                raise InvalidRequestError
            
        for usr in self._session.query(User):
            if getattr(usr, k) == v:
                return usr
        #     return .filter_by(**kwargs).first()
        # except NoResultFound as e:
        #     raise e
        raise NoResultFound

