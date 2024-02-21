import sqlite3

conn = sqlite3.connect('testDb.sqlite')

#We will create all the tables first
print ("Opened database successfully");

conn.execute('''CREATE TABLE IF NOT EXISTS `customer` (
  `customer_id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `age` INTEGER NOT NULL
)''')

conn.execute('''CREATE TABLE IF NOT EXISTS `items` (
  `item_id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `item_name` varchar(255) NOT NULL
)''')

conn.execute('''CREATE TABLE IF NOT EXISTS `sales` (
  `sales_id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `customer_id` INTEGER,
  FOREIGN KEY(customer_id) REFERENCES customer(customer_id)
)''')

conn.execute('''CREATE TABLE IF NOT EXISTS `orders` (
  `order_id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `quantity` INTEGER,
  `sales_id` INTEGER,
  `item_id` INTEGER,
  FOREIGN KEY(sales_id) REFERENCES sales(sales_id),
  FOREIGN KEY(item_id) REFERENCES items(item_id)
)''')


print("tables created successfully")


#insert data into tables

conn.execute('''INSERT INTO `customer` (`customer_id`, `age`) VALUES
(1, 21),
(2, 23),
(3, 35)''')

conn.execute('''INSERT INTO `items` (`item_id`, `item_name`) VALUES
(1, 'x'),
(2, 'y'),
(3, 'z')''')

conn.execute('''INSERT INTO `orders` (`order_id`, `sales_id`, `item_id`, `quantity`) VALUES
(1, 1, 1, 3),
(2, 2, 1, 7),
(3, 3, 1, 1),
(4, 4, 2, 1),
(5, 5, 3, 1),
(6, 6, 3, 1),
(7, 7, 3, 1)''')

conn.execute('''INSERT INTO `sales` (`sales_id`, `customer_id`) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 2),
(6, 3),
(7, 3)''')

queryData = conn.execute('''SELECT cu.customer_id, cu.age, it.item_name, SUM(od.quantity)  FROM customer as cu
             JOIN sales as sa ON sa.customer_id=cu.customer_id
             JOIN orders as od ON od.sales_id =sa.sales_id
             JOIN  items AS it ON it.item_id=od.item_id
             GROUP BY od.item_id, sa.customer_id
             ''')

for data in queryData:
    print(data)

