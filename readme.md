# fastAPI Study
### 파이썬 가상환경 만들기
`python -m venv <venv-name>`

- 파이썬 가상환경 실행
`source  /Users/ballboy/workspace/env/venvs/myapi/bin/activate`

- 프로젝트 실행
`uvicorn main:app --reload`

- svelte template 생성
`npm create vite@latest frontend -- --template svelte`

- SQLAlchemy ORM 설치
`pip install sqlalchemy`

- alembic 설치
    - SQLAlchemy로 작성한 모델을 기반으로 데이터베이스를 관리 지원
`pip install alembic`
`alembic init migrations`
`alembic revision --autogenerate`