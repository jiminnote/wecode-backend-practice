# wecode-backend-practice

위코드(Wecode) 학습 과정 중 진행한 **Django** 기초 및 클론 코딩 프로젝트들을 모아둔 저장소입니다.  
각 폴더는 독립적인 Django 프로젝트로 구성되어 있습니다.

---

## 📂 프로젝트 목록

### 1. [django-initial](./django-initial)
- Django 기본 세팅, URL, View, Model 학습
- 초기 환경 세팅 및 실습 코드

### 2. [34-1st-wesop-backend](./34-1st-wesop-backend)
- **프로젝트명:** WeSop – Aesop 클론  
- **기간:** 2022/06/20 ~ 2022/07/01 (11일)  
- **인원:** Frontend 4명, Backend 1명 (정지민)  
- **핵심 기능:**  
  - 로그인/회원가입 (비밀번호 암호화, JWT 발급)  
  - 제품 리스트 & 상세 조회 (카테고리 포함)  
  - 장바구니 (추가, 조회, 수정, 삭제)  
  - 회원정보 조회 및 수정  

### 3. [34-2nd-wescanner-backend](./34-2nd-wescanner-backend)
- **프로젝트명:**WeScanner** – Skyscanner 클론  
- **기간:** 2022/07/04 ~ 2022/07/15 (11일)  
- **인원:** Frontend 3명, Backend 1명 (정지민)  
- **적용 기술:** Django, MySQL, JWT, AWS (RDS, EC2, S3, Boto3)  
- **핵심 기능:**  
  - 이메일 로그인 / 카카오 소셜 로그인  
  - 호텔 검색 & 리스트 필터링  
  - 리뷰 업로드/삭제 (S3 연동)  
  - 위시리스트  
  - 호텔 리스트 정렬 (저가순, 고가순, 추천순)  

### 4. [django-basics-actor-movie-api](./django-basics-actor-movie-api)
- **학습용 프로젝트:** Actor–Movie 다대다 관계 모델링  
- **핵심 기능:**  
  - `/actors` → 배우와 출연 영화 목록 반환  
  - `/movies` → 영화와 출연 배우 목록 반환  

### 5. [django-basics-westagram](./django-basics-westagram)
- **프로젝트명:** Westagram (Instagram 클론)  
- **핵심 기능:**  
  - 회원가입/로그인  
  - 게시글 작성, 댓글 작성  
  - 사용자 팔로우 기능  

### 6. [django-basics-westarbucks](./django-basics-westarbucks)
- **프로젝트명:** Westarbucks (Starbucks 클론)  
- **핵심 기능:**  
  - 카테고리/메뉴/상품 조회  
  - 상품 상세 조회  

---

## 🛠 Tech Stack
- Python 3.x
- Django 4.x
- MySQL / SQLite3
- JWT Authentication
- AWS (RDS, EC2, S3)
- Git / GitHub

---

## 🚀 실행 방법

각 프로젝트 디렉토리로 이동 후:

```bash
# 가상환경 실행 (예: conda/mamba/venv)
cd django-basics-actor-movie-api

# 패키지 설치
pip install -r requirements.txt

# 마이그레이션
python manage.py migrate

# 서버 실행
python manage.py runserver
```

📌 목적
* Django 기본기 및 ORM 이해
* REST API 설계 및 구현
* 팀 프로젝트 경험 (프론트-백 협업)
* 클론 프로젝트를 통한 실전 감각 습득
