from lib.db.models import SessionLocal, User, Expense

def create_user(name, email):
    session = SessionLocal()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.close()
    return user

def create_expense(description, amount, user_id):
    session = SessionLocal()
    expense = Expense(description=description, amount=amount, user_id=user_id)
    session.add(expense)
    session.commit()
    session.close()
    return expense

def list_users():
    session = SessionLocal()
    users = session.query(User).all()
    session.close()
    return users

def list_expenses():
    session = SessionLocal()
    expenses = session.query(Expense).all()
    session.close()
    return expenses

def find_user(user_id):
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()
    session.close()
    return user

def delete_user(user_id):
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()

def delete_expense(expense_id):
    session = SessionLocal()
    expense = session.query(Expense).filter_by(id=expense_id).first()
    if expense:
        session.delete(expense)
        session.commit()
    session.close()
