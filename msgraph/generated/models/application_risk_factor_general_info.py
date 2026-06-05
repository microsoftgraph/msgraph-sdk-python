from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_data_type import ApplicationDataType
    from .application_location import ApplicationLocation
    from .hold_type import HoldType

@dataclass
class ApplicationRiskFactorGeneralInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates the relative popularity or adoption of the application based on the user or tenant usage metrics.
    consumer_popularity: Optional[int] = None
    # Specifies the date when the application's primary domain was registered, used to assess domain maturity and legitimacy.
    domain_registration_date: Optional[datetime.date] = None
    # Year the company or organization behind the application was founded.
    founded: Optional[int] = None
    # Indicates whether the application provider maintains a disaster recovery or business continuity plan.
    has_disaster_recovery_plan: Optional[bool] = None
    # The hold property
    hold: Optional[HoldType] = None
    # Specifies the name of the company or provider that hosts the application's infrastructure.
    hosting_company_name: Optional[str] = None
    # Provides the geographical and operational location information for the application, including data center and headquarters regions.
    location: Optional[ApplicationLocation] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the URL of the application's privacy policy.
    privacy_policy: Optional[str] = None
    # The processedDataTypes property
    processed_data_types: Optional[ApplicationDataType] = None
    # Specifies the URL of the application's terms of service.
    terms_of_service: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationRiskFactorGeneralInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationRiskFactorGeneralInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationRiskFactorGeneralInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_data_type import ApplicationDataType
        from .application_location import ApplicationLocation
        from .hold_type import HoldType

        from .application_data_type import ApplicationDataType
        from .application_location import ApplicationLocation
        from .hold_type import HoldType

        fields: dict[str, Callable[[Any], None]] = {
            "consumerPopularity": lambda n : setattr(self, 'consumer_popularity', n.get_int_value()),
            "domainRegistrationDate": lambda n : setattr(self, 'domain_registration_date', n.get_date_value()),
            "founded": lambda n : setattr(self, 'founded', n.get_int_value()),
            "hasDisasterRecoveryPlan": lambda n : setattr(self, 'has_disaster_recovery_plan', n.get_bool_value()),
            "hold": lambda n : setattr(self, 'hold', n.get_enum_value(HoldType)),
            "hostingCompanyName": lambda n : setattr(self, 'hosting_company_name', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(ApplicationLocation)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "privacyPolicy": lambda n : setattr(self, 'privacy_policy', n.get_str_value()),
            "processedDataTypes": lambda n : setattr(self, 'processed_data_types', n.get_collection_of_enum_values(ApplicationDataType)),
            "termsOfService": lambda n : setattr(self, 'terms_of_service', n.get_str_value()),
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
        writer.write_int_value("consumerPopularity", self.consumer_popularity)
        writer.write_date_value("domainRegistrationDate", self.domain_registration_date)
        writer.write_int_value("founded", self.founded)
        writer.write_bool_value("hasDisasterRecoveryPlan", self.has_disaster_recovery_plan)
        writer.write_enum_value("hold", self.hold)
        writer.write_str_value("hostingCompanyName", self.hosting_company_name)
        writer.write_object_value("location", self.location)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("privacyPolicy", self.privacy_policy)
        writer.write_enum_value("processedDataTypes", self.processed_data_types)
        writer.write_str_value("termsOfService", self.terms_of_service)
        writer.write_additional_data_value(self.additional_data)
    

