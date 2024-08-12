# LSTM모델을 이용한 주식 예측 프로그램 웹 개발
**2022/10/18 제 1회 명지대학교 ICT융합대학 SW프로그램 개발 경진대회**
https://www.mju.ac.kr/ict/2832/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGaWN0JTJGNDIyJTJGMTkzODI4JTJGYXJ0Y2xWaWV3LmRvJTNGcGFnZSUzRDIlMjZzcmNoQ29sdW1uJTNEJTI2c3JjaFdyZCUzRCUyNmJic0NsU2VxJTNEJTI2YmJzT3BlbldyZFNlcSUzRCUyNnJnc0JnbmRlU3RyJTNEJTI2cmdzRW5kZGVTdHIlM0QlMjZpc1ZpZXdNaW5lJTNEZmFsc2UlMjZpc1ZpZXclM0R0cnVlJTI2cGFzc3dvcmQlM0QlMjY%3D</br>
**팀이름: 주식을 정통한 (장려상)**</br>
**개발인원: 최규성(팀장), 김소명, 오우준, 임수한**</br>
**프로젝트 기간 : 2022.09.01~2022.10.15**</br>

## 프로젝트 아키텍처
![Untitled](https://github.com/user-attachments/assets/f262ec69-7f03-4029-81ce-e611afbe1728)


## 프로젝트 소개
이 Django 프로젝트 사용자인증, LSTM을 활용한 주식예측 프로그램, 주식 관련 게시판기능, 스크래핑한 주식 정보를 포함한 웹 애플리케이션입니다 주요기능은 다음과 같습니다

- **주식 예측**
  - Pytorch를 활용해서 LSTM모델 구축
- **주식 관련 게시판 기능과 자유로운 댓글 작성 가능** 
  - MySql과 연동하여 주식 관련 정보 전달 및 자유로운 댓글 작성
- **주식 정보**
  - 스크래핑을 통해 정보 전달
    
## 프로젝트 목표
- 주식 예측 웹 애플리케이션 개발
  - Django와 LSTM 모델을 사용하여 사용자가 주식 예측을 할 수 있는 웹 애플리케이션을 개발합니다.

- 데이터 기반 의사 결정 지원
  - 주식 시장의 패턴을 학습하여 미래 주가를 예측하고, 사용자에게 데이터 기반의 의사 결정을 지원합니다.

- 정보 제공 및 게시판 기능
  - 주식 관련 정보와 뉴스를 제공하며, 사용자가 자유롭게 의견을 나눌 수 있는 게시판 기능을 포함합니다.

- 스마트한 투자 결정 지원
  - 이 모든 기능을 통해 주식 투자자들이 더 스마트한 결정을 내릴 수 있도록 돕는 것이 목표입니다.
## 요구사항 분석

- Django의 내장 인증 시스템을 이용하여 사용자 등록, 로그인, 로그아웃 기능을 구현합니다.
  - 사용자의 역할에 따라 접근 가능한 페이지를 제한하여 보안을 강화합니다.
  - 주식 예측 기능

- Pytorch를 사용해 LSTM 모델을 구축하여 주식 데이터를 기반으로 미래 주가를 예측합니다.
  - 사용자는 특정 주식의 과거 데이터를 입력하여 예측 결과를 확인할 수 있어야 합니다.
  - 예측 결과는 시각화하여 사용자에게 쉽게 이해할 수 있도록 제공합니다.
  - 주식 관련 정보 제공

- 사용자는 주식 관련 토론 게시판에 접근하여 글을 작성하고, 다른 사용자의 글에 댓글을 달 수 있습니다.
  - 게시판은 주식 정보와 관련된 논의뿐만 아니라 자유로운 의견 교환의 장으로 활용됩니다.
  - 댓글 기능을 통해 사용자는 서로의 의견에 피드백을 제공할 수 있습니다.

- 데이터베이스 연동
  - MySQL 데이터베이스와 연동하여 사용자 정보, 게시판 글, 댓글, 주식 예측 데이터를 저장하고 관리합니다.
  - 데이터베이스는 효율적인 데이터 처리를 위해 최적화된 쿼리를 사용합니다.
  
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

## 개선 사항
- **2022.09.20 장기 or 단기 투자 컨셉 추가**
- **2024.08.09 코드 리펙토링**
