const sayT1 = () => {
  console.log('짱')
}

const sayKDA = () => {
  console.log('Imma popstar')
}

// 다른 파일에서 쓰려면 export 키워드로 내보내줘야한다
export { sayT1, sayKDA }

// 근데!! 일반 자바스크립트 파일에선 다음과 같이 작성해야한다.
console.log(module)
module.exports = { sayT1, sayKDA }