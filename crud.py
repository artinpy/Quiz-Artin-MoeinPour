from sqlalchemy.orm import Session
from models import User, Questions, Choice, Answers

def create_user(db: Session, name: str):
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_question(db: Session, text: str):
    question = Questions(text=text)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def add_choice(db: Session, question: Questions, text: str, is_correct: bool = False):
    choice = Choice(text=text, is_correct=is_correct, question=question)
    db.add(choice)
    db.commit()
    db.refresh(choice)
    return choice

def list_questions(db: Session):
    return db.query(Questions).all()

def submit_answer(db: Session, user_id: int, question_id: int, choice_id: int):
    answer = Answers(user_id=user_id, question_id=question_id, choice_id=choice_id)
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer

def calculate_score(db: Session, user_id: int):
    user_answers = db.query(Answers).filter(Answers.user_id == user_id).all()
    correct_count = 0
    for ans in user_answers:
        choice = db.query(Choice).filter(Choice.id == ans.choice_id).first()
        if choice and choice.is_correct:
            correct_count += 1
    total = len(user_answers)
    return correct_count, total

def get_unanswered_questions(db: Session, user_id: int):
    all_questions = db.query(Questions).all()
    answered_ids = [a.question_id for a in db.query(Answers).filter(Answers.user_id == user_id).all()]
    return [q for q in all_questions if q.id not in answered_ids]

def get_top_users(db: Session, n: int = 3):
    users = db.query(User).all()
    scores = []
    for u in users:
        correct, total = calculate_score(db, u.id)
        score = correct / total if total > 0 else 0
        scores.append((u.name, correct, total, score))
    scores.sort(key=lambda x: x[3], reverse=True)
    return scores[:n]

def reset_user_answers(db: Session, user_id: int):
    db.query(Answers).filter(Answers.user_id == user_id).delete()
    db.commit()

def get_choice_distribution(db: Session, user_id: int):
    choices = db.query(Choice).join(Answers).filter(Answers.user_id == user_id).all()
    dist = {}
    for c in choices:
        dist[c.text] = dist.get(c.text, 0) + 1
    return dist
