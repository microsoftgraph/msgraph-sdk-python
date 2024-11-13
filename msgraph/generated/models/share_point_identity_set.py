from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity import Identity
    from .identity_set import IdentitySet
    from .share_point_identity import SharePointIdentity

from .identity_set import IdentitySet

@dataclass
class SharePointIdentitySet(IdentitySet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.sharePointIdentitySet"
    # The group associated with this action. Optional.
    group: Optional[Identity] = None
    # The SharePoint group associated with this action. Optional.
    site_group: Optional[SharePointIdentity] = None
    # The SharePoint user associated with this action. Optional.
    site_user: Optional[SharePointIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointIdentitySet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointIdentitySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity import Identity
        from .identity_set import IdentitySet
        from .share_point_identity import SharePointIdentity

        from .identity import Identity
        from .identity_set import IdentitySet
        from .share_point_identity import SharePointIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "group": lambda n : setattr(self, 'group', n.get_object_value(Identity)),
            "siteGroup": lambda n : setattr(self, 'site_group', n.get_object_value(SharePointIdentity)),
            "siteUser": lambda n : setattr(self, 'site_user', n.get_object_value(SharePointIdentity)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .identity import Identity
        from .identity_set import IdentitySet
        from .share_point_identity import SharePointIdentity

        writer.write_object_value("group", self.group)
        writer.write_object_value("siteGroup", self.site_group)
        writer.write_object_value("siteUser", self.site_user)
    

