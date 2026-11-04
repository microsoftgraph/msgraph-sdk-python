from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_migration_service_status import CrossTenantMigrationServiceStatus
    from .error import Error

@dataclass
class CrossTenantMigrationServiceStatusDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Errors associated with the migration for this service.
    errors: Optional[list[Error]] = None
    # Service status message.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Service or workload associated with the status details.
    service: Optional[str] = None
    # The status property
    status: Optional[CrossTenantMigrationServiceStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantMigrationServiceStatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantMigrationServiceStatusDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantMigrationServiceStatusDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_migration_service_status import CrossTenantMigrationServiceStatus
        from .error import Error

        from .cross_tenant_migration_service_status import CrossTenantMigrationServiceStatus
        from .error import Error

        fields: dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(Error)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CrossTenantMigrationServiceStatus)),
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
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("service", self.service)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

