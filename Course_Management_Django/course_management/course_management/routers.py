# course_management/routers.py

class MongoDBRouter:
    """
    A router to control all database operations on models in the
    assessments app.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read assessments models go to mongodb.
        """
        if model._meta.app_label == 'assessments':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write assessments models go to mongodb.
        """
        if model._meta.app_label == 'assessments':
            return 'mongodb'
        return 'default'

    def db_for_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the assessments app only appears in the
        'mongodb' database.
        """
        if app_label == 'assessments':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the assessments app is involved.
        """
        if obj1._meta.app_label == 'assessments' or obj2._meta.app_label == 'assessments':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the assessments app only appears in the
        'mongodb' database.
        """
        if app_label == 'assessments':
            return db == 'mongodb'
        return db == 'default'