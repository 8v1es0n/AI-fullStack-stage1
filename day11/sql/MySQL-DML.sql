-- 员工表
create table employee
(
    id          int unsigned primary key auto_increment comment '主键',
    name        varchar(10)      not null comment '姓名',
    gender      tinyint unsigned not null comment '性别, 1:男, 2:女',
    job         tinyint unsigned comment '职位, 1:班主任, 2:讲师, 3:学工主管, 4:教研主管, 5:咨询师',
    salary      int unsigned     not null comment '薪资',
    entry_date  date comment '入职日期',
    create_time datetime comment '创建时间', -- 记录数据创建时间
    update_time datetime comment '更新时间'  -- 记录数据修改时间
) comment '员工信息表';


-- DML : 数据操作语言
-- DML : 插入数据 - insert
-- 1. 为 employee 表的 name, gender, job, salary 字段插入值
insert into employee(name, gender, job, salary)
values ('张伟', 1, 1, 12000),
       ('李娜', 2, 2, 9500),
       ('王强', 1, 3, 15000),
       ('赵敏', 2, 4, 16000);

-- 2. 为 employee 表的 所有字段插入值 -->
insert into employee(name, gender, job, salary, entry_date, create_time, update_time)
values ('刘洋', 1, 5, 8000, '2024-01-08', NOW(), NOW()),
       ('陈静', 2, 2, 9800, '2023-09-12', NOW(), NOW()),
       ('杨磊', 1, 1, 12500, '2023-05-22', NOW(), NOW()),
       ('黄丽', 2, 5, 8500, '2024-02-18', NOW(), NOW()),
       ('周杰', 1, 2, 10000, '2023-07-30', NOW(), NOW());
-- 简化写法
insert into employee
values (1001, '吴芳', 2, 3, 14500, '2023-01-05', NOW(), NOW()),
       (1002, '郑浩', 1, 4, 15500, '2022-12-01', NOW(), NOW()),
       (1003, '孙婷', 2, 1, 11800, '2023-11-15', NOW(), NOW()),
       (1004, '马超', 1, 5, 7800, '2024-03-01', NOW(), NOW()),
       (1005, '朱琳', 2, 2, 9600, '2023-08-20', NOW(), NOW());
-- now() : 获取当前系统时间

-- 3. 批量为 employee 表的 name, gender, job, salary 字段插入数据
insert into employee
values (null, '胡斌', 1, 3, 14800, '2022-10-15', NOW(), NOW()),
       (null, '林雪', 2, 4, 16500, '2022-07-25', NOW(), NOW()),
       (null, '何军', 1, 1, 12200, '2023-04-10', NOW(), NOW());


-- DML : 更新数据 - update
-- 1. 将 employee 表的所有员工的入职日期更新为 '2010-01-01' 【不带条件的更新是一个比较危险的操作, 将会更新整张表的所有数据】
update employee
set entry_date  = '2035-12-13',
    update_time = now()
where id = 3;

-- 2. 将 employee 表的ID为1的员工 姓名更新为 '张三丰', 性别更新为男;
update employee
set name  = '张三丰',
    gender = 1,
    update_time = now()
where id = 1;

-- 3. 将 employee 表的所有员工, 每人涨薪500
update employee
set salary = salary + 500,
    gender = 1;

-- DML : 删除数据 - delete
-- 1. 删除 employee 表中 ID为1的员工
delete from employee where id = 1;

-- 2. 删除 employee 表中的所有员工
-- 把表中的数据都删除
delete from employee;

-- 摧毁表,并重建
truncate employee;

-- 删除表
drop table employee;