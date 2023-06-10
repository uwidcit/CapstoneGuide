# blue prints are imported 
# explicitly instead of using *
#from .user import user_views
from .index import index_views
from .auth import auth_views
from .proposal import proposal_views
from .evaluation import evaluation_views
from .rubric import rubric_views
from .registration import registration_views
from .history import history_views
from .stuQuery import stuQuery_views


views = [
    index_views, 
    proposal_views, 
    evaluation_views, 
    rubric_views,
    registration_views, 
    history_views, 
    stuQuery_views
]
# blueprints must be added to this list