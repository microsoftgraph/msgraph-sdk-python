from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .client_user_agent import ClientUserAgent
    from .service_user_agent import ServiceUserAgent

@dataclass
class UserAgent(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Identifies the version of application software used by this endpoint.
    application_version: Optional[str] = None
    # User-agent header value reported by this endpoint.
    header_value: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserAgent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.clientUserAgent".casefold():
            from .client_user_agent import ClientUserAgent

            return ClientUserAgent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.serviceUserAgent".casefold():
            from .service_user_agent import ServiceUserAgent

            return ServiceUserAgent()
        return UserAgent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .client_user_agent import ClientUserAgent
        from .service_user_agent import ServiceUserAgent

        from .client_user_agent import ClientUserAgent
        from .service_user_agent import ServiceUserAgent

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationVersion": lambda n : setattr(self, 'application_version', n.get_str_value()),
            "headerValue": lambda n : setattr(self, 'header_value', n.get_str_value()),
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
        writer.write_str_value("applicationVersion", self.application_version)
        writer.write_str_value("headerValue", self.header_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

