from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_audit import DirectoryAudit
    from .entity import Entity
    from .provisioning_object_summary import ProvisioningObjectSummary
    from .sign_in import SignIn

from .entity import Entity

@dataclass
class AuditLogRoot(Entity, Parsable):
    # The directoryAudits property
    directory_audits: Optional[list[DirectoryAudit]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The provisioning property
    provisioning: Optional[list[ProvisioningObjectSummary]] = None
    # The signIns property
    sign_ins: Optional[list[SignIn]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditLogRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditLogRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditLogRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_audit import DirectoryAudit
        from .entity import Entity
        from .provisioning_object_summary import ProvisioningObjectSummary
        from .sign_in import SignIn

        from .directory_audit import DirectoryAudit
        from .entity import Entity
        from .provisioning_object_summary import ProvisioningObjectSummary
        from .sign_in import SignIn

        fields: dict[str, Callable[[Any], None]] = {
            "directoryAudits": lambda n : setattr(self, 'directory_audits', n.get_collection_of_object_values(DirectoryAudit)),
            "provisioning": lambda n : setattr(self, 'provisioning', n.get_collection_of_object_values(ProvisioningObjectSummary)),
            "signIns": lambda n : setattr(self, 'sign_ins', n.get_collection_of_object_values(SignIn)),
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
        writer.write_collection_of_object_values("directoryAudits", self.directory_audits)
        writer.write_collection_of_object_values("provisioning", self.provisioning)
        writer.write_collection_of_object_values("signIns", self.sign_ins)
    

