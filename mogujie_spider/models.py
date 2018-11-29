from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/spider?charset=utf8", max_overflow=5, encoding='utf-8')
Base = declarative_base()


class Mogujie(Base):
    __tablename__ = 'mogujie'
    id = Column(Integer, primary_key=True, autoincrement=True)    #主键，自增
    tradeitemid = Column(String(512))
    img = Column(String(1024))
    itemtype = Column(String(512))
    clienturl = Column(String(1024))
    link = Column(String(1024))
    itemmarks = Column(String(512))
    acm = Column(String(512))
    title = Column(String(2048))
    type = Column(String(512))
    orgprice = Column(String(512))
    hassimilarity = Column(String(512))
    cfav = Column(String(512))
    price = Column(String(512))
    similarityurl = Column(String(1024))
