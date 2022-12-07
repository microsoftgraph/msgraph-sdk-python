from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
share_point_identity = lazy_import('msgraph.generated.models.share_point_identity')

class SharePointIdentitySet(identity_set.IdentitySet):
    def __init__(self,) -> None:
        """
        Instantiates a new SharePointIdentitySet and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.sharePointIdentitySet"
        # The group associated with this action. Optional.
        self._group: Optional[identity.Identity] = None
        # The SharePoint group associated with this action. Optional.
        self._site_group: Optional[share_point_identity.SharePointIdentity] = None
        # The SharePoint user associated with this action. Optional.
        self._site_user: Optional[share_point_identity.SharePointIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharePointIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharePointIdentitySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharePointIdentitySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group": lambda n : setattr(self, 'group', n.get_object_value(identity.Identity)),
            "site_group": lambda n : setattr(self, 'site_group', n.get_object_value(share_point_identity.SharePointIdentity)),
            "site_user": lambda n : setattr(self, 'site_user', n.get_object_value(share_point_identity.SharePointIdentity)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group(self,) -> Optional[identity.Identity]:
        """
        Gets the group property value. The group associated with this action. Optional.
        Returns: Optional[identity.Identity]
        """
        return self._group
    
    @group.setter
    def group(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the group property value. The group associated with this action. Optional.
        Args:
            value: Value to set for the group property.
        """
        self._group = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("group", self.group)
        writer.write_object_value("siteGroup", self.site_group)
        writer.write_object_value("siteUser", self.site_user)
    
    @property
    def site_group(self,) -> Optional[share_point_identity.SharePointIdentity]:
        """
        Gets the siteGroup property value. The SharePoint group associated with this action. Optional.
        Returns: Optional[share_point_identity.SharePointIdentity]
        """
        return self._site_group
    
    @site_group.setter
    def site_group(self,value: Optional[share_point_identity.SharePointIdentity] = None) -> None:
        """
        Sets the siteGroup property value. The SharePoint group associated with this action. Optional.
        Args:
            value: Value to set for the siteGroup property.
        """
        self._site_group = value
    
    @property
    def site_user(self,) -> Optional[share_point_identity.SharePointIdentity]:
        """
        Gets the siteUser property value. The SharePoint user associated with this action. Optional.
        Returns: Optional[share_point_identity.SharePointIdentity]
        """
        return self._site_user
    
    @site_user.setter
    def site_user(self,value: Optional[share_point_identity.SharePointIdentity] = None) -> None:
        """
        Sets the siteUser property value. The SharePoint user associated with this action. Optional.
        Args:
            value: Value to set for the siteUser property.
        """
        self._site_user = value
    

