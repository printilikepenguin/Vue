어떻게 해야 상태를 더 잘 관리할 수 있을까??

# State Management
상태 === 데이터
Vue 컴포넌트는 이미 반응형 상태를 관리하고 있음

상태관리의 단순성이 무너지는 시점
1. 여러 컴포넌트가 상태를 공유할 때
1. 여러 뷰가 동일한 상태에 종속되는 경우 
2. 서로 다른 뷰의 동일한 상태를 변경시켜야하는 경우

# Pinia

구성요소
1. store
  - 중앙 저장소
  - 모든 컴포넌트가 공유하는 상태, 기능등이 작성됨
2. state
  - 반응형 상태(데이터)
  - ref() === state
3. getters
  - 계산된 값
  - computed() === getters
4. actions
  - 메서드
  - function() === actions
5. plugin
  - 추가 확장 프로그램

중앙저장소 갖다쓰면 바로 참조가능

특정 컴포넌트가 중앙저장소 값을 변경하지 않도록 주의!!
필요하다면 getters나 actions으로 간접활용

중앙저장소에 없는 걸 임의로 추가할 수는 없다

```
<template>
  <div>
    <p>{{ store.count }}</p>
    <p>{{ newNumber }}</p>
    <p>{{ store.doubleCount }}</p>
    <button @click="store.increment()">버튼</button>
  </div> 
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
console.log(store.count)

const newNumber = store.count + 1

console.log(store.doubleCount)

</script>

<style scoped>

</style>
```
```
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // 상태
  const count = ref(100)
  const doubleCount = computed(() => count.value * 2)
  // 기능
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
```

---

투두 목록이 저장소에 저장될수잇도록..!!!
우선 객체배열에 접근가능한지 확인
style가이드상 id(key)로 반복 넣어줘야됨!!!

counter.js에 모양 먼저 정의
TodoList에 반복모양 정의
TodoListItem에 출력모양 정의

다시 counter에서 액션정하기

import할 때
"'import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'"
얘는 중괄호 안쓰고 다른 건 왜 쓸까요?
>>> test.js 확인해보세용

### JS 모듈 가져오기
```javascript
// 내보내는 쪽
// export { sayT1, sayKDA }
module.exports = { sayT1, sayKDA }

// 가져오는 쪽
// import { sayT1 } from './test.js'
const { sayT1 } =require('./test.js')
```

- export, import, from 문법은 ES6부터 모듈 시스템에서 지원하는 기능
  - 내가 쓰는 자바스크립트 파일들을 모듈 시스템에서  관리해야만 쓸 수 있는 문법
  - vue에서는 한번에 여러 자바스크립트 파일을 관리하므로 주석처리된 문법이 사용가능하다

utils 폴더가 있으면 import 가능
그래서 아래처럼 많이 함
```
export const sayT1 = () => {
  console.log('어쩌고')
}
```

pinia 왜 쓰는가?
- 사실 안써도 돼!!! props,emit으로 다 할수있어!!
- 컴포넌트끼리 관계가 복잡해지거나, 규모가 커졌을 때 쓰는 것
- 할아버지의 9촌 동생 손자..? 약 12촌 사이면 11번의 emit, 12번의 props가 발생해야 데이터를 전달할 수 있음
- 관리가 어렵쥬
- 전역변수처럼 써서 관리하자!

pinia
- flux 패턴을 기반으로 만들어짐
  - 용어들과 구성이 모두 flux 패턴 기반으로 만들어짐

store값을 view에서 받고... 
v-for="product in store.productList"
  :products="product"