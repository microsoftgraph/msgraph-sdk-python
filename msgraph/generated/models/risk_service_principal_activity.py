from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import risk_detail

class RiskServicePrincipalActivity(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new riskServicePrincipalActivity and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: none, hidden, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal.
        self._detail: Optional[risk_detail.RiskDetail] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The riskEventTypes property
        self._risk_event_types: Optional[List[str]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RiskServicePrincipalActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RiskServicePrincipalActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RiskServicePrincipalActivity()
    
    @property
    def detail(self,) -> Optional[risk_detail.RiskDetail]:
        """
        Gets the detail property value. Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: none, hidden, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal.
        Returns: Optional[risk_detail.RiskDetail]
        """
        return self._detail
    
    @detail.setter
    def detail(self,value: Optional[risk_detail.RiskDetail] = None) -> None:
        """
        Sets the detail property value. Details of the detected risk. Note: Details for this property are only available for Workload Identities Premium customers. Events in tenants without this license will be returned hidden. The possible values are: none, hidden, adminConfirmedServicePrincipalCompromised, adminDismissedAllRiskForServicePrincipal. Note that you must use the Prefer: include-unknown-enum-members request header to get the following value(s) in this evolvable enum: adminConfirmedServicePrincipalCompromised , adminDismissedAllRiskForServicePrincipal.
        Args:
            value: Value to set for the detail property.
        """
        self._detail = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import risk_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "detail": lambda n : setattr(self, 'detail', n.get_enum_value(risk_detail.RiskDetail)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskEventTypes": lambda n : setattr(self, 'risk_event_types', n.get_collection_of_primitive_values(str)),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def risk_event_types(self,) -> Optional[List[str]]:
        """
        Gets the riskEventTypes property value. The riskEventTypes property
        Returns: Optional[List[str]]
        """
        return self._risk_event_types
    
    @risk_event_types.setter
    def risk_event_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the riskEventTypes property value. The riskEventTypes property
        Args:
            value: Value to set for the risk_event_types property.
        """
        self._risk_event_types = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("detail", self.detail)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("riskEventTypes", self.risk_event_types)
        writer.write_additional_data_value(self.additional_data)
    

