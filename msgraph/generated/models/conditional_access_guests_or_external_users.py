from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_external_tenants, conditional_access_guest_or_external_user_types

@dataclass
class ConditionalAccessGuestsOrExternalUsers(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The tenant IDs of the selected types of external users. Either all B2B tenant or a collection of tenant IDs. External tenants can be specified only when the property guestOrExternalUserTypes is not null or an empty String.
    external_tenants: Optional[conditional_access_external_tenants.ConditionalAccessExternalTenants] = None
    # The guestOrExternalUserTypes property
    guest_or_external_user_types: Optional[conditional_access_guest_or_external_user_types.ConditionalAccessGuestOrExternalUserTypes] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessGuestsOrExternalUsers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessGuestsOrExternalUsers
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessGuestsOrExternalUsers()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_external_tenants, conditional_access_guest_or_external_user_types

        fields: Dict[str, Callable[[Any], None]] = {
            "externalTenants": lambda n : setattr(self, 'external_tenants', n.get_object_value(conditional_access_external_tenants.ConditionalAccessExternalTenants)),
            "guestOrExternalUserTypes": lambda n : setattr(self, 'guest_or_external_user_types', n.get_enum_value(conditional_access_guest_or_external_user_types.ConditionalAccessGuestOrExternalUserTypes)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("externalTenants", self.external_tenants)
        writer.write_enum_value("guestOrExternalUserTypes", self.guest_or_external_user_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

