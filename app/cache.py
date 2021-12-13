
from detacache import DetaCache

from app.settings import setting

detaCache = DetaCache(projectKey=setting.DETA_PROJECT_KEY,baseName=setting.DETA_BASE_NAME)

expire = setting.EXPIRE

log = setting.LOG
