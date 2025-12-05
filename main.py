from database import Base, engine, SessionLocal
import models  # ensures all model classes are imported & registered

Base.metadata.create_all(engine)

session = SessionLocal()

# ... create instances, test methods, seed etc.
