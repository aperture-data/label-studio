from core.utils.params import get_env, get_bool_env
# #for importing by core.settings.label_studio
APERTUREDB_KEY = get_env( "APERTUREDB_KEY" , None )
APERTUREDB_DEFAULT_LIMIT = get_env( "APERTUREDB_DEFAULT_LIMIT",1000)
# This flag is used to make predictions read-only
# If set to True, predictions will not be editable in the UI
# If set to False, predictions will be editable in the UI
# The latter is a strange situation because predictions are shared 
# between all client projects.
APERTUREDB_PREDICTIONS_READONLY = get_bool_env( "APERTUREDB_RO_PREDS", True )
