# -*- coding: utf-8 -*-
import pymysql


class Mysql:
    def __init__(self):
        # 连接数据库
        self.count = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="990209",
            db="test"
        )

    def execute_sql(self, sql):
        """
        执行插入/更新/删除语句
        """
        try:
            # 创建数据库对象
            database = self.count.cursor()
            # 执行sql命令
            database.execute(sql)
            # 保存操作
            self.count.commit()
        except Exception as e:
            print(e)
        finally:
            # 关闭数据库连接
            self.count.close()

    def select(self, sql, *args):
        """
        执行查询语句
        """
        try:
            # 创建数据库对象
            database = self.count.cursor()
            # 执行sql命令
            database.execute(sql, args)
            result = database.fetchall()
            if len(result) == 1:
                # absolute绝对偏移，游标重置，从头开始偏移
                database.scroll(0, mode='absolute')
                result = database.fetchone()
            return result
        except Exception as e:
            print(e)
        finally:
            # 关闭数据库连接
            self.count.close()


db = Mysql().select("select name,age,count(*) from user group by age having age = 23")
print(db)

'''
MySQL 是一个关系型数据库管理系统
主键：主键是唯一的。一个数据表中只能包含一个主键。你可以使用主键来查询数据。
外键：外键用于关联两个表。
索引：使用索引可快速访问数据库表中的特定信息
约束：主键约束(primary key) PK
     自增长约束(auto_increment)
     非空约束(not null)
     唯一性约束(unique)
     默认约束(default)
     零填充约束(zerofill)
     外键约束(foreign key) FK
     
show databases;
use test;
show tables;
create table user(
    id int unsigned primary key not null auto_increment,
    name varchar(20),
    age int,
    sex varchar(3),
    leng float(3,2)
);
insert into user(name,age,sex,leng) values ("小花",23,"女",1.69),
                                           ("小华",29,"男",1.55),
                                           ("小草",23,"女",1.72);
select * from user;
update  user set leng = 1.75 where id = 1 or id = 2;
delete  from user where name="小明" and leng=1.75;

#内连接（查询两个表中存在对于关系的数据，无对应关系的数据不显示）
select * from score  inner join user  on score.name = user.name;
#左连接(查询score表中name等于user表中name的数据)
select score.* from score  left join user  on score.name = user.name;
#右连接（查询score表中语文成绩大于60的学生信息）
select user.*,score.Chiness from score right join user on score.name=user.name where score.Chiness>=60;
select * from score;
#修改表中列的名字
alter table score change Chiness Chinese int;
#模糊查询（使用like关键字，%匹配任意字符）
select * from user where name like '%小%';
#范围查询
select * from user where age between 20 and 30;
#判断数据是否为空(''可以为空格与null不一样)
select * from user where age is null;
#查询age升序，当age相同时按照leng降序(order by默认为升序，asc：升序，desc：降序)
select * from user order by age, leng desc;
#聚合函数：count(*)统计数据总数，max()最大值,min()最小值,avg()平均值,sum()和
select count(*) from user;
select max(age) from user;
select min(age) from user;
select avg(age) from user;
select sum(age) from user;
#分组查询（group by需要和聚合函数一起使用,可以使用having对分组后的数据进行条件查询）
select name,age,count(*) from user group by age having age = 23;

'''
