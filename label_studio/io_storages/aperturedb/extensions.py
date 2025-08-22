# allows extensions by code not intented to go in main
from dataclasses import dataclass

@dataclass
class extension_iface():
    ref:int # last used ref - USER CAN MODIFY
    object_ref:int # reference for object for call
    object_id:str # unique id for object for call

# passes the iface and the annotation props
# returns modified props
def modify_annotation_add_props( annotation_props:object,  ctx:extension_iface ):
    return annotation_props

def modify_bbox_add_props( bbox_props:object,  ctx:extension_iface ):
    return bbox_props

# passes a iface which callee can modify to put private data or update ref.
# return a list of aperturedb commands to add to the query when saving an annotation
def append_to_save_annotation( ctx:extension_iface ):
    return []

# passes a iface which callee can modify to put private data or update ref.
# return a list of aperturedb commands to add to the query when saving an annotation
def append_to_save_bbox( ctx:extension_iface ):
    return []
