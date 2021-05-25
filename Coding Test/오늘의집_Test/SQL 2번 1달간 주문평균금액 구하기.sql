SELECT m.name 'member_name',round(avg(oo.amount)) 'avg_amount', count(o.id) 'oder_count'

FROM orders o
	LEFT OUTER JOIN members m ON o.member_id = m.id
	LEFT OUTER JOIN order_options oo ON o.id = oo.order_id
	LEFT OUTER JOIN payments p ON oo.id = p.order_option_id
WHERE p.created_at between date("2020-12-1") and date("2021-1-1")
	group by m.name
	order by round(avg(oo.amount)) desc, count(o.id) asc;	
	
	