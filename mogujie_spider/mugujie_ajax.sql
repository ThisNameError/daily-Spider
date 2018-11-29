use spider;

create table mogujie(
    id int AUTO_INCREMENT PRIMARY KEY,
    tradeitemid varchar(512),
    img varchar(1024),
    itemtype varchar(512),
    clienturl varchar(1024),
    link varchar(1024),
    itemmarks varchar(512),
    acm varchar(512),
    price_taglist varchar(512),
    title varchar(512),
    type varchar(512),
    orgprice varchar(512),
    hassimilarity varchar(512),
    lefttop_taglist varchar(512),
    cfav varchar(512),
    price varchar(512),
    leftbottom_taglist varchar(512),
    similarityurl varchar(1024)
);
