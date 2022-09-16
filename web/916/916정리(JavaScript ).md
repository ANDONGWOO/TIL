# 변수

* 애플리케이션에서 값에 상징적인 이름으로 변수를 사용합니다. 
* 변수명은 식별자라고 불리며 특정 규칙을 따릅니다.

## 변수 선언

* 변수 선언은 아래3가지 방법으로 가능 

* `var x = 42` 와 같이 `var` 키워드로 변수를 선언 할 수 있습니다.

  실행 맥락에 따라 지역 및 전역 변수를 선언하는데 모두 사용

* `let y = 13 ` 와 같이 `const` 혹은 `let` 키워드로 변수를 선언할 수 있습니다.

  블록 스코프 지역 변수를 선언하는데 사용 변수스코프 참고

* 구조 분해 할당 구문을 사용하여 객체 리터럴에서 값을 풀기 위해 변수를 선언할 수 있습니다.

## 변수 할당

* 지정된 초기 값 없이 `var` 혹은 `let` 문을 사용해서 선언된 변수는 `undefined` 값을 갖습니다.
* 선언되지 않은 변수에 접근을 시도하는 경우 `ReferenceError` 예외가 발생

```javascript
var a;
console.log('a 값은 ' + a); // a 값은 undefined

console.log('b 값은 ' + b); // b 값은 undefined
var b;
// 이것은 아래의 '변수 호이스팅'을 읽기 전에는 혼란스러울 수 있음

console.log('c 값은 ' + c); // Uncaught ReferenceError: c is not defined

let x;
console.log('x 값은 ' + x); // x 값은 undefined

console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
let y;
```

*  `undefined` 를 사용하여 변수 값이 있는지 확인할 수 있습니다. 아래 코드에서 `input` 변수는 할당되지 않았고 `if` 문은 ` true` 로 평가합니다.

```javascript
var input;
if(input === undefined) {
  doThis();
} else {
  doThat();
}
```

* `undefined` 값은 불리언 맥락(context)에서 사용될 때`false` 로 동작 합니다. 

* 아래코드는 `myArray ` 요소가 `undefined` 이므로 `myFunction` 함수를 실행합니다.

  ```javascript
  var myArray = [];
  if (!myArray[0]) myFunction();
  ```

* `undefined` 값은 수치 맥락에서 사용될 때  `NaN` 으로 변환

  ```javascript
  var a;
  a + 2; // NaN으로 평가
  ```

* `null` 값을 평가할 때, 수치 맥락에서는 0으로, 불리언 맥락에서 `false` 로 동작합니다.

  ```javascript
  var n = null;
  console.log(n * 32); // 콘솔에 0 으로 로그가 남음
  ```

##  변수 스코프

* 함수의 바깥에 변수를 선언하면, 현재 문서의 다른 코드에 해당 변수를 사용할 수 있기에 `전역 변수`라고 함

* 함수 부에 변수를 선언하면, 오직 그 함수 내에서만 사용할 수 있기에 `지역 변수`라고 함

*  아래의 코드는 `5` 라는 로그가 남는데. `x` 의 스코프가 전역 맥락(혹은 코드가 함수의 일부분이라면 함수맥락)

  이기 때문입니다. `x` 의 스코프는 `if` 문 블록에 제한되지 않습니다.

  ```javascript
  if (true) {
    var x = 5;
  }
  console.log(x); // 5
  ```

* 다음 예 `let` 선언을 사용하면 바뀝니다.(ECMAScript 2015에 도입)

  ```javascript
  if (true) {
    let y = 5;
  }
  console.log(y); // ReferenceError: y is not defined
  ```

## 변수 호이스팅

*  `JavaScript` 변수의 특이한 점은 예외를 받지 않고도, 나중에 선언된 변수를 참조 할 수 있다.  이걸 호이스팅 이라고함

  ```javascript
  /**
   * Example 1
   */
  console.log(x === undefined); // true
  var x = 3;
  
  
  /**
   * Example 2
   */
  // undefined 값을 반환함.
  var myvar = "my value";
  
  (function() {
    console.log(myvar); // undefined
    var myvar = "local value";
  })();
  ```

