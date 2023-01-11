create table products(
productid VARCHAR(10),
product_name varchar(255),
product_supplier varchar(10),
price float,
quantity int,
category varchar(11)
);

create table customers(
cus_id varchar(50) primary key,
first_name varchar(20),
last_name varchar(20),
email varchar(30),
phone varchar(30)
);

create table orders(
order_id VARCHAR(10),
order_date date,
cus_id varchar(50),
productid varchar(50),
foreign key (cus_id) references customers(cus_id) 
on delete cascade,
foreign key (productid) references 
products(productid) on delete cascade
);
