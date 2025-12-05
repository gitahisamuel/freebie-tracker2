from database import init_db, SessionLocal
from models import Company, Dev, Freebie

def seed_data(session):
    # create some test companies and devs
    c1 = Company(name="HackCorp", founding_year=2010)
    c2 = Company(name="DevGoods", founding_year=2005)
    d1 = Dev(name="Alice")
    d2 = Dev(name="Bob")
    session.add_all([c1, c2, d1, d2])
    session.commit()

    # give freebies
    fb1 = c1.give_freebie(d1, "Sticker Pack", 0, session)
    fb2 = c2.give_freebie(d1, "T-Shirt", 20, session)
    fb3 = c2.give_freebie(d2, "Mug", 10, session)

    print(fb1.print_details())
    print(fb2.print_details())
    print(fb3.print_details())

    # test received_one
    print(d1.received_one("T-Shirt"))  # True
    print(d2.received_one("T-Shirt"))  # False

    # transfer
    d1.give_away(d2, fb2, session)
    print(fb2.print_details())

    # oldest company
    old = Company.oldest_company(session)
    print("Oldest company:", old.name)

if __name__ == "__main__":
    init_db()
    session = SessionLocal()
    seed_data(session)
