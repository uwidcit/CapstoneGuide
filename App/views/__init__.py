# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .proposal import proposal_views
from .evaluation import evaluation_views
from .addRequirement import addRequirement_views
from .viewRequirement import viewRubric_views
from .registration import registration_views
from .history import history_views
from .stuQuery import stuQuery_views


views = [index_views, auth_views, proposal_views, evaluation_views, addRequirement_views, viewRubric_views,
         registration_views, history_views, stuQuery_views]
# blueprints must be added to this list