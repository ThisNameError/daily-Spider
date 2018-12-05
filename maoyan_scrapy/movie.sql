create database maoyan default character set utf8;

use maoyan;

create table movie(
    id int AUTO_INCREMENT PRIMARY KEY,
    title varchar(256),
    actor varchar(256),
    release_time varchar(128)
);