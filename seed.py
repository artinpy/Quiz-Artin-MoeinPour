from database import Base, engine, get_db
from crud import create_user, create_question, add_choice, list_questions

Base.metadata.create_all(engine)
db = get_db()

q1 = create_question(db, text='2 * 2 = ?')
add_choice(db, q1, text='4', is_correct=True)
add_choice(db, q1, text='2', is_correct=False)
add_choice(db, q1, text='6', is_correct=False)

q2 = create_question(db, text='80 - 10 = ?')
add_choice(db, q2, text='70', is_correct=True)
add_choice(db, q2, text='90', is_correct=False)
add_choice(db, q2, text='75', is_correct=False)

q3 = create_question(db, text='what is the name of the language used in this quiz?')
add_choice(db, q3, text='php', is_correct=False)
add_choice(db, q3, text='python', is_correct=True)
add_choice(db, q3, text='javascript', is_correct=False)

q4 = create_question(db, text='40 / 2 = ?')
add_choice(db, q4, text='20', is_correct=True)
add_choice(db, q4, text='10', is_correct=False)
add_choice(db, q4, text='30', is_correct=False)

print('Seed data created successfully.')
