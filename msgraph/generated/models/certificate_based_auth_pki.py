from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_authority_detail import CertificateAuthorityDetail
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class CertificateBasedAuthPki(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.certificateBasedAuthPki"
    # The certificateAuthorities property
    certificate_authorities: Optional[list[CertificateAuthorityDetail]] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The status property
    status: Optional[str] = None
    # The statusDetails property
    status_details: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CertificateBasedAuthPki:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CertificateBasedAuthPki
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CertificateBasedAuthPki()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_authority_detail import CertificateAuthorityDetail
        from .directory_object import DirectoryObject

        from .certificate_authority_detail import CertificateAuthorityDetail
        from .directory_object import DirectoryObject

        fields: dict[str, Callable[[Any], None]] = {
            "certificateAuthorities": lambda n : setattr(self, 'certificate_authorities', n.get_collection_of_object_values(CertificateAuthorityDetail)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("certificateAuthorities", self.certificate_authorities)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("status", self.status)
        writer.write_str_value("statusDetails", self.status_details)
    

