from sqlalchemy.orm import Session
from app.models.contact import Contact
from app.schemas.contact import ContactCreate


class ContactRepository:
    def create(self, db: Session, contact: ContactCreate):
        new_contact = Contact(**contact.dict())
        db.add(new_contact)
        db.commit()
        db.refresh(new_contact)
        return new_contact

    def get_all(self, db: Session):
        return db.query(Contact).all()

    def get_by_id(self, db: Session, contact_id: int):
        return db.query(Contact).filter(Contact.id == contact_id).first()

    def update(self, db: Session, contact_id: int, contact: ContactCreate):
        db_contact = self.get_by_id(db, contact_id)
        if db_contact:
            for key, value in contact.dict().items():
                setattr(db_contact, key, value)
            db.commit()
            db.refresh(db_contact)
        return db_contact

    def delete(self, db: Session, contact_id: int):
        db_contact = self.get_by_id(db, contact_id)
        if db_contact:
            db.delete(db_contact)
            db.commit()
