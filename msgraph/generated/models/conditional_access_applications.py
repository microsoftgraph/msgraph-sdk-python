from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ConditionalAccessApplications(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Can be one of the following:  The list of client IDs (appId) explicitly excluded from the policy. Office365 - For the list of apps included in Office365, see Conditional Access target apps: Office 365
    exclude_applications: Optional[List[str]] = None
    # Can be one of the following:  The list of client IDs (appId) the policy applies to, unless explicitly excluded (in excludeApplications)  All  Office365 - For the list of apps included in Office365, see Conditional Access target apps: Office 365
    include_applications: Optional[List[str]] = None
    # The includeAuthenticationContextClassReferences property
    include_authentication_context_class_references: Optional[List[str]] = None
    # User actions to include. Supported values are urn:user:registersecurityinfo and urn:user:registerdevice
    include_user_actions: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessApplications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessApplications
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessApplications()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "excludeApplications": lambda n : setattr(self, 'exclude_applications', n.get_collection_of_primitive_values(str)),
            "includeApplications": lambda n : setattr(self, 'include_applications', n.get_collection_of_primitive_values(str)),
            "includeAuthenticationContextClassReferences": lambda n : setattr(self, 'include_authentication_context_class_references', n.get_collection_of_primitive_values(str)),
            "includeUserActions": lambda n : setattr(self, 'include_user_actions', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("excludeApplications", self.exclude_applications)
        writer.write_collection_of_primitive_values("includeApplications", self.include_applications)
        writer.write_collection_of_primitive_values("includeAuthenticationContextClassReferences", self.include_authentication_context_class_references)
        writer.write_collection_of_primitive_values("includeUserActions", self.include_user_actions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

