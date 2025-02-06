from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Certification(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # URL that shows certification details for the application.
    certification_details_url: Optional[str] = None
    # The timestamp when the current certification for the application expires.
    certification_expiration_date_time: Optional[datetime.datetime] = None
    # Indicates whether the application is certified by Microsoft.
    is_certified_by_microsoft: Optional[bool] = None
    # Indicates whether the application developer or publisher completed Publisher Attestation.
    is_publisher_attested: Optional[bool] = None
    # The timestamp when the certification for the application was most recently added or updated.
    last_certification_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Certification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Certification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Certification()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "certificationDetailsUrl": lambda n : setattr(self, 'certification_details_url', n.get_str_value()),
            "certificationExpirationDateTime": lambda n : setattr(self, 'certification_expiration_date_time', n.get_datetime_value()),
            "isCertifiedByMicrosoft": lambda n : setattr(self, 'is_certified_by_microsoft', n.get_bool_value()),
            "isPublisherAttested": lambda n : setattr(self, 'is_publisher_attested', n.get_bool_value()),
            "lastCertificationDateTime": lambda n : setattr(self, 'last_certification_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("certificationExpirationDateTime", self.certification_expiration_date_time)
        writer.write_bool_value("isPublisherAttested", self.is_publisher_attested)
        writer.write_datetime_value("lastCertificationDateTime", self.last_certification_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

