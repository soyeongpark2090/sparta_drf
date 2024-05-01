# 👩‍💻Project: Sparta Market_drf
#### 내일배움캠프 AI 6기: DRF를 활용해서 Sparta Market을 RESTful API로 만들어본 개인과제

<br>

## 👨‍🏫 Project Introduction
DJANGO(DRF)를 백엔드 개발에만 사용해서 RESTful API를 구현

<br>

## ⏲️ Development time
- 2024.04.26(금) ~ 2023.05.02(목)


<br>

## 💻 Development Environment
- **Programming Language** : Python 3.10
- **Web Framework** : DRF
- **Database** : SQLite (for development and testing)
- **IDE** : Visual Studio Code
- **Version Control** : Git, GitHub
  
<br>

## 📝 API

![스크린샷 2024-05-02 024656](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/db7379d5-19d6-48a2-a590-23cb5de97a11)



<br>


## ⭐ Key Features

### 1. Auth
   - 회원가입, 로그인, 로그아웃, 회원정보 수정, 회원탈퇴 기능
   - 로그인이 된 사용자에게는 '로그아웃','회원정보 수정', '회원탈퇴'버튼이 노출되며, 그렇지 않은 경우에는 '로그인'버튼과 '회원가입'버튼이 노출된다

### 2. Product_Post CRUD
  - 사용자가 판매하려는 항목에 대한 게시물(이미지 포함)을 작성, 읽기, 업데이트 및 삭제할 수 있다.
  - 자신이 작성한 게시글에 한해서만 수정 및 삭제가 가능하며, 게시글의 작성자에게만 게시글 상세 조회 페이지에서 '수정'과 '삭제'버튼이 보여진다
  - 게시물은 메인페이지, 전체 게시물 목록 페이지에서 보실 수 있으며, 비회원도 볼 수 있다.
  - 카드 링크를 클릭하면 세부 항목 페이지로 이동할 수 있다.
  - 모든 페이지에서는 navbar의 "SPARTA MARKET"을 클릭하면 메인페이지인 전체 게시글 목록 페이지로 이동할 수 있다.


### 3. Comment CRD
   - 물품의 상세 페이지 하단에서 게시글에 대한 댓글을 작성,수정,삭제할 수 있다.
   - 댓글의 작성자에 한해 수정,삭제가 가능하며, 자신이 작성한 댓글에 대해서만 수정버튼과 삭제버튼이 보여진다
     
### 4. LIKE
   - 사용자들은 다른 유저들이 작성한 게시글에 LIKE(찜)를 누를 수 있다
   - 메인페이지인 전체 게시물 목록에 있는 카드 내에 있는 하트표시를 눌러서 찜(LIKE)을 할 수도, 찜을 해제할 수도 있다
     
### 5. Profile Page & Follow
   - 게시물의 상세 페이지에 있는 작성자를 클릭하면, 작성자의 프로필 페이지로 이동할 수 있다
   - 각 유저의 프로필 페이지에는 그가 작성한 게시글 목록과 LIKE를 누른 게시글의 목록을 볼 수 있고, 하이퍼링크를 통해 해당 게시글 페이지로 바로 이동할 수 있다
   - 프로필 페이지 상단에는 해당 유저에 대한 Follow버튼이 있으며, 버튼을 눌러서 팔로우할 수도 있고, 언팔로우 할 수도 있다
   - Follow버튼 하단에는 해당 유저의 팔로잉과 팔로워 수가 표시된다

<hr>



## 📄 ERD:

