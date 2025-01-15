from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_external_tenants import ConditionalAccessExternalTenants
    from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes

@dataclass
class ConditionalAccessGuestsOrExternalUsers(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The tenant IDs of the selected types of external users. Either all B2B tenant or a collection of tenant IDs. External tenants can be specified only when the property guestOrExternalUserTypes isn't null or an empty String.
    external_tenants: Optional[ConditionalAccessExternalTenants] = None
    # The guestOrExternalUserTypes property
    guest_or_external_user_types: Optional[ConditionalAccessGuestOrExternalUserTypes] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessGuestsOrExternalUsers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessGuestsOrExternalUsers
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessGuestsOrExternalUsers()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_external_tenants import ConditionalAccessExternalTenants
        from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes

        from .conditional_access_external_tenants import ConditionalAccessExternalTenants
        from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes

        fields: dict[str, Callable[[Any], None]] = {
            "externalTenants": lambda n : setattr(self, 'external_tenants', n.get_object_value(ConditionalAccessExternalTenants)),
            "guestOrExternalUserTypes": lambda n : setattr(self, 'guest_or_external_user_types', n.get_collection_of_enum_values(ConditionalAccessGuestOrExternalUserTypes)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("externalTenants", self.external_tenants)
        writer.write_enum_value("guestOrExternalUserTypes", self.guest_or_external_user_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

