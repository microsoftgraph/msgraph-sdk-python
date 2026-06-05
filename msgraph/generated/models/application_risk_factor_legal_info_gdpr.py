from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .data_protection import DataProtection
    from .user_ownership import UserOwnership

@dataclass
class ApplicationRiskFactorLegalInfoGdpr(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The dataProtection property
    data_protection: Optional[DataProtection] = None
    # Indicates whether the application provides users with the ability to request deletion of their personal data (the right to be forgotten).
    has_right_to_erasure: Optional[bool] = None
    # Indicates whether the organization reports personal data breaches to authorities and affected users in accordance with GDPR requirements.
    is_reporting_data_breaches: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the URL of the application's GDPR or privacy compliance statement, outlining how user data is handled.
    statement_url: Optional[str] = None
    # The userOwnership property
    user_ownership: Optional[UserOwnership] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationRiskFactorLegalInfoGdpr:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationRiskFactorLegalInfoGdpr
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationRiskFactorLegalInfoGdpr()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .data_protection import DataProtection
        from .user_ownership import UserOwnership

        from .data_protection import DataProtection
        from .user_ownership import UserOwnership

        fields: dict[str, Callable[[Any], None]] = {
            "dataProtection": lambda n : setattr(self, 'data_protection', n.get_collection_of_enum_values(DataProtection)),
            "hasRightToErasure": lambda n : setattr(self, 'has_right_to_erasure', n.get_bool_value()),
            "isReportingDataBreaches": lambda n : setattr(self, 'is_reporting_data_breaches', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "statementUrl": lambda n : setattr(self, 'statement_url', n.get_str_value()),
            "userOwnership": lambda n : setattr(self, 'user_ownership', n.get_collection_of_enum_values(UserOwnership)),
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
        writer.write_enum_value("dataProtection", self.data_protection)
        writer.write_bool_value("hasRightToErasure", self.has_right_to_erasure)
        writer.write_bool_value("isReportingDataBreaches", self.is_reporting_data_breaches)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("statementUrl", self.statement_url)
        writer.write_enum_value("userOwnership", self.user_ownership)
        writer.write_additional_data_value(self.additional_data)
    

