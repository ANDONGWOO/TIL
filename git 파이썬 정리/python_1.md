# 파이썬 

* 문법이 간단하면 문법이 간결하다

* 객체 지향 프로그래밍
  * 객체-물체

## 기초문법

* 코드 스타일 가이드 (pep8)

* 들여쓰기 4칸

* 변수는 객체를 참조하기 위해 사용되는 이름

* 변수는 할당 연산자를 통해 값을 할당

  `x=1`
```
x, y  = 10 , 20
tmp = x
x = y
y = tmp
print(x, y)
```
```
y, x = x, y
print(x, y)
```

* 주석 

  한줄을 온전히 사용 할수도있고 그줄 코드 뒷부분에 작성 할 수있음

* `#  주석입니디`

기본)

- 코드는 위에서 부터 아래로 실행함
- 오른쪽에서 왼쪽으로

# 기본 자료형

* 불린형

  true(1)/false(0)

* 수치형

* 문자열

* NONE 

  값이 없음



논리 연산자

* 논리식 판단하여 참와 거짓 를 반화함

  | 연산자  | 내용                          |
  | ------- | ----------------------------- |
  | A and B | A와 B 모두 true시,true        |
  | A or B  | A와 B 모두 false시,false      |
  | Not     | true를 false로 false를 true로 |

* and : 모두 참인 경우 참, 그렇지 않으면 거짓

  | 논리연산자 and  | 내용  |
  | --------------- | ----- |
  | true and true   | true  |
  | true and false  | false |
  | false and true  | false |
  | false and false | false |

* or: 둘 중 하나만 참이라도 참 그렇지 않으면 거짓

| 논리연산자 or  | 내용  |
| -------------- | ----- |
| true or true   | true  |
| true or false  | true  |
| false or true  | true  |
| false or false | false |

* not:  참 거짓의 반대의결과

  

| 논리연산자 not | 내용  |
| -------------- | ----- |
| not true       | false |
| not false      | true  |

  

## 수치형

모든 정수의 타입 int



정수가 아닌 모든실수는 float



부동소수점



## 문자열

모든 문자는 str타입


```

print('문자열')

print("문자열")

```

중첩따옴표

```
print("중'첩따옴'표")

print('중"첩따옴"표')
```

삼중따옴표

print('''삼중따옴표'삼중따옴표'삼중따옴표"삼중따옴표"삼중따옴표삼중따옴표''')

기타 

* 결합

* 반복

* 포함

  

## 자료형 변환

* 암시적 변환
  자동으로 
* 명시적 변환
  수동으로

​     형식에 맞는 문자열만 가능



타입값 
숫자 int float complex
boolean true false
none

시퀀스(순서o)

컬렉션/비시퀀스(순서x)

## 리스트

변경가능한 갑들의 나열된 자료형

순서를 가지며 반복 가능



.append() 추가

.pep()삭제



## 튜플

변경 불가능 반복 가능

소괄호 형태로 정의

(1,2,3,)

## 레인지

변경 불가 반복 가능

range(4)

range(0, 4)

list(range(4)) 

[0, 1, 2, 3,]

## 세트

* 순서가 없고 중복된 값이 없음

* 변경 가능 반복가능

* .add()추가

* .remove()삭제

## 딕셔너리

키 값 쌍으로 이뤄진 모음

* 키 불변 자료형만가능

* 값 어떠한 형배든 관계없음

  키와 값 :으로 구분 개별 요소는 ,로 구분

* 변경 가능 반복 가능

키 값 추가 및 변경 

* 키가 있다면 값이 변경

키 삭제 .pop()

키 없는경우 KeyError 발생



  

