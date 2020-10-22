SELECT distinct(a.cart_id)
FROM cart_products a
JOIN cart_products on a.cart_id = b.cart_id and a.name = 'Milk' and b.name = 'Yogurt'
order by a.cart_id