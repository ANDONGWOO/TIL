# 사전 설정

## 실행

```bash
$ sqlite3 healthcare.sqlite3 
```

## Column 출력 설정

```sql
sqlite3> .headers on 
sqlite3> .mode column
```

## table 및 스키마 조회

```sql
sqlite3> .tables
healthcare

sqlite3> .schema healthcare
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

blood_pressure INTEGER 
NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);
```
# 8/16

# 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare;
```

```
COUNT(*)
--------
1000000
```

### 2. 나이 그룹이 10(age)미만인 사람의 수를 출력하시오.

```sql
sqlite> SELECT COUNT(*) FROM healthcare where age<10;
```
156277
```
```

### 3. 성별이 1인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare where gender=1;
```
510689
```
```

### 4. 흡연 수치(smoking)가 3이면서 음주(is_drinking)가 1인 사람의 수를 출력하시오.

```sql
 SELECT COUNT(*) FROM healthcare where smoking=3 AND is_drinking;  
```
150361
```
```

### 5. 양쪽 시력이(va_left, va_right) 모두 2.0이상인 사람의 수를 출력하시오.

```sql
SELECT COUNT(*) FROM healthcare where va_left>=2.0 AND va_right>=2.0;

```
2614
```
```

### 6. 시도(sido)를 모두 중복 없이 출력하시오.

```sql
SELECT DISTINCT sido FROM healthcare;
```
36
27
11
31
41
44
48
30
42
43
46
28
26
47
45
29
49
```
```

### 자유롭게 조합해서 원하는 데이터를 출력해보세요.

> 예) 허리 둘레가 x이상이면서 몸무게가 y이하인 사람

# 8/17

## 문제

### 1. 추가되어 있는 모든 데이터의 수를 출력하시오.

```sql
```
SELECT COUNT(*) FROM healthcare;
1000000 
```
```

### 2. 연령 코드(age)의 최대, 최소 값을 모두 출력하시오. 

```sql
```
SELECT max(age),min(age) FROM healthcare;
18,9
```
```

### 3. 신장(height)과 체중(weight)의 최대, 최소 값을 모두 출력하시오.

```sql
```
SELECT max(height),min(height),max(weight),min(weight) FROM healthcare;
195,130,135,30
```
```

### 4. 신장(height)이 160이상 170이하인 사람은 몇 명인지 출력하시오.

```sql
```
SELECT COUNT(*) FROM healthcare WHERE height>=160 and height<=170;
516930

```
```

### 5. 음주(is_drinking)를 하는 사람(1)의 허리 둘레(waist)를 높은 순으로 5명 출력하시오. 

```sql
```

```
```

### 6. 시력 양쪽(va_left, va_right)이 1.5이상이면서 음주(is_drinking)를 하는 사람의 수를 출력하시오.

```sql
```

```
```

### 7. 혈압(blood_pressure)이 정상 범위(120미만)인 사람의 수를 출력하시오.

```sql
```

```
```

### 8. 혈압(blood_pressure)이 140이상인 사람들의 평균 허리둘레(waist)를 출력하시오.

```sql
```

```
```

### 9. 성별(gender)이 1인 사람의 평균 키(height)와 평균 몸무게(weight)를 출력하시오.

```sql
```

```
```

### 10. 키가 가장 큰 사람 중에 두번째로 무거운 사람의 id와 키(height), 몸무게(weight)를 출력하시오.

```sql
```

```
```

### 11. BMI가 30이상인 사람의 수를 출력하시오. 

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
```

```
```

### 12. 흡연(smoking)이 3인 사람의 BMI지수가 제일 높은 사람 순서대로 5명의 id와 BMI를 출력하시오.

> BMI는 체중/(키*키)의 계산 결과이다. 
> 키는 미터 단위로 계산한다.

```sql
```

```
```

### 13. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
```

```
```

### 14. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
```

```
```

### 15. 자유롭게 쿼리를 작성해주시고, 결과와 함께 공유해주세요.

```sql
```

```
```

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
