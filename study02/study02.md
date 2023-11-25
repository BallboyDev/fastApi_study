### 프로젝트 구조
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
- > frontend

### sqlalcehmy 
```py
from models import Question, Answer
from datetime import datetime
from database import SessionLocal

# add Question
questions = [
    Question(
        subject='first question subject',
        content='first question content',
        create_date=datetime.now()
    ), 
    Question(
        subject='second question subject',
        content='second question content',
        create_date=datetime.now()
    )
]

db = SessionLocal()

for q in questions:
    print(q)
    db.add(q)
    db.commit() # db.rollback()
    
# add Answer
q = db.query(Question).get(2)
a = Answer(question = q, content='answer of second question', create_date=datetime.now())
db.add(a)
db.commit()

```

- 데이터 조회하기
```py
from database import SessionLocal
db = SessionLocal()

# 데이터 조회하기
db.query(Question).all()
# pk 값을 이용한 조회
db.query(Question).get(1)
# filter 조회
db.query(Quetsion).filter(Question.subject.like('%pybo%')).all()

# 데이터 수정하기
q = db.query(Question).get(1)
q.subject = 'what is pybo update'
db.commti()

# 데이터 삭제하기
q = db.query(Question).get(1)
db.delete(q)
db.commit()
```