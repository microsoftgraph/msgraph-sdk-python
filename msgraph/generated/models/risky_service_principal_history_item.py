from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

risk_service_principal_activity = lazy_import('msgraph.generated.models.risk_service_principal_activity')
risky_service_principal = lazy_import('msgraph.generated.models.risky_service_principal')

class RiskyServicePrincipalHistoryItem(risky_service_principal.RiskyServicePrincipal):
    """
    Provides operations to manage the collection of agreementAcceptance entities.
    """
    @property
    def activity(self,) -> Optional[risk_service_principal_activity.RiskServicePrincipalActivity]:
        """
        Gets the activity property value. The activity related to service principal risk level change.
        Returns: Optional[risk_service_principal_activity.RiskServicePrincipalActivity]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[risk_service_principal_activity.RiskServicePrincipalActivity] = None) -> None:
        """
        Sets the activity property value. The activity related to service principal risk level change.
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new riskyServicePrincipalHistoryItem and sets the default values.
        """
        super().__init__()
        # The activity related to service principal risk level change.
        self._activity: Optional[risk_service_principal_activity.RiskServicePrincipalActivity] = None
        # The identifier of the actor of the operation.
        self._initiated_by: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RiskyServicePrincipalHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RiskyServicePrincipalHistoryItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RiskyServicePrincipalHistoryItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(risk_service_principal_activity.RiskServicePrincipalActivity)),
            "initiated_by": lambda n : setattr(self, 'initiated_by', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiated_by(self,) -> Optional[str]:
        """
        Gets the initiatedBy property value. The identifier of the actor of the operation.
        Returns: Optional[str]
        """
        return self._initiated_by
    
    @initiated_by.setter
    def initiated_by(self,value: Optional[str] = None) -> None:
        """
        Sets the initiatedBy property value. The identifier of the actor of the operation.
        Args:
            value: Value to set for the initiatedBy property.
        """
        self._initiated_by = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("activity", self.activity)
        writer.write_str_value("initiatedBy", self.initiated_by)
    

