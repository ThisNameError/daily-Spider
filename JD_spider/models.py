from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/spider?charset=utf8", max_overflow=5, encoding='utf-8')
Base = declarative_base()


class JDgoods(Base):
    __tablename__ = 'JDgoods'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1024))
    img = Column(String(1024))
    price = Column(String(512))
    commits = Column(String(512))
    shop = Column(String(512))