* 위 예제는 아래 예제와 동일하게 볼 수 있습니다

  ```javascript
  /**
   * Example 1
   */
  var x;
  console.log(x === undefined); // true
  x = 3;
  
  /**
   * Example 2
   */
  var myvar = 'my value';
  
  (function() {
    var myvar;
    console.log(myvar); // undefined
    myvar = 'local value';
  })();
  ```

* 호이스팅 때문에 , 함수 내의 모든 `var` 문은 가능한 함수 상단 근처에 두는 것이 좋습니다. 이 방법은 코드를 더욱 명확하게 만들어줍니다.

* ECMAScript 2015의 `let` 과 `const` 는 변수를 블록의 상단으로 끌어올리지만 초기화하지 않습니다.변수가 선언되기 전에 블록 안에서 변수를 참조하게 되면

  `ReferenceError` 를 발생시키게 되는데, 변수는 블록 시작부터 선언이 처리될 때까지 "temporal dead zone"에 위치하게 되기 때문입니다.

  ```javascript
  console.log(x); // ReferenceError
  let x = 3;
  ```

## 함수 호이스팅

* 함수에서는 함수 선언으로 호이스팅되자만 함수 표현식으로는 호이스팅 되지 않습니다.

  ```javascript
  /* 함수 선언 */
  
  foo(); // "bar"
  
  function foo() {
    console.log('bar');
  }
  
  /* 함수 표현식 */
  
  baz(); // TypeError: baz is not a function
  
  var baz = function() {
    console.log('bar2');
  };
  ```

# 배열

* 배열은 리스트와 비슷한 객체로서 순회와 변형 작업을 수행하는 메서드를 갖습니다.
* 배열은 길이도 각 요소의 자료형도 고정 되어 있지 않습니다.
* 배열은 밀집성을 보장하지 않습니다.
* 배열은 요소 인덱스로 문자열을 사용할 수 없으며 무조건 정수만 허용

* 배열만들기

  ```javascript
  let fruits = ['사과', '바나나']
  
  console.log(fruits.length)
  // 2
  ```

* 인덱스로 배열의 항목에 접근

  ```javascript
  let first = fruits[0]
  // 사과
  
  let last = fruits[fruits.length - 1]
  // 바나나
  ```

* 배열의 항목들들 순환하며 처리하기

  ```javascript
  fruits.forEach(function (item, index, array) {
    console.log(item, index)
  })
  // 사과 0
  // 바나나 1
  ```

* 배열 끝에 항목 추가하기

  ```javascript
  let newLength = fruits.push('오렌지')
  // ["사과", "바나나", "오렌지"]
  ```

* 배열 끝에서부터  항목 제거하기

  ```javascript
  let last = fruits.pop() // 끝에있던 '오렌지'를 제거
  // ["사과", "바나나"]
  ```

* 배열 앞에서부터 항목 제거하기

  ```javascript
  let first = fruits.shift() // 제일 앞의 '사과'를 제거
  // ["바나나"]
  ```

* 배열 앞에 항목 추가하기

  ```javascript
  let newLength = fruits.unshift('딸기') // 앞에 추가
  // ["딸기", "바나나"]
  ```

* 배열 안 항목의 인덱스 찾기

  ```javascript
  fruits.push('망고')
  // ["딸기", "바나나", "망고"]
  
  let pos = fruits.indexOf("바나나")
  // 1
  ```

* 인덱스 위치에 있는 항목 제거하기

  ```javascript
  let removedItem = fruits.splice(pos, 1) // 항목을 제거하는 방법
  
  // ["딸기", "망고"]
  ```

* 인덱스 위치에서부터 여러개의 항목 제거하기

  ```javascript
  let vegetables = ['양배추', '순무', '무', '당근']
  console.log(vegetables)
  // ["양배추", "순무", "무", "당근"]
  
  let pos = 1
  let n = 2
  
  let removedItems = vegetables.splice(pos, n)
  // 배열에서 항목을 제거하는 방법
  // pos 인덱스부터 n개의 항목을 제거함
  
  console.log(vegetables)
  // ["양배추", "당근"] (원 배열 vegetables의 값이 변함)
  
  console.log(removedItems)
  // ["순무", "무"]
  ```

