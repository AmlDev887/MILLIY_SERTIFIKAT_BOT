from database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import BigInteger,String
class Users(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(BigInteger,primary_key=True,autoincrement=True)