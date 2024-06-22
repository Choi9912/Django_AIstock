# LSTM모델을 이용한 주식 예측 프로그램 웹 개발
**2022/10/18 제 1회 명지대학교 ICT융합대학 SW프로그램 개발 경진대회**
https://www.mju.ac.kr/ict/2832/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGaWN0JTJGNDIyJTJGMTkzODI4JTJGYXJ0Y2xWaWV3LmRvJTNGcGFnZSUzRDIlMjZzcmNoQ29sdW1uJTNEJTI2c3JjaFdyZCUzRCUyNmJic0NsU2VxJTNEJTI2YmJzT3BlbldyZFNlcSUzRCUyNnJnc0JnbmRlU3RyJTNEJTI2cmdzRW5kZGVTdHIlM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZpc1ZpZXclM0R0cnVlJTI2cGFzc3dvcmQlM0QlMjY%3D


**팀이름: 주식을 정통한 (장려상)**


**개발인원: 최규성(팀장), 김소명, 오우준, 임수한**


**프로젝트 기간 : 2022.09.01~2022.10.15**
## 프로젝트 소개
이 Django 프로젝트 사용자인증, LSTM을 활용한 주식예측 프로그램, 주식 관련 게시판기능, 스크래핑한 주식 정보를 포함한 웹 애플리케이션입니다 주요기능은 다음과 같습니다
- 주식 예측
 - Pytorch를 활용해서 LSTM모델 구축
- 주식 관련 게시판 기능과 자유로운 댓글 작성 가능 
 - MySql과 연동하여 주식 관련 정보 전달 및 자유로운 댓글 작성
- 주식 정보
 - 스크래핑을 통해 정보 전달
 - 
# 파일명
- APP : 주식예측
- Acoounts : 로그인 및 회원가입
- blog : 게시판
- crawl : 크롤링
  
## Stacks
**Environment**


<img src="https://img.shields.io/badge/Pycharm-E34F26?style=for-the-badge&logo=Pycharm&logoColor=white">  <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

**Config**


 <img src="https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white"> 
 
**Development**


  <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white"> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white"> 

## 화면 구성 📺

| 메인 페이지 | 주식 예측 프로그램 |
| --- | --- |
| ![메인 페이지](https://github.com/Choi9912/Django_AIstock/assets/76863081/9a2cf9ba-a447-4963-b9fb-df2f11adda68) | ![주식 예측](https://github.com/Choi9912/Django_AIstock/assets/76863081/ff32b7f7-0aec-4000-aae3-30436017453e) |

| 로그인 및 회원가입 | 주식 정보 + 커뮤니티 |
| --- | --- |
| ![로그인 및 회원가입](https://github.com/Choi9912/Django_AIstock/assets/76863081/2f2a77c4-d2bb-4547-8ebf-cbaa6fdb4baa) | ![주식정보 + 커뮤니티](https://github.com/Choi9912/Django_AIstock/assets/76863081/2f2a77c4-d2bb-4547-8ebf-cbaa6fdb4baa) |
