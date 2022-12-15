from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

evidence_remediation_status = lazy_import('msgraph.generated.models.security.evidence_remediation_status')
evidence_role = lazy_import('msgraph.generated.models.security.evidence_role')
evidence_verdict = lazy_import('msgraph.generated.models.security.evidence_verdict')

class AlertEvidence(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new alertEvidence and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The time the evidence was created and added to the alert.
        self._created_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The remediationStatus property
        self._remediation_status: Optional[evidence_remediation_status.EvidenceRemediationStatus] = None
        # Details about the remediation status.
        self._remediation_status_details: Optional[str] = None
        # The role/s that an evidence entity represents in an alert, e.g., an IP address that is associated with an attacker will have the evidence role 'Attacker'.
        self._roles: Optional[List[evidence_role.EvidenceRole]] = None
        # Array of custom tags associated with an evidence instance, for example to denote a group of devices, high value assets, etc.
        self._tags: Optional[List[str]] = None
        # The verdict property
        self._verdict: Optional[evidence_verdict.EvidenceVerdict] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The time the evidence was created and added to the alert.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The time the evidence was created and added to the alert.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlertEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlertEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remediation_status": lambda n : setattr(self, 'remediation_status', n.get_enum_value(evidence_remediation_status.EvidenceRemediationStatus)),
            "remediation_status_details": lambda n : setattr(self, 'remediation_status_details', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_enum_values(evidence_role.EvidenceRole)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "verdict": lambda n : setattr(self, 'verdict', n.get_enum_value(evidence_verdict.EvidenceVerdict)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def remediation_status(self,) -> Optional[evidence_remediation_status.EvidenceRemediationStatus]:
        """
        Gets the remediationStatus property value. The remediationStatus property
        Returns: Optional[evidence_remediation_status.EvidenceRemediationStatus]
        """
        return self._remediation_status
    
    @remediation_status.setter
    def remediation_status(self,value: Optional[evidence_remediation_status.EvidenceRemediationStatus] = None) -> None:
        """
        Sets the remediationStatus property value. The remediationStatus property
        Args:
            value: Value to set for the remediationStatus property.
        """
        self._remediation_status = value
    
    @property
    def remediation_status_details(self,) -> Optional[str]:
        """
        Gets the remediationStatusDetails property value. Details about the remediation status.
        Returns: Optional[str]
        """
        return self._remediation_status_details
    
    @remediation_status_details.setter
    def remediation_status_details(self,value: Optional[str] = None) -> None:
        """
        Sets the remediationStatusDetails property value. Details about the remediation status.
        Args:
            value: Value to set for the remediationStatusDetails property.
        """
        self._remediation_status_details = value
    
    @property
    def roles(self,) -> Optional[List[evidence_role.EvidenceRole]]:
        """
        Gets the roles property value. The role/s that an evidence entity represents in an alert, e.g., an IP address that is associated with an attacker will have the evidence role 'Attacker'.
        Returns: Optional[List[evidence_role.EvidenceRole]]
        """
        return self._roles
    
    @roles.setter
    def roles(self,value: Optional[List[evidence_role.EvidenceRole]] = None) -> None:
        """
        Sets the roles property value. The role/s that an evidence entity represents in an alert, e.g., an IP address that is associated with an attacker will have the evidence role 'Attacker'.
        Args:
            value: Value to set for the roles property.
        """
        self._roles = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("remediationStatus", self.remediation_status)
        writer.write_str_value("remediationStatusDetails", self.remediation_status_details)
        writer.write_enum_value("roles", self.roles)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_enum_value("verdict", self.verdict)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. Array of custom tags associated with an evidence instance, for example to denote a group of devices, high value assets, etc.
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. Array of custom tags associated with an evidence instance, for example to denote a group of devices, high value assets, etc.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def verdict(self,) -> Optional[evidence_verdict.EvidenceVerdict]:
        """
        Gets the verdict property value. The verdict property
        Returns: Optional[evidence_verdict.EvidenceVerdict]
        """
        return self._verdict
    
    @verdict.setter
    def verdict(self,value: Optional[evidence_verdict.EvidenceVerdict] = None) -> None:
        """
        Sets the verdict property value. The verdict property
        Args:
            value: Value to set for the verdict property.
        """
        self._verdict = value
    

