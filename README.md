# lunch-menu
- [x] 팀원들의 점심 메뉴를 수집
- [x] 분석
- [ ] 알람(입력하지 않은 사람들에게 ...)
- [ ] CSV to DB

## Ready
### Install DB with Docker
```bash
$ sudo docker run --name local-postgres \
-e POSTGRES_USER=sunsin \
-e POSTGRES_PASSWORD=mysecretpassword \
-e POSTGRES_DB=sunsindb \
-p 5432:5432 \
-d postgres:15.10
```

### Create Table
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

## Dev
```bash
# DB Check, Start, Stop
$ sudo docker ps -a
$ sudo docker start local-postgres
$ sudo docker stop local-postgres

# Into CONTAINER
$ sudo docker exec -it local-postgres bash
```
