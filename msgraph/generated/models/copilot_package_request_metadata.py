from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_package_request_info import CopilotPackageRequestInfo

@dataclass
class CopilotPackageRequestMetadata(AdditionalDataHolder, BackedModel, Parsable):
    """
    A snapshot of first explicit assignee contacts, request dates, and additional request data for a package.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The request snapshots returned by the service. Empty when metadata was loaded and no requests were found.
    requests: Optional[list[CopilotPackageRequestInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPackageRequestMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPackageRequestMetadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPackageRequestMetadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_package_request_info import CopilotPackageRequestInfo

        from .copilot_package_request_info import CopilotPackageRequestInfo

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requests": lambda n : setattr(self, 'requests', n.get_collection_of_object_values(CopilotPackageRequestInfo)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

