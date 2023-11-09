Routing

라우팅: 네트워크에서 경로를 선택하는 프로세스
=> 웹 애플리케이션에서 다른 페이지간의 전환!과 경로!!를 관리하는 기술

SSR에서의 Routing
CSR/SPA에서의 Routing

만약 routing이 없다면?
- 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
- 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
  - URL이 1개이기 때문에 새로고침 시 처음 페이지로 되돌아감
  - 링크를 공유할 시 첫 페이지만 공유가능
- 브라우저의 뒤로 가기 기능을 사용할 수 없음

Vue Router
Vue 공식 라우터
설치 시 Yes하면 페이지에 Home, About 버튼이 생김

구조 변화: 
1. App.vue 코드 변화
<nav>안에 <RouterLink>가 새로 생김!
- 페이지를 다시 로드하지 않고 URL을 변경하고 URL 생성 및 관련 로직을 처리
- HTML의 a 태그를 렌더링
<RouterView>
- URL에 해당하는 컴포넌트를 표시
- 어디에나 배치하여 레이아웃에 맞출 수 있음

2. router 폴더 생성
index.js 파일 생성
- 라우팅에 관련된 정보 및 설정이 작성되는 곳
- router에 URL과 컴포넌트를 매핑
- urls.py와 유사하지 않나요...? url을 컨트롤하는 위치랍니당

3. views 폴더 생성
- RouterView 위치에 렌더링할 컴포넌트를 배치
- 기존 components 폴더와 기능적으로 다른 것은 없으며 단순 분류의 의미로 구성됨
- 일반 컴포넌트와 구분하기 위해 컴포넌트 이름을 View로 끝나도록 작성하는 것을 권장

라우팅 기본
1. index.js에 라우터 관련 설정 작성(주소, 이름, 컴포넌트)
2. RouterLink의 'to' 속성으로 index.js에서 정의한 주소 속성 값(path)을 사용

```
// index.js

const router = createRouter({
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    }
  ]
})
```
```
<!-- App.vue -->
<RouterLink to="/">Home</RouterLink>
<RouterLink to="/about">About</RouterLink>
```

Named Routes
경로에 이름을 지정하는 라우팅
1. name 속성값에 경로에 대한 이름을 지정
2. 경로에 연결하려면 RouterLink에 v-bind를 사용해 'to' prop 객체로 전달
```
<RouterLink :to="{ name: 'home' }">Home</RouterLink>
<RouterLink :to="{ about: 'about'}">About</RouterLink>
```
장점
- 하드 코딩된 URL 사용하지 않아도 됨
- 입력시 오타 방지

Dynamic route Matching with Params 동적데이터 URL로 전달(aka Variable Routing)
동적 라우팅

매개 변수를 사용한 동적 경로 매칭
- 주어진 패턴 경로를 동일한 컴포넌트에 매핑해야할 경우 활용
- 예를 들어 모든 사용자의 ID를 활용하여 프로필 페이지 url을 설계한다면?
  - 일정 패턴의 URL 작성을 반복해야함

1. 새 컴포넌트 생성
2. index.js에 컴포넌트 라우트 등록(url 연결), 매개변수는 콜론(:) 표기
3. 라우트의 매개변수는 컴포넌트에서 $route.params로 참조가능
4. Composition API 방식으로 작성하는 것 권장

Programmatic Navigation 프로그래밍 방식 네비게이션
router의 인스턴스 메서드를 사용해 RouterLink로 a태그를 만드는 것 처럼 프로그래밍으로 네비게이션 관련 작업을 수행할 수 있음

1. 다른 위치로 이동하기: router.push()
- Routerlink를 클릭했을 대 내부적으로 호출되는 메서드이므로 RouterLink를 클릭하는 것은 router.push()를 호출하는 것과 같음
- 다양하게 인자 활용 가능 공식문서 ㄲ

2. 현재 위치 바꾸기: router.replace()
- push와 달리 history stack에 새로운 항목을 push하지 않고 다른 URL로 이동 (=== 이동전 URL로 뒤로 가기 불가능)

Navigation Guard 
Vue router를 통해 특정 URL에 접근할 때 다른 URL로 redirect 하거나 취소하여 네비게이션을 보호
ex) 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함

종류 (범위에 따라 작성위치가 달라짐)
1. Globally (전역 가드)
- 애플리케이션 전역에서 동작
- index.js에서 정의
2. Per-route (라우터 가드)
- 특정 route에서만 동작
- index.js의 각 routes에 정의
3. In-component (컴포넌트 가드)
- 특정 컴포넌트 내에서만 동작
- 컴포넌트 내 script에서 정의

router.beforeEach()
다른 URL로 이동하기 직전에 실행되는 함수 Global Before Guards
구조
```
router.beforeEatch((to, from) => {
  ...
  return false
})
```
to: 이동할 URL 정보가 담긴 Route 객체
from: 현재 URL 정보가 담긴 Route 객체
선택적 반환(return) 값
  1. false
  - 현재 내비게이션 취소
  - 브라우저 URL이 변경된 경우(사용자가 수동으로 또는 뒤로 버튼으로) from 경로의 URL로 재설정
  2. Route Location
  - 경로 위치를 전달하여 다른 위치로 redirect
return이 없다면 'to' URL 루트 객체로 이동
```
router.beforeEach((to, from) => {
  const isAuthenticated = false

  if (!isAuthenticated && to.name !== 'login') {
    console.log('로그인이 필요합니다')
    return {name: 'login'}
  }
})
```

router.beforeEnter()
route에 진입했을 때만 실행되는 함수
매개변수, 쿼리값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
구조
routes 객체에서 정의 
함수의 to, from, 선택 반환 인자는 beforeEach와 동일
```
// index.js

{
  path: '/user/id',
  name: 'user',
  component: UserView,
  beforeEnter: (to, from) => {
    console.log(to)
    console.log(from)
  }
}
```

컴포넌트 가드 종류
onBeforeRouteLeave
- 현재 라우트에서 다른 라우트로 이동하기 전에 실행
- 사용자가 현재 페이지를 떠나는 동작에 대한 로직을 처리

onBeforeRouteUpdate
- 이미 렌더링된 컴포넌트가 같은 라우트 내에서 업데이트되기 전에 실행
- 라우트 업데이트 시 추가적인 로직을 처리
- 만약 userid와 같이 변경해주지 않으면 갱신되지 않음-컴포넌트가 재사용되었기 때문

Lazy Loading Routes
첫 빌드시 해당 컴포넌트를 로드하지 않고, 해당 경로를 처음으로 방문할 때만 컴포넌트를 로드하는 것
- 앱을 빌드할 때 앱의 크기에 따라 페이지 로드 시간이 길어질 수 있기 때문
  기존에 정적 가져오기 방식을 동적 가져오기 방식으로 변경하는 것과 같음