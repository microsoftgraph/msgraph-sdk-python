from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_package_request_principal import CopilotPackageRequestPrincipal
    from .email_address import EmailAddress

@dataclass
class CopilotPackageRequestInfo(AdditionalDataHolder, BackedModel, Parsable):
    """
    The business identifier, first explicit assignee contact, all explicit assignees, submission date, and additional collected data of one package request.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # All explicit assigned recipients returned by Governance, in source order with duplicates preserved. The first member supplies the requestedBy display contact; the collection is not truncated to that member. Empty means no explicit members were returned, not that the request has no audience. Broad or all-users audiences are not expanded or represented by this collection.
    assignees: Optional[list[CopilotPackageRequestPrincipal]] = None
    # The business request identifier returned by Governance, or null when unavailable. Not a requester identity, title identifier, correlation identifier, or Graph resource key or address. Uniqueness and lifetime stability are not guaranteed. No existing Graph operation in this proposal consumes this value.
    identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The display name and contact address of the first explicitly assigned principal. The address may be a mail address or user principal name. Null only when there are no explicit assignees; a present first assignee may have null name and address. The first principal may be a user, group, or agent; requestedBy does not identify the request creator.
    requested_by: Optional[EmailAddress] = None
    # The request submission date and time in ISO 8601 format. Null when unknown; independent of assignee presence and not the package creation or modification time.
    requested_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPackageRequestInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPackageRequestInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPackageRequestInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_package_request_principal import CopilotPackageRequestPrincipal
        from .email_address import EmailAddress

        from .copilot_package_request_principal import CopilotPackageRequestPrincipal
        from .email_address import EmailAddress

        fields: dict[str, Callable[[Any], None]] = {
            "assignees": lambda n : setattr(self, 'assignees', n.get_collection_of_object_values(CopilotPackageRequestPrincipal)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "requestedBy": lambda n : setattr(self, 'requested_by', n.get_object_value(EmailAddress)),
            "requestedDateTime": lambda n : setattr(self, 'requested_date_time', n.get_datetime_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

