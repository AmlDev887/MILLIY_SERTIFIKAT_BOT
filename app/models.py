from app.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import BigInteger,String,DateTime,func,Boolean
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id:Mapped[int] = mapped_column(BigInteger,primary_key=True,autoincrement=True)
    telegram_id:Mapped[int] = mapped_column(BigInteger,unique=True,nullable=False)
    username:Mapped[str|None] = mapped_column(String(60))
    first_name:Mapped[str|None] = mapped_column(String(60))
    access_type:Mapped[str|None] = mapped_column(String(60),default='normal')
    created_at:Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())

class Subject(Base):
    __tablename__='subjects'

    id:Mapped[int] = mapped_column(BigInteger,primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String,nullable=False)
    is_active:Mapped[bool] = mapped_column(Boolean,nullable=True,default=True)
    
