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

## 📝 APIs

![스크린샷 2024-05-02 090944](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/cee7dc25-8858-49a1-95cd-a5747cf8c03a)





<br>


## 📌 Project Result (accounts)

### 1. 로그인
   - req의 body에 json행태(key-value)로 "user_name"과 "password" 데이터를 담아 POST요청을 보낸다
   - 요청이 성공하면 결과로 refresh token과 access token이 반환된다
   - 요청에 포함된 데이터가 올바르지 않으면 "detail": "No active account found with the given credentials" 오류메시지가 반환된다

[status 200]
![스크린샷 2024-05-02 092801](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/66f53362-9b96-430c-986b-4e4cdd4b9c76)
<hr><br>

[status 401 Unauthorized]
![스크린샷 2024-05-02 092822](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/ff8253ec-665b-474c-88ff-9fb597944fb7)

<br><br>

### 2. refresh token
   - req의 body에 json행태(key-value)로 "refresh token"데이터를 담아 POST요청을 보낸다
   - 요청이 성공하면 결과로 새로운 refresh token과 access token이 반환된다
   - req로 보낸 refresh token은 블랙리스트에 추가되어 더이상의 사용이 불가능해진다

[status 200]
![스크린샷 2024-05-02 093405](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/28ab4791-130d-40e8-ac30-be192015b7a1)

<br><br>

### 3. 회원가입
   - req의 body에 json행태(key-value)로 "user_name","email","password","nickname","name","birth","gender","bio"데이터를 담아 POST요청을 보낸다
   - 요청이 성공하면 별도의 데이터는 반환되지 않고, status code 201 Created가 반환된다

[status 201 Created]
![스크린샷 2024-05-02 094101](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/fe2b4d5b-3a04-4365-b2f0-241419561f96)


<br><br>

### 4. 로그아웃
   - req의 body에 json행태(key-value)로 "refresh token"데이터를 담아 POST요청을 보낸다
   - 요청이 성공하면 "로그아웃 되었습니다"라는 message가 반환된다

[status 200]
![스크린샷 2024-05-02 094726](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/8fb5ae19-13c8-4b9c-9a29-41b806148533)


<br><br>
     
### 5. 회원정보 수정
   - req의 body에 json행태(key-value)로 "email", nickname","name","birth","gender","bio"의 수정데이터를 담아 PUT요청을 보낸다
   - 특정항목만의 수정(부분수정)도 가능하다
   - 로그인한 사용자만 사용가능하며, 자신의 회원정보만 수정할 수 있다 (->access token을 header에 담아야 함)
   - 요청이 성공하면 수정된 데이터가 반환된다
   - url의 username이 로그인된 사용자와 일치하지 않으면 "권한이 없는 사용자입니다"라는 오류메시지가 반환된다
   - 수정한 email이 다른 사용자의 이메일과 동일하면 "new user with this email address already exists"라는 오류메시지가 반환된다

[status 200]

![스크린샷 2024-05-02 095025](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/f7404f73-bd01-4821-b67c-69d01e4a99af)

<br>

[status 403 Forbidden]
![스크린샷 2024-05-02 095720](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/b221df74-5420-4e0b-ae95-2b0785eb5e96)

<br>

[status 400 Bad Request]
![스크린샷 2024-05-02 095243](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/6042a913-bee2-447d-80a0-cd55e016b800)

<br><br>

### 6. 프로필 조회
   - req의 body에 아무런 데이터없이 GET요청을 보낸다
   - 로그인한 사용자만 프로필을 조회할 수 있다 (->access token을 header에 담아야 함)
   - url부분의 username만 조정하면 나의 프로필과 타인의 프로필을 모두 조회할 수 있다
   - 요청이 성공하면 해당 프로필 데이터가 반환된다

[status 200]
![스크린샷 2024-05-02 100144](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/9a32c03c-aa5a-49a6-880b-91401252f32b)


<hr><br><br>

## 📌 Project Result (products)

### 1. products 전체 조회
   - req의 body에 아무런 데이터도 넣지않고 GET요청을 보낸다
   - 로그인하지 않아도 사용이 가능하다
   - 요청이 성공하면 db에 있는 전체 products게시물이 조회되어 반환된다

[status 200]
![스크린샷 2024-05-02 100901](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/a3071dac-d477-40d8-b85a-fddad409243f)

<br><br>

### 2. products 검색
   - req의 body에 url에 검색할 query를 붙여 GET요청을 보낸다
   - 로그인하지 않아도 사용이 가능하다
   - query로 하나의 검색어만 입력할 수도 있으나, 띄어쓰기로 여러개의 검색어를 함께 입력할 수도 있다
   - title, content, user_name(작성자)에 대한 검색이 가능하다
   - 요청이 성공하면 해당 검색어에 해당하는 게시물이 조회되어 반환된다

[status 200]
![스크린샷 2024-05-02 102418](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/3adbe11c-8484-4d90-bf88-624be7961f06)

<hr>

[status 200]

![스크린샷 2024-05-02 102255](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/7e74e403-8480-4f08-8543-6ce963cf2f96)


<br><br>

### 3. products 생성
   - req의 body에 json행태(key-value)로 "title","content","image"데이터를 담아 POST요청을 보낸다
   - 요청이 성공하면 새롭게 생성된 게시물의 데이터가 반환된다

[status 201 Created]
![스크린샷 2024-05-02 101906](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/62cec73c-8e7a-42fd-b8ae-6c30b21eddd4)

<br><br>

### 4. products 수정
   - req의 body에 json행태(key-value)로 "title","content","image" 수정 데이터를 담아 PUT요청을 보낸다
   - 로그인한 사용자만 프로필을 수정할 수 있다 (->access token을 header에 담아야 함)
   - 자신이 작성한 게시물에 대한 수정만이 가능하다
   - 타인이 작성한 게시물에 대해 수정요청을 보내면 "권한이 없는 사용자입니다"라는 오류메시지가 반환된다
   - 요청이 성공하면 수정된 게시물의 데이터가 반환된다


[stauts 200]
![스크린샷 2024-05-02 102720](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/b201848b-f0e5-419c-9058-16565530d220)

<hr>

[status 403 Forbidden]
![스크린샷 2024-05-02 102930](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/9b280f3c-e4d3-49d6-bc1f-15a8e095e61a)

<br><br>


### 5. products 삭제
   - req의 body에 아무런 데이터없이 url에 삭제할 해당 데이터의 productID를 담아 DELETE요청을 보낸다
   - 로그인한 사용자만 프로필을 삭제할 수 있다 (->access token을 header에 담아야 함)
   - 자신이 작성한 게시물에 대한 삭제만이 가능하다
   - 타인이 작성한 게시물에 대해 삭제요청을 보내면 "권한이 없는 사용자입니다"라는 오류메시지가 반환된다
   - 요청이 성공하면 status code 204 No Content가 반환된다

[status 204 No Content]
![스크린샷 2024-05-02 103243](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/d1caab03-4ab4-4749-8e71-65a25ba1ed4a)

<hr>

[status 403 Forbidden]
![스크린샷 2024-05-02 103227](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/6826742a-732d-482b-ba28-475abf0b679e)


<br>
<hr><br>

## 📄 ERD:
![ERD_sparta drf (1)](https://github.com/soyeongpark2090/sparta_drf/assets/159408752/2b162539-e30b-4584-9c17-e3c03b5ecd71)
