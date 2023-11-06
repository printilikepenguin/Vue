Computed Property
computed()
계산된 속성을 정의하는 함수
미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복연산을 줄임

vue 객체에서 먼저 할당해줘야함
반응성 데이터를 포함하는 복잡한 로직의 경우 computed를 활용하여 미리 값을 계산

특징
- 반환되는 값은 computed ref이며 일반 refs와는 유사하게 계산된 결과를 .value로 참조할 수 있음 (템플릿에서는 .value 생략 가능)
- computed 속성은 의존된 반응형 데이터를 자동으로 추적
- 의존데이터가 변경될 때만 재평가
  - restofTodos의 계산은 todos에 의존하고 있음
  - 따라서 todos가 변경될 때만 restofTodos가 업데이트됨

computed vs methods(일반함수)
- 접근방식은 완전히 동일
- computed 속성은 의존된 반응형 데이터를 기반으로 캐시(cached)된다
- 의존하는 데이터가 변경된 경우에만 재평가됨
- 의존된 반응형 데이터가 변경되지 않는한 이전에 계산된 결과를 즉시 반환
- method 호출은 다시 렌더링이 발생할 때마다 항상 함수를 실행

Cache? 
- 데이터나 결과를 일시적으로 저장해두는 임시 저장소
- 이후 같은 데이터나 결과를 다시 계산하지 않고 빠르게 저장할 수 있게 함
- 웹에서 이미지 부를 때 많이 씀

computed의 적절한 사용처
- 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
- 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지

method의 적절한 사용처
- 단순히 특정 동작을 수행하는 함수를 정의할 때 사용



Conditional Rendering
조건에 따른 렌더링

v-if
표현식 값의 t/f

여러 요소에 대한 v-if 적용
v-if는 dirextive이기 때문에 단일 요소에만 연결 가능
이 경우 template 요소에 v-if를 사용하여 하나 이상의 요소에 대해 적용할 수 있음

HTML <template> element
보이지 않는 wrapper 역할

v-if vs v-show
공통점 : 조건부 렌더링
자주 전환해야하는 경우 v-show, 실행 중 조건 변경되지 않으면 v-if 권장

v-if (Cheap initial load, expensive toggle)
- 초기 조건이 false인 경우 아무 작업도 수행하지 않음
- 토글 비용이 높음

v-show (Expensive initial load, cheap toggle)
- 초기 조건에 관계없이 항상 렌더링
- 초기 렌더링 비용이 더 높음
표현식의 T/F 값을 기반으로 요소의 가시성visibility을 전환
항상 렌더링되어 DOM에 남아있음
CSS display 속성만 전환하기 때문



List Rendering 반복
v-for 
소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러번 렌더링 
- v-for는 alias in expression 형식의 특수 구문을 사용하여 반복되는 현재 요소에 대한 별칭을 제공
- 인덱스(객체에서는 키)에 대한 별칭을 지정할 수 있음

여러 요소에 대한 v-for 적용
template 요소에 v-for를 사용하여 하나 이상의 요소에 대해 반복 렌더링 할 수 있음

반드시 v-for와 key를 함께 사용한다
내부 컴포넌트의 상태를 일관되게 유지
데이터의 예측 가능한 행동을 유지(Vue 내부 동작 관련)
key는 반드시 각 요소에 대한 고유한 값을 나타낼 수 있는 식별자여야함

동일 요소에 v-for와 v-if를 함께 사용하지 않는다
동일 요소에서 v-if가 우선순위가 더 높음

Watchers

watch() 반응형 데이터를 감시하고, 감시하는 데이터가 변경되면 콜백 함수를 호출
watch 구조

watch는 왜 return에 안쓰나용? 템플릿에서 안쓰이고 자동호출되니까용




Lifecycle Hooks
Vue 인스턴스 생애주기 동안 특정 시점에 실행되는 함수
개발자가 특정 단계에서 의도하는 로직이 실행될 수 있도록 함

특징
- Vue는 Lifecycle Hooks에 등록된 콜백 함수들을 인스턴스와 자동으로 연결함
- 이렇게 동작하려면 hooks 함수들은 반드시 동기적어로




Vue Style 

스타일 가이드 우선순위
computed의 반환 값은 일하지 말것
computed 사용시 원본 배열 변경하지 말 것
- reverse() 및 sort() 사용 시 원본 배열을 변경하기 때문에 복사본 만들어서 진행해야 함
배열의 인덱스를 v-for의 key로 쓰지 말것

원본 배열 수정하는 수정 메서드
- Vue는 반응형 배열의 변경 메소드가 호출 되는 것을 감지하여 필요한 업데이트를 발생시킴
- push, pop shift, shie

