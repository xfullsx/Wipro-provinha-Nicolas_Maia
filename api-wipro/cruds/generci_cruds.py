from sqlalchemy.orm import Session


def get_by_id(db: Session, model, model_id: int):
    try:
        return db.query(model).filter(model.id == model_id).first()
    except Exception as e:
        print(e)
        return False


def get_list_model(db: Session, model, skip: int = 0, limit: int = 100):
    try:
        return db.query(model).offset(skip).limit(limit).all()
    except Exception as e:
        print(e)
        return []


def create_model(db: Session, model, schema):
    try:
        db_model = model(**schema)
        db.add(db_model)
        db.commit()
        db.refresh(db_model)
        db.close()
        return db_model
    except Exception as e:
        print(e)
        return False


def update_model(db: Session, model, model_id, values):
    db_model = get_by_id(db, model, model_id)
    if db_model:
        db.query(model).filter(model.id == model_id).update(values)
        db.commit()
        db.refresh(db_model)
        db.close()
        return db_model
    return False


def delete_model(db: Session, model, model_id):
    db_model = get_by_id(db, model, model_id)
    try:
        if db_model:
            db.delete(db_model)
            db.commit()
            db.close()
            return True
        return False
    except Exception as e:
        print(e)
        return False
