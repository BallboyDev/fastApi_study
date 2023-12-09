from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

# from database import SessionLocal
from database import get_db
from models import Question

router = APIRouter(
    prefix='/api/question'
)

@router.get('/list')
def question_list():
    # 기본적인 DB호출 방법
    # db = SessionLocal()
    # _question_list = db.query(Question).order_by(Question.create_date.desc()).all()

    # # db 세션 객체를 생성한 후에 db.close()를 수행하지 않으면 SQLAlchemy가 사용하는 커넥션 풀에 DB세션이 반환되지 않아 문제가 생긴다.
    # db.close()

    # 의존성 주입 / 데이터 베이스 세션의 반환의 자동화
    with get_db() as db:
        _question_list = db.query(Question).order_by(Question.create_date.desc())
    all()    

    return _question_list

@router.get('/list2')
def question_list(db: Session = Depends(get_db)):
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()
    return _question_list