use myasset;
CREATE TABLE member_table (
 seq        INT NOT NULL AUTO_INCREMENT,
 mb_id     VARCHAR(20),
 mb_pw    VARCHAR(20),
 mb_addr   VARCHAR(50),
 mb_phone    VARCHAR(50),  
  PRIMARY KEY(seq)
) CHARSET=utf8;
select * from myasset.member_table;

insert into myasset.member_table(mb_id, mb_pw, mb_addr, mb_phone) values ('20204000','400abc','대구 중구','01040004000');

desc member_table;