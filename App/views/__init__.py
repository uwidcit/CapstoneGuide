# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .proposal import proposal_views
from .evaluation import evaluation_views
from .addRequirement import addRequirement_views
from .viewRequirement import viewRequirement_views
from .registration import registration_views


views = [index_views, auth_views, proposal_views, evaluation_views, addRequirement_views, viewRequirement_views,
         registration_views]
# blueprints must be added to this list