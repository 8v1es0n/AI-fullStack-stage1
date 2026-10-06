-- 员工表
create table employee (
  id int unsigned primary key auto_increment comment '主键',
  name varchar(10) not null comment '姓名',
  gender tinyint unsigned not null comment '性别, 1:男, 2:女',
  job tinyint unsigned comment '职位, 1:班主任, 2:讲师, 3:学工主管, 4:教研主管, 5:咨询师',
  salary int unsigned not null comment '薪资',
  entry_date date comment '入职日期',
  create_time datetime comment '创建时间',
  update_time datetime comment '更新时间'
)  comment '员工信息表';

INSERT INTO employee (id, name, gender, job, salary, entry_date, create_time, update_time) VALUES
       (1,'夫子',1,4,30000,'2005-08-19','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (2,'颜瑟',1,3,18000,'2010-03-22','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (3,'君陌',1,2,22000,'2015-09-01','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (4,'李慢慢',1,2,17000,'2018-12-25','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (5,'叶红鱼',2,2,21000,'2013-07-14','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (6,'柳白',1,2,13000,'2021-04-17','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (7,'余帘',2,2,14500,'2020-10-31','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (8,'宁缺',1,1,6800,'2022-06-11','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (9,'李渔',2,1,4500,'2024-02-28','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (10,'唐小棠',2,1,6000,'2017-05-09','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (11,'陈皮皮',1,1,4700,'2025-01-15','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (12,'桑桑',2,5,8000,'2023-08-08','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (13,'莫山山',2,5,6500,'2020-10-31','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (14,'隆庆',1,5,5500,'2016-09-22','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (15,'夏侯',1,5,7500,'2011-12-12','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (16,'曲妮',2,5,6800,'2024-06-01','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (17,'何明池',1,5,6200,'2019-03-19','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (18,'陆晨迦',2,5,5800,'2015-09-01','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (19,'唐王',1,5,6800,'2022-07-07','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (20,'卫光明',1,2,19000,'2009-11-11','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (21,'朝小树',1,2,18500,'2020-05-05','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (22,'夏天',2,1,5500,'2014-08-16','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (23,'钟大俊',1,1,5500,'2015-09-01','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (24,'柯浩然',2,2,21000,'2023-01-01','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (25,'齐四',1,1,6500,'2018-10-10','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (26,'叶苏',1,5,5200,'2025-03-03','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (27,'七念',2,5,5500,'2015-06-18','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (28,'程立雪',2,5,6000,'2012-09-09','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (29,'观主',1,2,21000,'2007-07-07','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (30,'熊初墨',1,5,7000,'2024-04-04','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (31,'水珠儿',1,2,5000,'2019-09-23','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (32,'徐崇山',1,NULL,13000,'2021-12-25','2026-06-16 16:30:39','2026-06-16 16:30:39'),
       (33,'司徒依兰',2,NULL,22500,'2013-03-21','2026-06-16 16:30:39','2026-06-16 16:30:39');



-- =================== DQL: 基本查询 ======================

-- 1. 查询指定字段 name, entry_date 并返回
SELECT name, entry_date FROM employee;

-- 2. 查询返回所有字段
-- 推荐写法（明确列出字段，性能更好且不易受表结构变更影响）
SELECT id, name, gender, job, salary, entry_date, create_time, update_time FROM employee;
-- 简化写法
SELECT * FROM employee;

-- 3. 查询所有员工的 name, entry_date, 并起别名(name的别名为姓名、entry_date的别名为入职日期)
SELECT name AS '姓名', entry_date AS '入职日期' FROM employee;

-- 4. 查询已有的员工关联了哪几种职位(不要重复) - distinct
SELECT DISTINCT job FROM employee;


-- =================== DQL: 条件查询 ======================

-- 1. 查询 姓名 为 莫山山 的员工
SELECT * FROM employee WHERE name = '莫山山';

-- 2. 查询 薪资小于等于5000 的员工信息
SELECT * FROM employee WHERE salary <= 5000;

-- 3. 查询 没有分配职位 的员工信息
SELECT * FROM employee WHERE job IS NULL;

-- 4. 查询 有职位 的员工信息
SELECT * FROM employee WHERE job IS NOT NULL;

-- 5. 查询 职位不是讲师(job=2) 的员工信息
SELECT * FROM employee WHERE job != 2;
SELECT * FROM employee WHERE job <> 2;
-- 或者使用 <>
-- SELECT * FROM employee WHERE job <> 2;

-- 6. 查询 入职日期 在 '2020-01-01' (包含) 到 '2025-01-01'(包含) 之间的员工信息
SELECT * FROM employee WHERE entry_date >= '2020-01-01' AND entry_date <= '2025-01-01';
-- 或者使用 BETWEEN ... AND ... (包含边界值)
-- SELECT * FROM employee WHERE entry_date BETWEEN '2020-01-01' AND '2025-01-01';

-- 7. 查询 入职时间 在 '2020-01-01' (包含) 到 '2025-01-01'(包含) 之间 且 性别为女(gender=2) 的员工信息
SELECT * FROM employee
WHERE entry_date BETWEEN '2020-01-01' AND '2025-01-01'
  AND gender = 2;

-- 8. 查询 职位是 2 (讲师), 3 (学工主管), 4 (教研主管) 的员工信息
SELECT * FROM employee WHERE job IN (2, 3, 4);

-- 9. 查询 姓名 为两个字的员工信息 (_ 表示一个字符)
SELECT * FROM employee WHERE name LIKE '__';

-- 10. 查询 姓 '李' 的员工信息
SELECT * FROM employee WHERE name LIKE '李%';

-- 11. 查询 姓名中包含 '小' 的员工信息
SELECT * FROM employee WHERE name LIKE '%小%';


-- =================== DQL: 分组查询 ======================
-- 聚合函数 ----> 所有的聚合函数不参与null值的统计

-- 1. 统计该企业员工数量 - count
SELECT COUNT(*) FROM employee;        -- 【推荐】统计总行数，不受NULL影响
-- SELECT COUNT(id) FROM employee;    -- 按主键统计
-- SELECT COUNT(1) FROM employee;     -- 按常量统计

-- 2. 统计该企业员工的平均薪资 - avg
SELECT AVG(salary) FROM employee;

-- 3. 统计该企业员工的最低薪资 - min
SELECT MIN(salary) FROM employee;

-- 4. 统计该企业员工的最高薪资 - max
SELECT MAX(salary) FROM employee;

-- 5. 统计该企业每月要给员工发放的薪资总额(薪资之和) - sum
SELECT SUM(salary) FROM employee;


-- 分组
-- 注意: 一旦进行了group by 分组操作之后, select之后的字段列表只能写: 分组字段、聚合函数

-- 1. 根据性别分组, 统计男性和女性员工的数量
SELECT gender, COUNT(*) AS employee_count
FROM employee
GROUP BY gender;

-- 2. 先查询入职时间在 '2015-01-01' (包含) 以前的员工, 并对结果根据职位分组, 获取员工数量大于等于2的职位
SELECT job, COUNT(*) AS emp_count
FROM employee
WHERE entry_date < '2015-01-01'
GROUP BY job
HAVING COUNT(*) >= 2;


-- =================== 排序查询 ======================

-- 1. 根据入职时间, 对员工进行升序排序
SELECT * FROM employee ORDER BY entry_date ASC;

-- 2. 根据入职时间, 对员工进行降序排序
SELECT * FROM employee ORDER BY entry_date DESC;

-- 3. 根据 入职时间 升序排序，入职时间相同再按照 薪资 降序排序
SELECT * FROM employee ORDER BY entry_date ASC, salary DESC;


-- =================== 分页查询 ======================
-- limit 起始索引, 每页展示记录数
-- 公式: 起始索引 = (页码 - 1) * 每页展示记录数

-- 1. 从起始索引0开始查询员工数据, 每页展示5条记录
SELECT * FROM employee LIMIT 0, 5;

-- 2. 查询 第1页 员工数据, 每页展示5条记录  → (1-1)*5 = 0
SELECT * FROM employee LIMIT 0, 5;

-- 3. 查询 第2页 员工数据, 每页展示5条记录  → (2-1)*5 = 5
SELECT * FROM employee LIMIT 5, 5;

-- 4. 查询 第3页 员工数据, 每页展示5条记录  → (3-1)*5 = 10
SELECT * FROM employee LIMIT 10, 5;

-- 5. 查询第6页, 每页展示5条记录  → (6-1)*5 = 25
SELECT * FROM employee LIMIT 25, 5;


-- ---------------------------------------- 事务管理 ---------------------------------
-- 员工操作日志表
create table employee_log (
    id int unsigned primary key auto_increment comment '主键',
    employee_id int unsigned not null comment '员工ID',
    operation varchar(20) not null comment '操作类型, insert/update/delete',
    note text comment '备注',
    create_time datetime comment '操作时间'
) comment '员工操作日志表';


-- 给ID为5,6 的员工调薪(增加2000), 同时记录操作日志;
start transaction ;


-- 执行业务操作
-- a. 调薪
update employee set salary = salary + 2000 where id in(7, 8);
-- b. 记录操作日志
insert into employee_log(employee_id, operation, note, create_time) VALUES (7, 'update', '涨薪2000', now());
insert into employee_log(employee_id, operation, note, create_time) VALUES (8, 'update', '涨薪2000', now());

select * from employee where id in (7,8);


commit ; / rollback;