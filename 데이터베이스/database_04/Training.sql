### 1. 모든 테이블의 이름을 출력하세요.
```sql
albums          employees       invoices        playlists
artists         genres          media_types     tracks
customers       invoice_items   playlist_track
```

### 2. 모든 테이블의 데이터를 확인해보세요.
| 공백은 있는지 NULL은 있는지 데이터 타입은 어떤지 등등 데이터를 직접 확인해보세요.
null ㅇ공백 x

### 3. 앨범(albums) 테이블의 데이터를 출력하세요.
| 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.
```sql
SELECT Title
FROM albums
ORDER BY Title DESC
LIMIT 5;
Title
----------------------------
[1997] Black Light Syndrome
Zooropa
Worlds
Weill: The Seven Deadly Sins
Warner 25 Anos
```

### 4. 고객(customers) 테이블의 행 개수를 출력하세요.
| 단, 컬럼명을 `고객 수`로 출력하세요.
```sql
SELECT (SELECT count(*)FROM customers )as '고객 수';
고객 수
----
59
```
### 5. 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력하세요.
| 단, 각각의 컬럼명을 `이름`, `성`으로 출력하고, `이름`을 기준으로 내림차순으로 5개까지 출력하세요.
```sql
SELECT FirstName,LastName
FROM customers
WHERE Country='USA'
ORDER BY FirstName DESC
LIMIT 5;

FirstName  LastName  
---------  ----------
Victor     Stevens
Tim        Goyer
Richard    Cunningham
Patrick    Gray
Michelle   Brooks
```

### 6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.
| 단, 컬렴명을 `송장수`로 출력하세요.
```sql
SELECT COUNT(BillingPostalCode)AS '송장수'
FROM invoices
WHERE BillingPostalCode NOT NULL ;
송장수
---
384
```

### 7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.
| 단, `InvoiceDate`를 기준으로 내림차순으로 5개까지 출력하세요.
```sql
SELECT InvoiceDate
FROM invoices
WHERE BillingPostalCode NOT NULL
ORDER BY InvoiceDate DESC
LIMIT 5;
InvoiceDate        
-------------------
2013-12-22 00:00:00
2013-12-14 00:00:00
2013-12-06 00:00:00
2013-12-05 00:00:00
2013-12-04 00:00:00
```

### 8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.
| `strftime`를 검색해서 활용해보세요.
```sql
SELECT COUNT(InvoiceDate)
FROM invoices
WHERE 

```

### 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.
| 단, 각각의 컬럼명을 `고객ID`, `이름`,`성`으로 출력하고, `고객ID`을 기준으로 오름차순으로 출력하세요.
```sql
``` 

### 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.
| 단, 각각의 컬렴명을 `고객 수`,`나라`로 출력하고, 고객 수 상위 5개의 나라만 출력하세요.
```sql
```

### 11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.
```sql
```

### 12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요
| 단, 앨범 수를 기준으로 내림차순으로 출력하세요.
```sql 
```

### 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.
| 단, `고객 수`, `Country` 순서 기준으로 내림차순으로 5개까지 출력하세요.
```sql 
```

### 14.  고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.
| 단, `CustomerId`와 `Fax 유/무` 컬럼만 출력하고, `CustomerId` 기준으로 오름차순으로 5개까지 출력하세요. 
```sql 
```

### 15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.
| 단, 점원의 `LastName`, `FirstName`, `나이` 컬럼만 출력하고, `EmployeeId`를 기준으로 오름차순으로 출력하세요.

| cast(), strftime(), 오늘 날짜를 구하는 함수를 검색하고, 활용해보세요.
```sql 
``` 

### 16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.
| artists 테이블과 albums 테이블의 `ArtistId` 활용하세요.
```sql 
```

### 17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.
| genres 테이블과 tracks 테이블의 `GenreId` 활용하세요.
```sql 
```


### 자유롭게 문제를 만들어 보시고, 디스코드 채널에 공유해보세요!

# 822

### 1. playlist_track 테이블에 `A`라는 별칭을 부여하고 데이터를 출력하세요.
| 단, 모든 컬럼을 `PlaylistId` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT *
FROM playlist_track AS A
ORDER BY PlaylistId DESC
LIMIT 5;
PlaylistId  TrackId
----------  -------
18          597
17          3290
17          2096
17          2095
17          2094
```

### 2. tracks 테이블에 `B`라는 별칭을 부여하고 데이터를 출력하세요
| 단, 모든 컬럼을 `TrackId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT *
FROM tracks AS B
ORDER BY TrackId ASC
LIMIT 5;

TrackId  Name                                     AlbumId  MediaTypeId  GenreId  Composer
                                          Milliseconds  Bytes     UnitPrice
-------  ---------------------------------------  -------  -----------  -------  -------------------------------------------------------------------------------------------  ------------  --------  ---------
1        For Those About To Rock (We Salute You)  1        1            1        Angus Young, Malcolm Young, Brian Johnson Young, Brian Johnson                     343719        11170334  0.99

2        Balls to the Wall                        2        2            1
                                          342562        5510424   0.99

3        Fast As a Shark                          3        2            1        F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffmann, U. Dirkscneider & W. Hoffman           230619        3990994   0.99

4        Restless and Wild                        3        2            1        F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirksch-Diesel, S. Kaufman, U. Dirkscneider &   252051        4331779   0.99
                                                                                 W. Hoffman

