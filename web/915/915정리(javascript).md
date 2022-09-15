# JavaScript

* 유형 및 연산자, 표준 내장 객체 및 메서드가 있는 다중 패러다임, 동적 언어입니다.
* 구문은 java 및 c언어를 기반으로 합니다
* 객체 지향 프로그래밍을 지원, 함수형 프로그래밍도 지원

## 데이터 타입

* 수(Number)
* Biglnt
* 문자열(String)
* 부울(Boolean)
* 기호(Symbol)
* 객체(Object)
  * 함수(Function)
  * 배열(Array)
  * 날짜(Date)
  * 정규식(RegExp)

* 널(Null)
* 정의되지 않음(Undefined)

## 변수

* JavaScript에서 새로운 변수는 `let`,`const`,`var` 키워드로 선언됩니다.

### let

* `let` 을 사용하면 블록 레벨 변수를 선언할 수 있습니다. 선언된 변수는 "변수가 선언된 블록"에서 사용

  ```javascript
  let a
  let name = 'Simon'
  ```

* `let` 으로  선언한 변수의 범위

  ```javascript
  //a는사용 불가능
  
  for (let a=0 a<5 a++){
      //a는 사용 가능
  }
  //a는사용 불가능
  ```

### const

* `const` 값이 변경 불가능한 변수를 선언 할 수 있고, 변수는 "변수가 선언된 블록"에서 사용

### var

* `var` 키워드는 `let` ,`const` 키워드가 가지는 제한을 가지지 않습니다.이는 JavaScript에서 변수를 선언하는

  유일한 방법, `var` 키워드로 선언된 변수는 "변수가 선언된 함수"에서 사용

  ```javascript
  var a
  var name = 'Simon'
  ```

  `var` 로  선언한 변수의 범위

  ```javascript
  //a는사용 가능
  
  for (let a=0 a<5 a++){
      //a는 함수전체 사용 가능
  }
  //a는사용 가능
  ```

* 변수에 값을 지정하지 않고 변수를 선언하면, 타입은 `Undefined` 로 지정

## 연산자

* 산술연산자로는 `+` ,`-`, ` *`, `/`, `%`(나머지 연산자)가 있습니다.값은 `=` 연산자로 할 수 있고

* `+=`와`-=` 와 같은 복합 할당 연산자를 통해서도 할당 할 수 있습니다

  ```javascript
  x +=5
  x = x+5
  ```

* `++` 와 `--` 를 각 증가와 감소에 사용, 이들은 또한 전처리와 후처리 연산자로 사용

* `+` 연산자는 문자열을 잇기도 합니다

  ```javascript
  'hello'+'world' //"hello world"
  ```


* 문자열에 어떤 수(또는 다른 값)를 더하면 모두 문자열로 바뀌게 됩니다.

  ```javascript
  '3' + 4 + 5 // "345" 
   3 + 4 + '5' // "75" 수(3)+수(4)+문자열(5) "75"
  ```

* 비교연산자는 `<` ,`>` ,`<=` ,`>=` 를 통해 가능, 이 연산자들은 문자열과 수 양쪽 모두에서 동작

* 이중 동호(`==`) 연산자는 서로 다른 타입을 비교 할 경우, `타입 강제 변환`을 수행 

  ```javascript
  123 == '123' // true
  1 == true // true
  ```

* 타입 강제 변환을 하지 않게 하려면, 삼중 등호 연산자(`===`)를 사용

  ```javascript
  123 === '123' // false
  1 === true // false
  ```

* 이와 비슷하게 `!=`와`!==` 연산자가 있습니다.

    

## 제어구조(조건문,반복문)

* 조건문 `if` 와`else` 지원

  ```javascript
  var name = 'kittens'
  if (name === 'puppies'){
      name += 'woof'
  } else if (){
      name += 'meow'
  } else{
      name += '!'
  }
  name === 'kittens meow'
  ```

* 반복문 `while`,`do-while` 지원

  ```javascript
  while(true){
      //무한 루프
  }
  var input
  do{
      input = get_input()
      
  }while(inputIsNotValid(input))
  ```

* 반복문 for은 반복문에 필요한 제어 정보를 한 줄에 표현 가능

  ```javascript
  for (var i=0 i<5 i++){
      //내부 동작 5번 반복
  }
  
* 두개의 중요한 `for` 반복문 또한 포함 1.`for ...of`
  
  ```javascript
  for (let value of array) {
    // value로 작업 실행
  }
  ```
  
* 2.`for...in`

  ```javascript
  for (let property in object) {
    // object의 항목(property)으로 작업을 실행합니다
  }
  ```

* `switch` 문은 숫자나 문자열을 기반으로 다중 분기되는 문장을 작성하는데 사용

  ```javascript
  switch (action) {
    case 'draw':
      drawIt();
      break;
    case 'eat':
      eatIt();
      break;
    default:
      doNothing();
  }
  ```

## 함수

* 함수는 JavaScript를 이해하는데 핵심이되는 컴포넌트

  ```javascript
  function add(x, y) {
      const total = x + y;
      return total;
  }
  ```

* 예시는 기본 함수를 보여주고 있습니다.함수는 0개 이상의 이름이 있는 매개변수를 가질 수 있습니다.

* `return` 문은 어느 시점이든 값을 반환하고 함수를 종료, 리턴문이 없으면(혹은 값이 없는 리턴이 사용되면)

   `Undefined` 을 반환

* 이름을 가진 매개변수들은 다른 어떤 것보다도 해당 함수가 어떤함수인지 잘 설명해줄 수 있습니다. 해당 함수가 원하는 매개변수를 전달하지 않고 함수를 호출할 수 있지만 그럴 경우 해당 변수들은 `Undefined` 로 설정

  ```javascript
  add(); // NaN
  // undefined 값으로 대해 덧셈을 수행할 수 없습니다
  ```

* 함수가 기대하는 매개변수보다 많은 매개변수를 넘겨 줄 수도 있습니다

  ```javascript
  add(2, 3, 4); // 5
  // 처음의 두 수가 더해집니다. 4는 무시됨
  ```

* 함수는 추가적으로  전달한 매개변수를 함수 내부에서 접근 할 수 있습니다.`arguments` 라는 객체는 매개변수로 전달한 모든 값을 가지고 있는 배열과 비숫한 객체입니다.값을 처리하는 add 함수로 다시 작성함

  ```javascript
  function add() {
    let sum = 0;
    for (const item of arguments) {
      sum += item;
    }
    return sum;
  }
  
  add(2, 3, 4, 5); // 14
  ```

* 평균을 계산하는 함수를 만들어 보겠습니다.

  ```javascript
  function avg() {
    let sum = 0;
    for (const item of arguments) {
      sum += item;
    }
    return sum / arguments.length;
  }
  
  avg(2, 3, 4, 5); // 3.5
  ```

