from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.print_job_configuration import PrintJobConfiguration

@dataclass
class RedirectPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The configuration property
    configuration: Optional[PrintJobConfiguration] = None
    # The destinationPrinterId property
    destination_printer_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RedirectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RedirectPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RedirectPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models.print_job_configuration import PrintJobConfiguration

        from .......models.print_job_configuration import PrintJobConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(PrintJobConfiguration)),
            "destinationPrinterId": lambda n : setattr(self, 'destination_printer_id', n.get_str_value()),
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
        from .......models.print_job_configuration import PrintJobConfiguration

        writer.write_object_value("configuration", self.configuration)
        writer.write_str_value("destinationPrinterId", self.destination_printer_id)
        writer.write_additional_data_value(self.additional_data)
    

