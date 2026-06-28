from database import get_db
from crud import create_user, list_questions, submit_answer, calculate_score
from models import User, Questions, Choice

db = get_db()

print('==============Mini Quiz================')
name = input('Enter your name: ')
user = create_user(db, name=name)

questions = list_questions(db)
for q in questions:
    print(f'\n{q.id}. {q.text}')
    choices = q.choice
    for idx, c in enumerate(choices, start=1):
        print(f'  {idx}. {c.text}')
    
    while True:
        try:
            choice_idx = int(input('Select option number: '))
            if 1 <= choice_idx <= len(choices):
                selected_choice = choices[choice_idx - 1]
                submit_answer(db, user.id, q.id, selected_choice.id)
                break
            else:
                print('Invalid choice. Please enter a number between 1 and', len(choices))
        except ValueError:
            print('Please enter a valid number.')

correct, total = calculate_score(db, user.id)
print(f'\nQuiz finished!')
print(f'Your score: {correct}/{total} ({round(correct/total*100, 1)}%)')
