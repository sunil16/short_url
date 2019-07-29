from model.schema import *

def get_model_obj():
    return Url()

def insert(table_name=None, data=None):
    if table_name == "urls" and data != None:
        m_obj = get_model_obj()
        m_obj.original_url = data
        m_obj.visitcount = 0
        db.session.add(m_obj)
        db.session.commit()
        new_inserted_record_id = m_obj.id
        return new_inserted_record_id
    return None


def find_and_update(table_name=None, id=None):
    if table_name == "urls" and id != None:
        visited_url = db.session.query(Url).filter(Url.id == id).first()
        if visited_url != None:
            import ipdb; ipdb.set_trace()
            count = visited_url.visitcount + 1
            visited_url.visitcount = count
            db.session.commit()
            return visited_url.original_url
    return None


def find(table_name=None, data=None):
    if table_name == "urls" and data != None:
        db_obj = db.session.query(Url).filter(Url.original_url.like("%"+data['query_str']+"%")).all()
        return db_obj
    return None
