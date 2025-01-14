from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .profile_card_annotation import ProfileCardAnnotation

from .entity import Entity

@dataclass
class ProfileCardProperty(Entity, Parsable):
    # Allows an administrator to set a custom display label for the directory property and localize it for the users in their tenant.
    annotations: Optional[list[ProfileCardAnnotation]] = None
    # Identifies a profileCardProperty resource in Get, Update, or Delete operations. Allows an administrator to surface hidden Microsoft Entra ID properties on the Microsoft 365 profile card within their tenant. When present, the Microsoft Entra ID field referenced in this property is visible to all users in your tenant on the contact pane of the profile card. Allowed values for this field are: UserPrincipalName, Fax, StreetAddress, PostalCode, StateOrProvince, Alias, CustomAttribute1,  CustomAttribute2, CustomAttribute3, CustomAttribute4, CustomAttribute5, CustomAttribute6, CustomAttribute7, CustomAttribute8, CustomAttribute9, CustomAttribute10, CustomAttribute11, CustomAttribute12, CustomAttribute13, CustomAttribute14, CustomAttribute15.
    directory_property_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProfileCardProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProfileCardProperty
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProfileCardProperty()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .profile_card_annotation import ProfileCardAnnotation

        from .entity import Entity
        from .profile_card_annotation import ProfileCardAnnotation

        fields: dict[str, Callable[[Any], None]] = {
            "annotations": lambda n : setattr(self, 'annotations', n.get_collection_of_object_values(ProfileCardAnnotation)),
            "directoryPropertyName": lambda n : setattr(self, 'directory_property_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("annotations", self.annotations)
        writer.write_str_value("directoryPropertyName", self.directory_property_name)
    

