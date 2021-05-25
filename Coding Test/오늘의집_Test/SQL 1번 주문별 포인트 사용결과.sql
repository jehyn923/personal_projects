SELECT o.id 'order_id', m.name 'name', IF(p.payment_method = 'point',1,0)	AS 'is_point' 
FROM orders o 
	LEFT OUTER JOIN members m ON o.member_id = m.id
	LEFT OUTER JOIN order_options oo ON o.id = oo.order_id
	LEFT OUTER JOIN payments p ON oo.id = p.order_option_id
	order by o.id asc;
    