* 배열 복사하기

  ```javascript
  let shallowCopySpread = [...fruits]
  // ["딸기", "망고"]
  ```

## 배열 요소에 접근하기

* 배열의 인덱스는 0부터 시작 배열의 첫 번째 요소의 인덱스는 0 마지막 요소는 `length`속성에서 1을 뺀 것과 같습니다.

* 잘못된 인덱스를 사용하면 `undefined` 를 반환 합니다

  ```javascript
  let arr = ['첫 번재 요소입니다', '두 번째 요소입니다', '마지막 요소입니다']
  console.log(arr[0])              // '첫 번재 요소입니다'를 기록
  console.log(arr[1])              // '두 번재 요소입니다'를 기록
  console.log(arr[arr.length - 1]) // '마지막 요소입니다'를 기록
  ```

## 배열 길이와 숫자형 속성의 관계

* 배열의 `length` 속성과 숫자형 속성은 연결되어 있습니다

* 배열 내장 메서드(`join` ,`slice`, `indexOf` 등 )은 호출했을 때 배열의  `length` 속성의 값을 참고

* 다른 메서드(`push`,`splice` 등)또한 배열의 `length` 속성을 바꾸는 결과를 낳습니다.

  ```javascript
  const fruits = []
  fruits.push('바나나', '사과', '복숭아')
  
  console.log(fruits.length) // 3
  ```

* 배열 인덱스로 유효한 속성을  `JavaScript` 배열에 설정 할 때, 그인덱스가 현제 배열의 경계 바깥에 있는 경우, 배열의  `length` 속성을 그에 맞춰 업데이트함

  ```javascript
  fruits[5] = 'mango'
  console.log(fruits[5])           // '망고'
  console.log(Object.keys(fruits)) // ['0', '1', '2', '5']
  console.log(fruits.length)       // 6
  ```

* `length` 를 직접 늘려도 요소에 변화는 없습니다.

  ```javascript
  fruits.length = 10
  console.log(fruits)              // ['바나나', '사과', '복숭아', 비어 있음 x 2, '망고', 비어 있음 x 4]
  console.log(Object.keys(fruits)) // ['0', '1', '2', '5']
  console.log(fruits.length)       // 10
  console.log(fruits[8])           // undefined
  ```

* `length` 속성을 감소시키면 요소가 지워집니다.

  ```javascript
  fruits.length = 2
  console.log(Object.keys(fruits)) // ['0', '1']
  console.log(fruits.length)       // 2
  ```

# 객체

* 객체는 관련된 데이터와 함수의 집합

* 객체를 생성하는 것은 변수를 정의하고 초기화하는 것으로 시작합니다

  ```javascript
  var person = {};
  ```

# JSON(JavaScript Object Notation )

* JSON(JavaScript Object Notation )은 `Javascript` 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의 표준 포맷입니다.
* JSON은 문자열 형태로 존재

## JSON 구조

* JSON 안에는 Javascript의 기본 데이터 타입인 문자열, 숫자, 배열, 불리언 그리고 다른 객체를 포함할 수 있습니다.

* 데이터 계층 구축가능

  ```javascript
  {
    "squadName": "Super hero squad",
    "homeTown": "Metro City",
    "formed": 2016,
    "secretBase": "Super tower",
    "active": true,
    "members": [
      {
        "name": "Molecule Man",
        "age": 29,
        "secretIdentity": "Dan Jukes",
        "powers": [
          "Radiation resistance",
          "Turning tiny",
          "Radiation blast"
        ]
      },
      {
        "name": "Madame Uppercut",
        "age": 39,
        "secretIdentity": "Jane Wilson",
        "powers": [
          "Million tonne punch",
          "Damage resistance",
          "Superhuman reflexes"
        ]
      },
      {
        "name": "Eternal Flame",
        "age": 1000000,
        "secretIdentity": "Unknown",
        "powers": [
          "Immortality",
          "Heat Immunity",
          "Inferno",
          "Teleportation",
          "Interdimensional travel"
        ]
      }
    ]
  }
  ```

  



