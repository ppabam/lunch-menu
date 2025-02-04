# lunch-menu

## Table
- postgres
```sql
CREATE TABLE public.lunch_menu (
	id serial NOT NULL,
	menu_name text NOT NULL,
	member_name text NOT NULL,
	dt date NOT NULL,
	CONSTRAINT lunch_menu_pk PRIMARY KEY (id)
);
```
