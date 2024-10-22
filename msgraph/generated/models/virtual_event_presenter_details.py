from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_body import ItemBody

@dataclass
class VirtualEventPresenterDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Bio of the presenter.
    bio: Optional[ItemBody] = None
    # The presenter's company name.
    company: Optional[str] = None
    # The presenter's job title.
    job_title: Optional[str] = None
    # The presenter's LinkedIn profile URL.
    linked_in_profile_web_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The presenter's personal website URL.
    personal_site_web_url: Optional[str] = None
    # The content stream of the presenter's photo.
    photo: Optional[bytes] = None
    # The presenter's Twitter profile URL.
    twitter_profile_web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventPresenterDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventPresenterDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventPresenterDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .item_body import ItemBody

        from .item_body import ItemBody

        fields: Dict[str, Callable[[Any], None]] = {
            "bio": lambda n : setattr(self, 'bio', n.get_object_value(ItemBody)),
            "company": lambda n : setattr(self, 'company', n.get_str_value()),
            "jobTitle": lambda n : setattr(self, 'job_title', n.get_str_value()),
            "linkedInProfileWebUrl": lambda n : setattr(self, 'linked_in_profile_web_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "personalSiteWebUrl": lambda n : setattr(self, 'personal_site_web_url', n.get_str_value()),
            "photo": lambda n : setattr(self, 'photo', n.get_bytes_value()),
            "twitterProfileWebUrl": lambda n : setattr(self, 'twitter_profile_web_url', n.get_str_value()),
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
        from .item_body import ItemBody

        writer.write_object_value("bio", self.bio)
        writer.write_str_value("company", self.company)
        writer.write_str_value("jobTitle", self.job_title)
        writer.write_str_value("linkedInProfileWebUrl", self.linked_in_profile_web_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("personalSiteWebUrl", self.personal_site_web_url)
        writer.write_bytes_value("photo", self.photo)
        writer.write_str_value("twitterProfileWebUrl", self.twitter_profile_web_url)
        writer.write_additional_data_value(self.additional_data)
    

