from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.contact import ContactCreate, ContactRead
from app.services.contact_service import ContactService
from app.database import get_db
from app.models.contact import Contact
from typing import List, Optional

router = APIRouter(prefix="/contacts", tags=["Contacts"])
service = ContactService()


@router.get("/search", response_model=List[ContactRead])
def search_contacts(
    db: Session = Depends(get_db),
    first_name: Optional[str] = Query(None),
    last_name: Optional[str] = Query(None),
    email: Optional[str] = Query(None),
):
    # Створення базового запиту
    query = db.query(Contact)

    # Якщо є параметри, фільтруємо за ними
    if first_name:
        query = query.filter(Contact.first_name.ilike(f"%{first_name}%"))
    if last_name:
        query = query.filter(Contact.last_name.ilike(f"%{last_name}%"))
    if email:
        query = query.filter(Contact.email.ilike(f"%{email}%"))

    # Виконання запиту та повернення результатів
    contacts = query.all()
    return contacts


@router.post("/", response_model=ContactRead)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return service.create_contact(db, contact)


@router.get("/", response_model=list[ContactRead])
def list_contacts(db: Session = Depends(get_db)):
    return service.get_all_contacts(db)


@router.get("/{contact_id}", response_model=ContactRead)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    return service.get_contact_by_id(db, contact_id)


@router.put("/{contact_id}", response_model=ContactRead)
def update_contact(contact_id: int, contact: ContactCreate, db: Session = Depends(get_db)):
    return service.update_contact(db, contact_id, contact)


@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    service.delete_contact(db, contact_id)
    return {"detail": "Contact deleted"}


@router.get("/birthdays/next7", response_model=List[ContactRead])
def get_contacts_with_birthdays_next_7_days(db: Session = Depends(get_db)):
    today = datetime.today()
    next_week = today + timedelta(days=7)

    # Пошук контактів з днями народження на найближчі 7 днів
    contacts = db.query(Contact).filter(
        (Contact.birthday >= today) & (Contact.birthday <= next_week)
    ).all()

    return contacts
