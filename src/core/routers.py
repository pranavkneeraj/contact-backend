"""
Router that maps to external DB for tier and blog related data
"""

import copy
from django_sharding_library.router import ShardedRouter

class CoreRouter(ShardedRouter):
    # add write_db key if writes are to be sent to different db
    common_apps = {
        'contact': {'default_db': 'default', 'allow_write': True, 'allow_migration': True},
    }


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        print((not db == "default") and (app_label not in self.common_apps))
        if (not db == "default") and (app_label not in self.common_apps):
            return False
        return True
