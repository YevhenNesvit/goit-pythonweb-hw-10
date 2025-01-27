from sqlalchemy.orm import Session
from app.repositories.contact_repo import ContactRepository
from app.schemas.contact import ContactCreate
from fastapi import HTTPException


class ContactService:
    def __init__(self):
        self.repo = ContactRepository()

    def create_contact(self, db: Session, contact: ContactCreate):
        return self.repo.create(db, contact)

    def get_all_contacts(self, db: Session):
        return self.repo.get_all(db)

    def get_contact_by_id(self, db: Session, contact_id: int):
        contact = self.repo.get_by_id(db, contact_id)
        if not contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        return contact

    def update_contact(self, db: Session, contact_id: int, contact: ContactCreate):
        return self.repo.update(db, contact_id, contact)

    def delete_contact(self, db: Session, contact_id: int):
        self.repo.delete(db, contact_id)
