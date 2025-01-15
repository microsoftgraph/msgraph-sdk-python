from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value import KeyValue

@dataclass
class ContentCustomization(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Represents the content options of External Identities to be customized throughout the authentication flow for a tenant.
    attribute_collection: Optional[list[KeyValue]] = None
    # A relative URL for the content options of External Identities to be customized throughout the authentication flow for a tenant.
    attribute_collection_relative_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents content options to customize during MFA proofup interruptions.
    registration_campaign: Optional[list[KeyValue]] = None
    # The relative URL of the content options to customize during MFA proofup interruptions.
    registration_campaign_relative_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentCustomization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentCustomization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentCustomization()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .key_value import KeyValue

        from .key_value import KeyValue

        fields: dict[str, Callable[[Any], None]] = {
            "attributeCollection": lambda n : setattr(self, 'attribute_collection', n.get_collection_of_object_values(KeyValue)),
            "attributeCollectionRelativeUrl": lambda n : setattr(self, 'attribute_collection_relative_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "registrationCampaign": lambda n : setattr(self, 'registration_campaign', n.get_collection_of_object_values(KeyValue)),
            "registrationCampaignRelativeUrl": lambda n : setattr(self, 'registration_campaign_relative_url', n.get_str_value()),
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
        writer.write_collection_of_object_values("attributeCollection", self.attribute_collection)
        writer.write_str_value("attributeCollectionRelativeUrl", self.attribute_collection_relative_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("registrationCampaign", self.registration_campaign)
        writer.write_str_value("registrationCampaignRelativeUrl", self.registration_campaign_relative_url)
        writer.write_additional_data_value(self.additional_data)
    

