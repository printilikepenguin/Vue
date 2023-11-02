Basic Syntax

Template Syntax
DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로(Vue Instance와 DOM을 연결) 바인딩할 수 있는 HTML 기반 템플릿 구문(확장된 문법 제공)을 사용

종류
1. Text Interpolation
  <p>message: {{ msg }}</p>
- 데이터 바인딩의 가장 기본적인 형태
- 이중 중괄호 구문(콧수염 구문)을 사용
- 콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
- msg 속성이 변경될 때마다 업데이트 됨

2. Raw HTML
  <div v-html="rawHtml"></div>
  const rawHtml = ref('<span style="color:red">This should be red.</span>')
- 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야함
- 잘 안씀

3. Attribute Bindings
  <div v-bind:id="dynamicId"></div>
  const dynamicId = ref('my-id')
- 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 v-bind를 사용
- HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함
- 바인딩 값이 null이나 undefind인 경우 렌더링 요소에서 제거됨

4. JavaScript Expressions
  <div>{{ number + 1 }}</div>
  <div>{{ ok ? 'YES' : 'NO' }}</div>
  <div>{{ msg.split('').reverse().join('') }}</div>
  <div v-bind:id="`list-${id}`"></div>
- Vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
- Vue 템플릿에서 JavaScript 표현식을 사용할 수 있는 위치
  - 콧수염 구문 내부
  - 모든 directive의 속성값 (v-로 시작하는 특수 속성)
- 주의사항
  - 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
  - 표현식은 값으로 평가할 수 있는 코드조각(return 뒤에 사용가능한 코드여야함)
  - 작동하지 않는 경우
    {{ const number = 1 }} 표현식이 아닌 선언식
    {{ if (ok) {return message} }} 흐름제어도 X. 삼항 표현식 사용

Directive
'v-' 접두사가 있는 특수 속성
- 속성값은 단일 JavaScript 표현식이어야 함 (v-for, v-on 제외)
- 표현식 값이 변경될 때 DOM에 반응적으로 업데이트 적용
- 예시) v-if는 seen 표현식 값의 T/F를 기반으로 <p> 요소를 제거/삽입
  <p v-if="seen">Hi There</p>

전체구문
v-on: submig .prevent ="onSubmit"
이름: 인자    .modifiers = Value

인자(Arguments)
- 일부 directive는 directive 뒤에 콜론(:)으로 표시되는 인자를 사용할 수 있음
- 아래 예시 href는 HTML a요소의 href 속성값을 myUrl 값에 바인딩 하도록 하는 v-bind의 인자
  <a v-bind:href="myUrl">Link</a>
- 아래 예시 click은 이벤트 수신할 이벤트 이름을 작성하는 v-on 인자
  <button v-on:click="doSomething">BUTTON</button>

수식어(Modifiers)
- .(dot)로 표시되는 특수 접미사로, 디렉티브가 특별한 방식으로 바인딩되어야 함을 나타냄
- 아례 예시 .prevent는 발생한 이벤트에서 event.preventDefault()를 호출하도록 v-on에 지시하는 modifier
  <form @submit.prevent="onSubmit">...</form>
https://ko.vuejs.org/api/built-in-directives.html#v-text

preventDefault




Dynamically data binding
v-bind 하나이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩(=동기화)

사용처
1. Attribute Bindings
- HTML의 속성값을 Vue의 상태속성값과 동기화 되도록 함
- v-bind shorthand(약어) : ':'(콜론)
    <img v-bind:src="imageSrc">
    <img :src="imageSrc">
    <a v-bind:href="myUrl">Move to url</a>
    <a :href="myUrl">Move to url</a>
- 동적 인자 이름(Dynamic attribute name)
  - 대괄호로 감싸서 directive argument에 JavaScript 표현식을 사용할 수도 있음
  - JavaScript 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨
  <p :[dynamicattr]="dynamicValue">.....</p>
  카멜케이스 X, 괄호안은 소문자


