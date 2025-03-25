from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_filter import ConditionalAccessFilter

@dataclass
class ConditionalAccessApplications(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Filter that defines the dynamic-application-syntax rule to include/exclude cloud applications. A filter can use custom security attributes to include/exclude applications.
    application_filter: Optional[ConditionalAccessFilter] = None
    # Can be one of the following:  The list of client IDs (appId) explicitly excluded from the policy. Office365 - For the list of apps included in Office365, see Apps included in Conditional Access Office 365 app suite  MicrosoftAdminPortals - For more information, see Conditional Access Target resources: Microsoft Admin Portals
    exclude_applications: Optional[list[str]] = None
    # Can be one of the following:  The list of client IDs (appId) the policy applies to, unless explicitly excluded (in excludeApplications)  All  Office365 - For the list of apps included in Office365, see Apps included in Conditional Access Office 365 app suite  MicrosoftAdminPortals - For more information, see Conditional Access Target resources: Microsoft Admin Portals
    include_applications: Optional[list[str]] = None
    # The includeAuthenticationContextClassReferences property
    include_authentication_context_class_references: Optional[list[str]] = None
    # User actions to include. Supported values are urn:user:registersecurityinfo and urn:user:registerdevice
    include_user_actions: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessApplications:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessApplications
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessApplications()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_filter import ConditionalAccessFilter

        from .conditional_access_filter import ConditionalAccessFilter

        fields: dict[str, Callable[[Any], None]] = {
            "applicationFilter": lambda n : setattr(self, 'application_filter', n.get_object_value(ConditionalAccessFilter)),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("applicationFilter", self.application_filter)
        writer.write_collection_of_primitive_values("excludeApplications", self.exclude_applications)
        writer.write_collection_of_primitive_values("includeApplications", self.include_applications)
        writer.write_collection_of_primitive_values("includeAuthenticationContextClassReferences", self.include_authentication_context_class_references)
        writer.write_collection_of_primitive_values("includeUserActions", self.include_user_actions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

