SELECT *
FROM table_order
JOIN order_menu_item ON table_order.table_id = order_menu_item.order_id
JOIN menu_item ON menu_item.menu_item_id = order_menu_item.menu_item_id
join tbl on tbl.table_id = table_order.table_id
join waiter on waiter.waiter_id = table_order.waiter_id