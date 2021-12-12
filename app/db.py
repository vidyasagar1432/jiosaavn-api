from deta import Deta

from app.settings import setting


db = Deta(setting.DETA_PROJECT_KEY).Base(setting.DETA_BASE_NAME)
