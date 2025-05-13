import warnings
from .ufs import *

warnings.filterwarnings("default", category=DeprecationWarning,
                                   module=__name__)
warnings.warn("_rrfs_cmaq_mm is deprecated. Use ufs instead.", DeprecationWarning)



