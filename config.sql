create table config(id int, topic_name varchar(60),
broker_server_list varchar(100),twitter_name varchar(1200),
createdBy varchar(200),createdDate date, 
updatedBy varchar(100),updatedtimestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
status boolean)
INSERT INTO config values(1,'hack2018','localhost:9092','java, usa, politics,sport,soccer','anji','2018-12-14','anji',current_timestamp,true)
