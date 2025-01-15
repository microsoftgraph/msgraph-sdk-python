from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teams_app_permission_set import TeamsAppPermissionSet

@dataclass
class TeamsAppAuthorization(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The registration ID of the Microsoft Entra app ID associated with the teamsApp.
    client_app_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Set of permissions required by the teamsApp.
    required_permission_set: Optional[TeamsAppPermissionSet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppAuthorization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppAuthorization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppAuthorization()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teams_app_permission_set import TeamsAppPermissionSet

        from .teams_app_permission_set import TeamsAppPermissionSet

        fields: dict[str, Callable[[Any], None]] = {
            "clientAppId": lambda n : setattr(self, 'client_app_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requiredPermissionSet": lambda n : setattr(self, 'required_permission_set', n.get_object_value(TeamsAppPermissionSet)),
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
        writer.write_str_value("clientAppId", self.client_app_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("requiredPermissionSet", self.required_permission_set)
        writer.write_additional_data_value(self.additional_data)
    

