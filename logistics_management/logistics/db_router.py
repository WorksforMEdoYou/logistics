class LogisticsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'logistics':
            if model.__name__ in ['Customer', 'Shipper']:
                return 'default'  # MySQL
        return None  # MongoDB

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'logistics' and model_name in ['customer', 'shipper']:
            return db == 'default'
        return False
