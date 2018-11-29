from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import JDgoods

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1/spider?charset=utf8", max_overflow=5)
session_maker = sessionmaker(bind=engine)
session = session_maker()


def save_good(all_lists):
    good = JDgoods()
    for all_dict in all_lists:
        good.title = all_dict['title']
        good.img = all_dict['img']
        good.price = all_dict['price']
        good.commits = all_dict['commits']
        good.shop = all_dict['shop']

        session.add(good)
        session.commit()
