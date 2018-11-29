from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Mogujie

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/spider?charset=utf8", max_overflow=5)
session_maker = sessionmaker(bind=engine)
session = session_maker()


def save_db(result_list):
    for mogu_dict in result_list:
        mogu = Mogujie()
        mogu.tradeitemid = mogu_dict['tradeItemId']
        mogu.img = mogu_dict['img']
        mogu.itemtype = mogu_dict['itemType']
        mogu.clienturl = mogu_dict['clientUrl']
        mogu.link = mogu_dict['link']
        mogu.itemmarks = mogu_dict['itemMarks']
        mogu.acm = mogu_dict['acm']
        # mogu.title = mogu_dict['title']
        mogu.type = mogu_dict['type']
        mogu.orgprice = mogu_dict['orgPrice']
        mogu.hassimilarity = mogu_dict['hasSimilarity']
        mogu.cfav = mogu_dict['cfav']
        mogu.price = mogu_dict['price']
        mogu.similarityurl = mogu_dict['similarityUrl']

        session.add(mogu)
        session.commit()
