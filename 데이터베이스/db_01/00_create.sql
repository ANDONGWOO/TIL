-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

# 8/18

###  1. 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT COUNT(smoking) FROM healthcare GROUP BY smoking;
COUNT(smoking)
--------------
626138
189808
183711
343

```

###  2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT COUNT(is_drinking) FROM healthcare GROUP BY is_drinking ;
COUNT(is_drinking)
------------------
415119
584685
196
```

### 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(is_drinking) FROM healthcare WHERE blood_pressure>=200 GROUP BY is_drinking;
COUNT(is_drinking)
------------------
6064
1770
```

### 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.

```sql
SELECT sido,COUNT(*) FROM healthcare GROUP BY sido HAVING COUNT(*)>=50000;
sido  COUNT(*)
----  --------
11    166231
26    69025
28    58345
41    247369
47    54438
48    68530
```

### 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.

> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.

```sql
SELECT height,COUNT(*) FROM healthcare GROUP BY height ORDER BY COUNT(*) DESC LIMIT 5;
height  COUNT(*)
------  --------
160     184993
155     181306
165     179352
170     152585
150     128555
```

### 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.

```sql
SELECT height,weight,COUNT(*) FROM healthcare GROUP BY height,weight ORDER BY COUNT(*) DESC LIMIT 5;
height  weight  COUNT(*)
------  ------  --------
155     55      45866
160     60      42454
165     65      40385
155     50      38582
160     55      38066
```

### 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.

```sql 
SELECT is_drinking,AVG(waist),COUNT(*) FROM healthcare GROUP BY is_drinking;
is_drinking  AVG(waist)        COUNT(*)
-----------  ----------------  --------
0            81.2128249971711  415119
1            83.1541594191841  584685
             82.7714285714286  196
```

### 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.

> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

```sql
SELECT gender,round(AVG(va_left),2),round(AVG(va_right),2) FROM healthcare GROUP BY gender;
gender  round(AVG(va_left),2)  round(AVG(va_right),2)
------  ---------------------  ----------------------
1       0.98                   0.99
2       0.88                   0.88
```

### 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.

> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

```sql
SELECT age,AVG(height),AVG(weight) FROM healthcare GROUP BY age HAVING height>=160 and weight>=60;
age  AVG(height)       AVG(weight)     
---  ----------------  ----------------
9    165.66545300972   67.2402208898302
10   164.119689244962  65.677140776194
18   150.440115440115  51.0261343594677
```

### 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.

```sql

SELECT is_drinking,smoking,AVG(mod(weight,(height*height)))
FROM healthcare 
WHERE length(smoking)>=1 AND length(is_drinking)>=1
GROUP BY is_drinking,smoking;
is_drinking  smoking  AVG(mod(weight,(height*height)))
-----------  -------  --------------------------------
0            1        57.6585362245955
0            2        67.2995534180694
0            3        66.4663447117404
1            1        61.2964422622851
1            2        70.3737630199422
1            3        69.4941839971801

```
# 8/19 복습

SELECT id, gender
FROM healthcare
LIMIT 5;
id  gender
--  ------
1   1     
2   2     
3   2     
4   1     
5   2 

-- 성별 1(남자), 2(여자)
SELECT id,CASE WHEN gender=1 THEN '남자'WHEN gender=2 THEN '여자'end as 성별
FROM healthcare
LIMIT 50;
id  성별
--  --  
1   남자
2   여자
3   여자
4   남자
5   여자

-- 흡연(smoking)

SELECT id,CASE WHEN smoking=1 THEN '비흡연자'WHEN smoking=2 THEN '흡연자' WHEN smoking=3 THEN '헤비스모커' ELSE '무응답' END as 흡연자
FROM healthcare
LIMIT 50;

id  흡연자  
--  -----
1   비흡연자
2   비흡연자
3   비흡연자
4   비흡연자
5   비흡연자
6   헤비스모커
7   헤비스모커
8   헤비스모커
9   비흡연자
10  비흡연자
11  비흡연자
12  헤비스모커
13  헤비스모커
14  비흡연자
15  비흡연자
16  헤비스모커
17  비흡연자
18  비흡연자
19  헤비스모커
20  비흡연자
21  비흡연자
22  비흡연자
23  비흡연자
24  헤비스모커
25  비흡연자
26  비흡연자
27  흡연자
28  비흡연자
29  흡연자
30  비흡연자 
31  비흡연자
32  비흡연자
33  헤비스모커
34  비흡연자
35  비흡연자
36  비흡연자
37  비흡연자
38  흡연자
39  비흡연자
40  비흡연자
41  흡연자
42  헤비스모커
43  비흡연자
44  비흡연자
45  흡연자
46  비흡연자
47  흡연자
48  비흡연자
49  헤비스모커
50  비흡연자


