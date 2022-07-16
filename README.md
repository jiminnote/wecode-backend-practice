# Wesop Project

## 개요

#### 목적 : [Aesop](https://www.aesop.com/)을 클론 코딩하며 프론트엔드와 백엔드의 원활한 커뮤니케이션과 Django를 이용하여 가능한 Aesop 보유 기능을 구현하기위해 학습하는 것을 목표를 두고 있음.

#### 개발 기간 : 2022년 6월 20일 ~ 2022년 7월 1일(총 11)

#### 개발 인원 :

- Frontend : 서한샘, 박수연, 조예지, 홍희윤
- Backend : 정지민(https://github.com/jiminnote)

####  2차 프로젝트 발표 자료<br />
  [PDF](public/readme/wesop%20%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.pdf)
  <br />
  [Keynote](public/readme/wesop%20%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C.key)
  <br />


## 핵심 기능 Key Feature

###  우리가 목표했던 필수 기능
- 로그인,회원가입
- 카테고리
- 제품 상세
- 제품 리스트

### 목표 외의 추가 기능
- 회원정보 조회 및 수정
- 장바구니

## How To Use

- 회원가입 완료시 비밀번호 암호화
- 해당 계정으로 로그인시 access_token 응답
- 메인 페이지 :  프론트 쪽에서 구현한 캐러쉘에 제품 리스트 응답(1. 전 상품 중 랜덤으로 7개 / 2. 향수 카테고리 상품들 전부 )
- 장바구니   : 원하는 상품을 담으면 수량이 1인 상태로 저장, 카트 페이지에서 장바구니 상품 조회, 수량 변경 및 삭제 가능
- 개인정보   : 로그인 후 회원정보 페이지에서 first_name, last_name, email, password 변경가능(password변경시 재암호화)

## 기능 구현

### modeling
<img width="1053" alt="image" src="https://user-images.githubusercontent.com/95075455/176985137-a872f255-21b0-4a98-b9ab-929331cfa58c.png">


### API
<img width="1275" alt="image" src="https://user-images.githubusercontent.com/95075455/176987964-180782b8-7727-47cd-895a-4ded9b07a721.png">

#### users
- users.SignupView : 회원 가입 기능
- users.SigninView  : 로그인 기능
- users.MypageView : 회원 정보 조회 및 수정

#### products
- product.CategoryView       : 3단계에 걸친 카테고리 전체를 조회
- products.ProductDetailView : 특정 상품의 상세 정보를 조회
- products.ProductListView   : 특정 카테고리에 대한 정보 조회 & 특정 조건에 맞는 상품들 필터링

#### orders
- carts.CartView : 장바구니를 보여주거나 상품을 추가하는 기능

## Contributing

- Thanks to [Wecode](https://wecode.co.kr/)

## Reference

- [Aesop](https://www.aesop.com/)
- [unsplash.com](https://unsplash.com/)
- [dbdiagram.io](https://dbdiagram.io/home)



## Links

-  프로젝트 회고
  - [1차 프로젝트 회고록](https://velog.io/@jiminnote/Wesop1%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9A%8C%EA%B3%A0%EB%A1%9D#-1%EC%9D%B8-%EB%B0%B1%EC%97%94%EB%93%9C)

- Repository
  - [프론트엔드](https://github.com/wecode-bootcamp-korea/34-1st-Wesop-frontend)
  - [백엔드](https://github.com/wecode-bootcamp-korea/34-1st-Wesop-backend)
  
- API Documentation
  - [API Documentation](https://documenter.getpostman.com/view/21511958/UzJETek8)
  
## License

**모든 사진은 저작권이 없는 사진을 사용했습니다.**
