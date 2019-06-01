from app.models import db

class BaseResources():

    def __init__(self, model):
        self.model = model

    def getAll(self, params=None):
        try:
            if params is None:
                query = self.model.query.all()
                return {'response':[i.serialize for i in query], 'status':200}
            
            query = self.model.query.filter_by(**params).all()
            return {'response':[i.serialize for i in query], 'status':200}

        except Exception as e:
            return {'response':str(e), 'status':406}

    def getFirst(self, params=None):
        try:
            if params is None:
                query = self.model.query.first()
                return {'response':[i.serialize], 'status':200}
            
            query = self.model.query.filter_by(**params).first()
            return {'response':[i.serialize], 'status':200}

        except Exception as e:
            return {'response':str(e), 'status':406}
    
    def postData(self, params):
        try:
            query = self.model(**params)
            db.session.add(query)
            db.session.commit()
            return {'response':'created successfully', 'status':201}

        except Exception as e:
            return {'response':str(e), 'status':406}
    
    def putData(self, search, params):
        try:
            query = self.model.query.filter_by(**search)
            if query is None:
                return {'response':'empty search', 'status':404}
            
            query.update(**params)
            db.session.commit()
            return {'response':'updated successfully', 'status':200}

        except Exception as e:
            return {'response':str(e), 'status':406}
        
    def deleteData(self, search):
        try:
            query = self.model.query.filter_by(**search)
            if query is None:
                return {'response':'empty search', 'status':404}
            
            db.session.delete(me)
            db.session.commit()
            return {'response':'deleted successfully', 'status':200}
        except Exception as e:
            return {'response':str(e), 'status':406}
