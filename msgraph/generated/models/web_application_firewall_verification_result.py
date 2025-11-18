from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .generic_error import GenericError
    from .web_application_firewall_verification_status import WebApplicationFirewallVerificationStatus

@dataclass
class WebApplicationFirewallVerificationResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # List of errors encountered during the verification process.
    errors: Optional[list[GenericError]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[WebApplicationFirewallVerificationStatus] = None
    # UTC timestamp when the verification was performed or last updated. This indicates when the verification result was produced.
    verified_on_date_time: Optional[datetime.datetime] = None
    # List of warnings produced during verification.
    warnings: Optional[list[GenericError]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebApplicationFirewallVerificationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebApplicationFirewallVerificationResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebApplicationFirewallVerificationResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .generic_error import GenericError
        from .web_application_firewall_verification_status import WebApplicationFirewallVerificationStatus

        from .generic_error import GenericError
        from .web_application_firewall_verification_status import WebApplicationFirewallVerificationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(GenericError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(WebApplicationFirewallVerificationStatus)),
            "verifiedOnDateTime": lambda n : setattr(self, 'verified_on_date_time', n.get_datetime_value()),
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_object_values(GenericError)),
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
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("verifiedOnDateTime", self.verified_on_date_time)
        writer.write_collection_of_object_values("warnings", self.warnings)
        writer.write_additional_data_value(self.additional_data)
    

