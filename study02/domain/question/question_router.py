from fastapi import APIRouter

from database import SessionLocal
from models import Question

router = APIRouter(
    prefix='/api/question'
)

@router.get('/list')
def question_list():
    db = SessionLocal()
    _question_list = db.query(Question).order_by(Question.create_date.desc()).all()

    # db 세션 객체를 생성한 후에 db.close()를 수행하지 않으면 SQLAlchemy가 사용하는 커넥션 풀에 DB세션이 반환되지 않아 문제가 생긴다.
    db.close()

    return _question_list