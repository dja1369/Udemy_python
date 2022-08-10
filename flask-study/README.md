# 목적 
## flask 복습 및 패키지 관리 툴인 Poetry 학습 

<br>

# 내용 
## poetry란 파이썬 의존성 관리툴로써 단순히 의존성만 관리하는것이 아니라 엄청 잘해주길래 학습하였음 
## 사용법도 매우 쉬웠으며 학습하는데 러닝커브가 매우 작다고 사료되며 자동으로 디펜던시를 추가해주어 
## 기존의 requirements.txt 파일을 생성하는것 보다 훨씬 편리하고 좋았음!

<br>

# 설치법 
## 나는 기본적으로 하나의 학습마다 개별적으로 가상환경을 사용했음 
## pyenv로 가상환경을 생성한 후에 
## pip install poetry로 설치를 진행하였음 
## 메뉴얼의 경우 poetry --help 를 치면 나오며 종류또한 적어 러닝커브가 매우 낮다고 생각함

<br>

# 명령어 
## 프로젝트 생성 
### 아래와 같은 구조의 프로젝트가 생성됨 
<br>

### poetry new project_name 
### my-project tree
### .
### ├── README.rst
### ├── my_project
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;│   
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── __init__.py
### ├── pyproject.toml
### └── tests
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── __init__.py
### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   └── test_my_project.py

<br>

## pyproject.toml
### 이 파일이 의존성을 관리하는 파일 >> 이 파일을 다른 의존성 파일로 변환도 가능함 
<br>

## 패키지 설치  
### poetry add Fastapi 
### 패키지가 설치되며 자동으로 의존성에 추가됨 너무 편리함!

<br>

## 업데이트 
### poetry update
### 자동으로 최신으로 업데이트됨

<br>

# 패키징 
## 중요함
<hr> 

## poetry build 
## 이 명령어를 실행하면 배포가 가능한 tarball, wheel 파일로 빌드가 가능함!!!

</hr>
<br>

# 결과
## poetry로 배포용이성 확보 및 flask 기능에 대해 리마인드 
## 앞으로 새로운 프로젝트를 진행시 poetry를 사용하면 디펜던시와 가상환경 관리가 더 편할것 같다.