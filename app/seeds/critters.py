from app.models import db, Critter, environment, SCHEMA
from sqlalchemy.sql import text
from faker import Faker
from .utils import generate_address

fake = Faker()
# fake.add_provider(person)

# Adds a demo user, you can add other users here if you want
def seed_critters():

    [street_address, city, state, zip] = generate_address()

    for i in range(5):
        new_address = Critter(
            userId=i+1,
            address=street_address,
            city=city,
            state=state,
            zipCode=zip,
        )
        db.session.add(new_address)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the critters table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_critters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.critters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM critters"))

    db.session.commit()
