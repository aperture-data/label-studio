# allows extensions by code not intented to go in main
from dataclasses import dataclass

@dataclass
class extension_iface():
    ref:int # last used ref
    object_ref:int # reference for object for call
    object_id:str # unique id for object for call


# return a list of aperturedb commands to add to the query when saving an annotation
def append_to_save_annotation( ctx:extension_iface ):
    return []
def append_to_save_bbox( ctx:extension_iface ):
    return []
