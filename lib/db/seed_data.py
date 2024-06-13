from faker import Faker
from .models import SessionLocal, User, Expense, create_tables

def seed_data():
    fake = Faker()
    session = SessionLocal()

    try:
        # Create 10 users
        for _ in range(10):
            user = User(name=fake.name(), email=fake.email())
            session.add(user)
        
        session.commit()  # Commit after adding all users

        # Create 3 expenses for each user
        for user in session.query(User).all():
            for _ in range(3):
                expense = Expense(description=fake.catch_phrase(), amount=fake.random_number(digits=5), user_id=user.id)
                session.add(expense)
        
        session.commit()  # Commit after adding all expenses
        print("Database seeded with test data!")

    except Exception as e:
        session.rollback()  # Rollback in case of an error
        print(f"An error occurred: {e}")

    finally:
        session.close()  # Ensure the session is closed

if __name__ == "__main__":
    create_tables()
    seed_data()
