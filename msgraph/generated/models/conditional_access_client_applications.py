from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ConditionalAccessClientApplications(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Service principal IDs excluded from the policy scope.
    exclude_service_principals: Optional[List[str]] = None
    # Service principal IDs included in the policy scope, or ServicePrincipalsInMyTenant.
    include_service_principals: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessClientApplications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessClientApplications
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessClientApplications()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "excludeServicePrincipals": lambda n : setattr(self, 'exclude_service_principals', n.get_collection_of_primitive_values(str)),
            "includeServicePrincipals": lambda n : setattr(self, 'include_service_principals', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("excludeServicePrincipals", self.exclude_service_principals)
        writer.write_collection_of_primitive_values("includeServicePrincipals", self.include_service_principals)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

