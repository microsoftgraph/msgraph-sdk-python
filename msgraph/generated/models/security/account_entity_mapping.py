from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity_mapping import EntityMapping

from .entity_mapping import EntityMapping

@dataclass
class AccountEntityMapping(EntityMapping, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.accountEntityMapping"
    # Name of the detection query column that maps to the Microsoft Entra user ID of the alert entity.
    aad_user_id_column: Optional[str] = None
    # Name of the detection query column that maps to the DNS domain of the alert entity.
    dns_domain_column: Optional[str] = None
    # Name of the detection query column that maps to the name of the alert entity.
    name_column: Optional[str] = None
    # Name of the detection query column that maps to the NT domain of the alert entity.
    nt_domain_column: Optional[str] = None
    # Name of the detection query column that maps to the security identifier (SID) of the alert entity.
    sid_column: Optional[str] = None
    # Name of the detection query column that maps to the user principal name (UPN) of the alert entity.
    upn_column: Optional[str] = None
    # Name of the detection query column that maps to the UPN suffix of the alert entity.
    upn_suffix_column: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccountEntityMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccountEntityMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccountEntityMapping()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity_mapping import EntityMapping

        from .entity_mapping import EntityMapping

        fields: dict[str, Callable[[Any], None]] = {
            "aadUserIdColumn": lambda n : setattr(self, 'aad_user_id_column', n.get_str_value()),
            "dnsDomainColumn": lambda n : setattr(self, 'dns_domain_column', n.get_str_value()),
            "nameColumn": lambda n : setattr(self, 'name_column', n.get_str_value()),
            "ntDomainColumn": lambda n : setattr(self, 'nt_domain_column', n.get_str_value()),
            "sidColumn": lambda n : setattr(self, 'sid_column', n.get_str_value()),
            "upnColumn": lambda n : setattr(self, 'upn_column', n.get_str_value()),
            "upnSuffixColumn": lambda n : setattr(self, 'upn_suffix_column', n.get_str_value()),
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
        writer.write_str_value("aadUserIdColumn", self.aad_user_id_column)
        writer.write_str_value("dnsDomainColumn", self.dns_domain_column)
        writer.write_str_value("nameColumn", self.name_column)
        writer.write_str_value("ntDomainColumn", self.nt_domain_column)
        writer.write_str_value("sidColumn", self.sid_column)
        writer.write_str_value("upnColumn", self.upn_column)
        writer.write_str_value("upnSuffixColumn", self.upn_suffix_column)
    

