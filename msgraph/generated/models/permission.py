from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
item_reference = lazy_import('msgraph.generated.models.item_reference')
share_point_identity_set = lazy_import('msgraph.generated.models.share_point_identity_set')
sharing_invitation = lazy_import('msgraph.generated.models.sharing_invitation')
sharing_link = lazy_import('msgraph.generated.models.sharing_link')

class Permission(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new permission and sets the default values.
        """
        super().__init__()
        # A format of yyyy-MM-ddTHH:mm:ssZ of DateTimeOffset indicates the expiration time of the permission. DateTime.MinValue indicates there is no expiration set for this permission. Optional.
        self._expiration_date_time: Optional[datetime] = None
        # The grantedTo property
        self._granted_to: Optional[identity_set.IdentitySet] = None
        # The grantedToIdentities property
        self._granted_to_identities: Optional[List[identity_set.IdentitySet]] = None
        # For link type permissions, the details of the users to whom permission was granted. Read-only.
        self._granted_to_identities_v2: Optional[List[share_point_identity_set.SharePointIdentitySet]] = None
        # For user type permissions, the details of the users and applications for this permission. Read-only.
        self._granted_to_v2: Optional[share_point_identity_set.SharePointIdentitySet] = None
        # Indicates whether the password is set for this permission. This property only appears in the response. Optional. Read-only. For OneDrive Personal only..
        self._has_password: Optional[bool] = None
        # Provides a reference to the ancestor of the current permission, if it is inherited from an ancestor. Read-only.
        self._inherited_from: Optional[item_reference.ItemReference] = None
        # Details of any associated sharing invitation for this permission. Read-only.
        self._invitation: Optional[sharing_invitation.SharingInvitation] = None
        # Provides the link details of the current permission, if it is a link type permissions. Read-only.
        self._link: Optional[sharing_link.SharingLink] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The type of permission, for example, read. See below for the full list of roles. Read-only.
        self._roles: Optional[List[str]] = None
        # A unique token that can be used to access this shared item via the **shares** API. Read-only.
        self._share_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Permission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Permission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Permission()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. A format of yyyy-MM-ddTHH:mm:ssZ of DateTimeOffset indicates the expiration time of the permission. DateTime.MinValue indicates there is no expiration set for this permission. Optional.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. A format of yyyy-MM-ddTHH:mm:ssZ of DateTimeOffset indicates the expiration time of the permission. DateTime.MinValue indicates there is no expiration set for this permission. Optional.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "granted_to": lambda n : setattr(self, 'granted_to', n.get_object_value(identity_set.IdentitySet)),
            "granted_to_identities": lambda n : setattr(self, 'granted_to_identities', n.get_collection_of_object_values(identity_set.IdentitySet)),
            "granted_to_identities_v2": lambda n : setattr(self, 'granted_to_identities_v2', n.get_collection_of_object_values(share_point_identity_set.SharePointIdentitySet)),
            "granted_to_v2": lambda n : setattr(self, 'granted_to_v2', n.get_object_value(share_point_identity_set.SharePointIdentitySet)),
            "has_password": lambda n : setattr(self, 'has_password', n.get_bool_value()),
            "inherited_from": lambda n : setattr(self, 'inherited_from', n.get_object_value(item_reference.ItemReference)),
            "invitation": lambda n : setattr(self, 'invitation', n.get_object_value(sharing_invitation.SharingInvitation)),
            "link": lambda n : setattr(self, 'link', n.get_object_value(sharing_link.SharingLink)),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "share_id": lambda n : setattr(self, 'share_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def granted_to(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the grantedTo property value. The grantedTo property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._granted_to
    
    @granted_to.setter
    def granted_to(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the grantedTo property value. The grantedTo property
        Args:
            value: Value to set for the grantedTo property.
        """
        self._granted_to = value
    
    @property
    def granted_to_identities(self,) -> Optional[List[identity_set.IdentitySet]]:
        """
        Gets the grantedToIdentities property value. The grantedToIdentities property
        Returns: Optional[List[identity_set.IdentitySet]]
        """
        return self._granted_to_identities
    
    @granted_to_identities.setter
    def granted_to_identities(self,value: Optional[List[identity_set.IdentitySet]] = None) -> None:
        """
        Sets the grantedToIdentities property value. The grantedToIdentities property
        Args:
            value: Value to set for the grantedToIdentities property.
        """
        self._granted_to_identities = value
    
    @property
    def granted_to_identities_v2(self,) -> Optional[List[share_point_identity_set.SharePointIdentitySet]]:
        """
        Gets the grantedToIdentitiesV2 property value. For link type permissions, the details of the users to whom permission was granted. Read-only.
        Returns: Optional[List[share_point_identity_set.SharePointIdentitySet]]
        """
        return self._granted_to_identities_v2
    
    @granted_to_identities_v2.setter
    def granted_to_identities_v2(self,value: Optional[List[share_point_identity_set.SharePointIdentitySet]] = None) -> None:
        """
        Sets the grantedToIdentitiesV2 property value. For link type permissions, the details of the users to whom permission was granted. Read-only.
        Args:
            value: Value to set for the grantedToIdentitiesV2 property.
        """
        self._granted_to_identities_v2 = value
    
    @property
    def granted_to_v2(self,) -> Optional[share_point_identity_set.SharePointIdentitySet]:
        """
        Gets the grantedToV2 property value. For user type permissions, the details of the users and applications for this permission. Read-only.
        Returns: Optional[share_point_identity_set.SharePointIdentitySet]
        """
        return self._granted_to_v2
    
    @granted_to_v2.setter
    def granted_to_v2(self,value: Optional[share_point_identity_set.SharePointIdentitySet] = None) -> None:
        """
        Sets the grantedToV2 property value. For user type permissions, the details of the users and applications for this permission. Read-only.
        Args:
            value: Value to set for the grantedToV2 property.
        """
        self._granted_to_v2 = value
    
    @property
    def has_password(self,) -> Optional[bool]:
        """
        Gets the hasPassword property value. Indicates whether the password is set for this permission. This property only appears in the response. Optional. Read-only. For OneDrive Personal only..
        Returns: Optional[bool]
        """
        return self._has_password
    
    @has_password.setter
    def has_password(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasPassword property value. Indicates whether the password is set for this permission. This property only appears in the response. Optional. Read-only. For OneDrive Personal only..
        Args:
            value: Value to set for the hasPassword property.
        """
        self._has_password = value
    
    @property
    def inherited_from(self,) -> Optional[item_reference.ItemReference]:
        """
        Gets the inheritedFrom property value. Provides a reference to the ancestor of the current permission, if it is inherited from an ancestor. Read-only.
        Returns: Optional[item_reference.ItemReference]
        """
        return self._inherited_from
    
    @inherited_from.setter
    def inherited_from(self,value: Optional[item_reference.ItemReference] = None) -> None:
        """
        Sets the inheritedFrom property value. Provides a reference to the ancestor of the current permission, if it is inherited from an ancestor. Read-only.
        Args:
            value: Value to set for the inheritedFrom property.
        """
        self._inherited_from = value
    
    @property
    def invitation(self,) -> Optional[sharing_invitation.SharingInvitation]:
        """
        Gets the invitation property value. Details of any associated sharing invitation for this permission. Read-only.
        Returns: Optional[sharing_invitation.SharingInvitation]
        """
        return self._invitation
    
    @invitation.setter
    def invitation(self,value: Optional[sharing_invitation.SharingInvitation] = None) -> None:
        """
        Sets the invitation property value. Details of any associated sharing invitation for this permission. Read-only.
        Args:
            value: Value to set for the invitation property.
        """
        self._invitation = value
    
    @property
    def link(self,) -> Optional[sharing_link.SharingLink]:
        """
        Gets the link property value. Provides the link details of the current permission, if it is a link type permissions. Read-only.
        Returns: Optional[sharing_link.SharingLink]
        """
        return self._link
    
    @link.setter
    def link(self,value: Optional[sharing_link.SharingLink] = None) -> None:
        """
        Sets the link property value. Provides the link details of the current permission, if it is a link type permissions. Read-only.
        Args:
            value: Value to set for the link property.
        """
        self._link = value
    
    @property
    def roles(self,) -> Optional[List[str]]:
        """
        Gets the roles property value. The type of permission, for example, read. See below for the full list of roles. Read-only.
        Returns: Optional[List[str]]
        """
        return self._roles
    
    @roles.setter
    def roles(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roles property value. The type of permission, for example, read. See below for the full list of roles. Read-only.
        Args:
            value: Value to set for the roles property.
        """
        self._roles = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def share_id(self,) -> Optional[str]:
        """
        Gets the shareId property value. A unique token that can be used to access this shared item via the **shares** API. Read-only.
        Returns: Optional[str]
        """
        return self._share_id
    
    @share_id.setter
    def share_id(self,value: Optional[str] = None) -> None:
        """
        Sets the shareId property value. A unique token that can be used to access this shared item via the **shares** API. Read-only.
        Args:
            value: Value to set for the shareId property.
        """
        self._share_id = value
    

