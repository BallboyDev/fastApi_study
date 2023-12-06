# study02
- APIRouter를 이용해 라우트 함수를 관리
- SQLAlchemy를 이용해 데이터 베이스 제어
- 게시판 질문 목록 상세 조회 기능 개발

## 프로젝트 구조
- > main.py
    - FastAPI 프로젝트의 전체적인 환경 설정 파일
- > database.py
    - 데이터베이스와 관련된 설정
- > models.py
    - DB 모델 정의
- > domain
    - > answer
    - > question
    - > user

- main.py - FastAPI 프로젝트의 전체적인 환경 설정 파일
- database.py - 데이터 베이스와 관련된 설정
- models.py - DB 모델 정의
- domain - 
    - question
        - question_router.py - 라우터 파일
        - question_crud.py - 데이터 베이스 처리 파일
        - question_schema.py - 입출력 관리 파일
    - answer
    - user

## ORM
- 데이터 베이스의 데이터 테이블을 프로그램 객체로 만들어 관리하는 기술
```sql
insert into question(subject, content) values ('subject1', 'content1')
```
```python
question = Question(subject='subject1', content='content1')
db.add(question)
```

## SQLAlchemy ORM
`pip install sqlalchemy`

### alembic
- SQLAlchemy로 작성한 모델을 기반으로 데이터 베이스를 관리할 수 있게 도와주는 도구
- alembic 설치
`pip install alembic`
- alembic 초기화
`alembic init migrations`
- 리비전 파일 생성
`alembic revision --autogenerate`
- 리비전 파일 실행
`alembic upgrade head`
