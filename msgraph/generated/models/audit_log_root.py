from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_audit, entity, provisioning_object_summary, sign_in

from . import entity

@dataclass
class AuditLogRoot(entity.Entity):
    # The directoryAudits property
    directory_audits: Optional[List[directory_audit.DirectoryAudit]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The provisioning property
    provisioning: Optional[List[provisioning_object_summary.ProvisioningObjectSummary]] = None
    # The signIns property
    sign_ins: Optional[List[sign_in.SignIn]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditLogRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditLogRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuditLogRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_audit, entity, provisioning_object_summary, sign_in

        fields: Dict[str, Callable[[Any], None]] = {
            "directoryAudits": lambda n : setattr(self, 'directory_audits', n.get_collection_of_object_values(directory_audit.DirectoryAudit)),
            "provisioning": lambda n : setattr(self, 'provisioning', n.get_collection_of_object_values(provisioning_object_summary.ProvisioningObjectSummary)),
            "signIns": lambda n : setattr(self, 'sign_ins', n.get_collection_of_object_values(sign_in.SignIn)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("directoryAudits", self.directory_audits)
        writer.write_collection_of_object_values("provisioning", self.provisioning)
        writer.write_collection_of_object_values("signIns", self.sign_ins)
    