2. Class and Style Bindings
- 클래스와 스타일은 모두 속성이므로 다른 속성과 마찬가지로 동적으로 문자열 값을 할당할 수 있음
- 단순 문자열 연결을 사용하여 값을 생성하는 것은 번거롭고 오류발생이 쉬움
- 객체나 배열을 활용한 개선 사항 제공

  가능한 경우
  1. Binding HTML Classes
  1-1. Binding to Objects 
  <div :class="{ active: isActive}">Text</div>
  const isActive = ref(false)
  객체를 :class에 전달하여 클래스를 동적으로 전환할 수 있음

      <div class="static" :class="{active:isActive, 'text-primary': hasInfo}">Text</div>
          const isActive = ref(false)
          const hasInfo = ref(true)
  객체에 더 많은 필드를 포함하여 여러 클래스를 전환할 수 있음

          const isActive = ref(true)
        const hasInfo = ref(true)
        const classObj = ref({
          active: isActive, 
          'text-primary': hasInfo
        })
      <div class="static" :class="classObj">Text</div>
  반드시 inline 방식으로 작성하지 않아도 됨

  1-2. Bindings to Arrays
  ':class'를 배열에 바인딩하여 클래스 목록을 적용할 수 있음
  배열 구문 내에서 객체 구문 사용

  2. Binding Inline Styels
  2-1. Binding to Objects
  ':sytle'은 JavaScript 객체 값에 대한 바인딩을 지원
  실제 CSS에서 사용하는 것처럼 :style은 kebab-cased 키문자열도 지원(단, camelCase 작성 권장)
  템플릿 더 깔끔히 작성하려면 스타일 객체에 직접 바인딩하는 것을 권장
  2-2. Binding to Arrays
  여러 스타일 객체의 배열에 :style을 바인딩할 수 있음
  작성한 객체는 병합되어 동일한 요소에 적용




Evnet Handling
v-on DOM 요소에 이벤트 리스너를 연결 및 수신
v-on:event="handler"
handler 종류
1. Inline handlers: 이벤트가 트리거될 때 실행 될 JavaScript 코드
2. Method handlers: 컴포넌트에 정의된 메서드 이름
v-on 약어: '@'
@event="handler"

1. Inline handlers: 주로 간단한 상황에 사용
2. Method Handlers: 인라인으로는 불가능한 대부분의 상황에서 사용, 이를 트리거하는 기본 DOM Event 객체를 자동으로 수신

Inline Handlers에서의 메서드 호출
메서드 이름에 직접 바인딩하는 대신 Inline Handlers에서 메서드를 호출할 수도 있음
이렇게 하면 기본 이벤트 대신 사용자 지정 인자를 전달할 수 있음

Inline Handlers에서의 event 인자에 접근하기
Inline handlers에서 원래 DOM 이벤트에 접근하기
$event 변수를 사용하여 메서드에 전달  

Event Modifiers
Vue는 v-on에 대한 Event Modifiers를 제공해 event.preventDefault()와 같은 구문을 메서드에서 작성하지 않도록 함
stop, prevent, self등 다양한 modifiers를 제공
메서드는 DOM 이벤트에 대한 처리보다는 데이터에 관한 논리를 작성하는 것에 집중할 것
Modifiers는 chained 되게끔 작성할 수 있으며 이때는 작성된 순서로 실행되므로 순서 유의

Key Modifiers
Vue는 키보드 이벤트를 수신할 때 특정 키에 관한 별도 modifiers를 사용할 수 있음
key가 Enter일 때만 onSubmit 이벤트를 호출하기




Form Input Bindings
form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JavaScript 상태에 동기화해야하는 경우(양방향 바인딩)

방법1. v-bind와 v-on 함께 사용
2. v-model 사용

v-model
form input 요소 또는 컴포넌트에서 양방향 바인딩을 만듦
v-model을 사용하여 사용자 입력 데이터와 반응형 변수를 실시간 동기화
- IME가 필요한 언어(ko,cn,jp 등)의 경우 v-model이 ㅔㅈ대로 업데이트 되지 않음
- 해당 언어에 대해 올바르게 응답하려면 v-bind와 v-on 방법을 사용

v-model 활용
v-model은 단순 text input 뿐만 아니라 Checkbox, Radio, Select 등 다양한 타입의 사용자 입력 방식과 함께 사용 가능

Checkbox 활용
1. 단일 체크박스와 boolean값 활용
2. 여러 체크박스와 배열 활용
- 해당 배열에는 현재 선택된 체크박스의 값이 포함됨

Select 활용
select에서 v-model 표현식의 초기 값이 어떤 옵션과도 일치하지 않는 select 요소는 선택되지않은(unselected) 상태로 렌더링됨


* IME(Input Method Editor)
사용자가 입력장치에서 기본적으로 사용할 수 없는 문자(비영어권 언어)를 입력할 수 있도록 하는 운영 체제 구성 프로그램
일반적으로 키보드 키보다 자모가 더 많은 언어에서 사용해야 함
IME가 동작하는 방식과 Vue의 양방향 바인딩 동작방식이 상충하기 때문에 한국어 입력시 예상대로 동작하지 않았던 것




##### v-if는 이벤트를 발생시키지 못해서 호출ㅇ르시켜주야함
https://ko.vuejs.org/api/built-in-directives.html#v-if

버블링
https://ko.javascript.info/bubbling-and-capturing

버츄얼 돔
https://jeong-pro.tistory.com/210