5        Princess of the Dawn                     3        2            1        Deaffy & R.A. Smith-DieselDiesel                                    375418        6290521   0.99
``` 
 
### 3. 각 playlist_track 해당하는 track 데이터를 함께 출력하세요.
| 단, PlaylistId, Name 컬럼을 `PlaylistId` 기준으로 내림차순으로 10개만 출력하세요. 
```sql
SELECT PlaylistId, Name 
FROM  playlist_track INNER JOIN tracks
on playlist_track.TrackId = tracks.TrackId
ORDER BY PlaylistId DESC
LIMIT 10;

PlaylistId  Name
----------  -----------------------
18          Now's The Time
17          The Zoo
17          Flying High Again
17          Crazy Train
17          I Don't Know
17          Looks That Kill
17          Live To Win
17          Ace Of Spades
17          Creeping Death
17          For Whom The Bell Tolls

```  

### 4. `PlaylistId`가 `10`인 track 데이터를 함께 출력하세요. 
| 단, PlaylistId, Name 컬럼을 `Name` 기준으로 내림차순으로 5개만 출력하세요.
```sql
SELECT PlaylistId, Name 
FROM  playlist_track INNER JOIN tracks
on playlist_track.TrackId = tracks.TrackId
WHERE PlaylistId=10
ORDER BY  Name DESC
LIMIT 5;
PlaylistId  Name
----------  ------------------------
10          Women's Appreciation
10          White Rabbit
10          Whatever the Case May Be
10          What Kate Did
10          War of the Gods, Pt. 2

``` 

### 5. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `INNER JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT count(*)
FROM tracks INNER JOIN artists
on tracks.Composer=artists.Name;
count(*)
--------
402
```

### 6. tracks 테이블을 기준으로 tracks `Composer` 와 artists 테이블의 `Name`을 `LEFT JOIN`해서 데이터를 출력하세요.
| 단, 행의 개수만 출력하세요.
```sql
SELECT count(*)
FROM tracks LEFT OUTER JOIN artists
on tracks.Composer=artists.Name;
count(*)
--------
3503
```

### 7. `INNER JOIN` 과 `LEFT JOIN` 행의 개수가 다른 이유를 작성하세요.
```plain
INNER JOIN
A와B 조건에 일치하는 전부
LEFT JOIN
A의전부그래서 A의COUNT 동일
```

### 8. invoice_items 테이블의 데이터를 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceLineId, InvoiceId
FROM invoice_items
ORDER BY InvoiceId ASC
LIMIT 5;
InvoiceLineId  InvoiceId
-------------  ---------
1              1
2              1
3              2
4              2
5              2

``` 

### 9. invoices 테이블의 데이터를 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT InvoiceId, CustomerId
FROM invoices
ORDER BY InvoiceId ASC
LIMIT 5;
InvoiceId  CustomerId
---------  ----------
1          2
2          4
3          8
4          14
5          23

``` 

### 10. 각 invoices_item에 해당하는 invoice 데이터를 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT invoice_items.InvoiceLineId, invoices.InvoiceId
FROM  invoice_items INNER JOIN invoices
on invoice_items.InvoiceId=invoices.InvoiceId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;
InvoiceLineId  InvoiceId
-------------  ---------
2240           412
2226           411
2227           411
2228           411
2229           411
``` 


### 11. 각 invoice에 해당하는 customer 데이터를 함께 출력하세요.
| 단, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT invoices.InvoiceId, customers.CustomerId
FROM invoices INNER JOIN customers
on invoices.CustomerId=customers.CustomerId
ORDER BY invoices.InvoiceId DESC
LIMIT 5;
InvoiceId  CustomerId
---------  ----------
412        58
411        44
410        35
409        29
408        25
``` 

### 12. 각 invoices_item(상품)을 포함하는 invoice(송장)와 해당 invoice를 받을 customer(고객) 데이터를 모두 함께 출력하세요.
| 단, InvoiceLineId, InvoiceId, CustomerId 컬럼을 `InvoiceId` 기준으로 내림차순으로 5개만 출력하세요.
```
SELECT invoice_items.InvoiceLineId, invoice_items.InvoiceId, customers.CustomerId
FROM  invoice_items 
INNER JOIN invoices on invoice_items.InvoiceId=invoices.InvoiceId
INNER JOIN customers on invoices.CustomerId=customers.CustomerId
ORDER BY invoice_items.InvoiceId DESC
LIMIT 5;

InvoiceLineId  InvoiceId  CustomerId
-------------  ---------  ----------
2240           412        58
2239           411        44
2238           411        44
2237           411        44
2236           411        44
```

### 13. 각 cusotmer가 주문한 invoices_item의 개수를 출력하세요.
| 단, CustomerId와 개수 컬럼을 `CustomerId` 기준으로 오름차순으로 5개만 출력하세요.
```sql
SELECT  customers.CustomerId, COUNT(*)
FROM  invoice_items 
INNER JOIN invoices on invoice_items.InvoiceId=invoices.InvoiceId
INNER JOIN customers on invoices.CustomerId=customers.CustomerId
GROUP BY  customers.CustomerId
ORDER BY  customers.CustomerId ASC
LIMIT 5;

CustomerId  COUNT(*)
----------  --------
1           38
2           38
3           38
4           38
5           38
```

