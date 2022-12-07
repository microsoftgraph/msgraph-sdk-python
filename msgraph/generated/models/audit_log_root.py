from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_audit = lazy_import('msgraph.generated.models.directory_audit')
entity = lazy_import('msgraph.generated.models.entity')
provisioning_object_summary = lazy_import('msgraph.generated.models.provisioning_object_summary')
sign_in = lazy_import('msgraph.generated.models.sign_in')

class AuditLogRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuditLogRoot and sets the default values.
        """
        super().__init__()
        # The directoryAudits property
        self._directory_audits: Optional[List[directory_audit.DirectoryAudit]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The provisioning property
        self._provisioning: Optional[List[provisioning_object_summary.ProvisioningObjectSummary]] = None
        # The signIns property
        self._sign_ins: Optional[List[sign_in.SignIn]] = None
    
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
    
    @property
    def directory_audits(self,) -> Optional[List[directory_audit.DirectoryAudit]]:
        """
        Gets the directoryAudits property value. The directoryAudits property
        Returns: Optional[List[directory_audit.DirectoryAudit]]
        """
        return self._directory_audits
    
    @directory_audits.setter
    def directory_audits(self,value: Optional[List[directory_audit.DirectoryAudit]] = None) -> None:
        """
        Sets the directoryAudits property value. The directoryAudits property
        Args:
            value: Value to set for the directoryAudits property.
        """
        self._directory_audits = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "directory_audits": lambda n : setattr(self, 'directory_audits', n.get_collection_of_object_values(directory_audit.DirectoryAudit)),
            "provisioning": lambda n : setattr(self, 'provisioning', n.get_collection_of_object_values(provisioning_object_summary.ProvisioningObjectSummary)),
            "sign_ins": lambda n : setattr(self, 'sign_ins', n.get_collection_of_object_values(sign_in.SignIn)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def provisioning(self,) -> Optional[List[provisioning_object_summary.ProvisioningObjectSummary]]:
        """
        Gets the provisioning property value. The provisioning property
        Returns: Optional[List[provisioning_object_summary.ProvisioningObjectSummary]]
        """
        return self._provisioning
    
    @provisioning.setter
    def provisioning(self,value: Optional[List[provisioning_object_summary.ProvisioningObjectSummary]] = None) -> None:
        """
        Sets the provisioning property value. The provisioning property
        Args:
            value: Value to set for the provisioning property.
        """
        self._provisioning = value
    
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
    
    @property
    def sign_ins(self,) -> Optional[List[sign_in.SignIn]]:
        """
        Gets the signIns property value. The signIns property
        Returns: Optional[List[sign_in.SignIn]]
        """
        return self._sign_ins
    
    @sign_ins.setter
    def sign_ins(self,value: Optional[List[sign_in.SignIn]] = None) -> None:
        """
        Sets the signIns property value. The signIns property
        Args:
            value: Value to set for the signIns property.
        """
        self._sign_ins = value
    

