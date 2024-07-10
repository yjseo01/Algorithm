select f.FLAVOR as FLAVOR
from FIRST_HALF as f left join ICECREAM_INFO as i on f.FLAVOR = i.FLAVOR
where f.TOTAL_ORDER > 3000 and i.INGREDIENT_TYPE = 'fruit_based'
order by f.TOTAL_ORDER DESC;