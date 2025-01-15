from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .item_reference import ItemReference
    from .share_point_identity_set import SharePointIdentitySet
    from .sharing_invitation import SharingInvitation
    from .sharing_link import SharingLink

from .entity import Entity

@dataclass
class Permission(Entity, Parsable):
    # A format of yyyy-MM-ddTHH:mm:ssZ of DateTimeOffset indicates the expiration time of the permission. DateTime.MinValue indicates there's no expiration set for this permission. Optional.
    expiration_date_time: Optional[datetime.datetime] = None
    # For user type permissions, the details of the users and applications for this permission. Read-only.
    granted_to: Optional[IdentitySet] = None
    # For type permissions, the details of the users to whom permission was granted. Read-only.
    granted_to_identities: Optional[list[IdentitySet]] = None
    # For link type permissions, the details of the users to whom permission was granted. Read-only.
    granted_to_identities_v2: Optional[list[SharePointIdentitySet]] = None
    # For user type permissions, the details of the users and applications for this permission. Read-only.
    granted_to_v2: Optional[SharePointIdentitySet] = None
    # Indicates whether the password is set for this permission. This property only appears in the response. Optional. Read-only. For OneDrive Personal only..
    has_password: Optional[bool] = None
    # Provides a reference to the ancestor of the current permission, if it's inherited from an ancestor. Read-only.
    inherited_from: Optional[ItemReference] = None
    # Details of any associated sharing invitation for this permission. Read-only.
    invitation: Optional[SharingInvitation] = None
    # Provides the link details of the current permission, if it's a link type permission. Read-only.
    link: Optional[SharingLink] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of permission, for example, read. See below for the full list of roles. Read-only.
    roles: Optional[list[str]] = None
    # A unique token that can be used to access this shared item via the shares API. Read-only.
    share_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Permission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Permission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Permission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .item_reference import ItemReference
        from .share_point_identity_set import SharePointIdentitySet
        from .sharing_invitation import SharingInvitation
        from .sharing_link import SharingLink

        from .entity import Entity
        from .identity_set import IdentitySet
        from .item_reference import ItemReference
        from .share_point_identity_set import SharePointIdentitySet
        from .sharing_invitation import SharingInvitation
        from .sharing_link import SharingLink

        fields: dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "grantedTo": lambda n : setattr(self, 'granted_to', n.get_object_value(IdentitySet)),
            "grantedToIdentities": lambda n : setattr(self, 'granted_to_identities', n.get_collection_of_object_values(IdentitySet)),
            "grantedToIdentitiesV2": lambda n : setattr(self, 'granted_to_identities_v2', n.get_collection_of_object_values(SharePointIdentitySet)),
            "grantedToV2": lambda n : setattr(self, 'granted_to_v2', n.get_object_value(SharePointIdentitySet)),
            "hasPassword": lambda n : setattr(self, 'has_password', n.get_bool_value()),
            "inheritedFrom": lambda n : setattr(self, 'inherited_from', n.get_object_value(ItemReference)),
            "invitation": lambda n : setattr(self, 'invitation', n.get_object_value(SharingInvitation)),
            "link": lambda n : setattr(self, 'link', n.get_object_value(SharingLink)),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "shareId": lambda n : setattr(self, 'share_id', n.get_str_value()),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_object_value("grantedTo", self.granted_to)
        writer.write_collection_of_object_values("grantedToIdentities", self.granted_to_identities)
        writer.write_collection_of_object_values("grantedToIdentitiesV2", self.granted_to_identities_v2)
        writer.write_object_value("grantedToV2", self.granted_to_v2)
        writer.write_bool_value("hasPassword", self.has_password)
        writer.write_object_value("inheritedFrom", self.inherited_from)
        writer.write_object_value("invitation", self.invitation)
        writer.write_object_value("link", self.link)
        writer.write_collection_of_primitive_values("roles", self.roles)
        writer.write_str_value("shareId", self.share_id)
    

