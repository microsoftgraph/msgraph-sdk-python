from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

risk_detection = lazy_import('msgraph.generated.models.risk_detection')
risky_user = lazy_import('msgraph.generated.models.risky_user')

class IdentityProtectionRoot(AdditionalDataHolder, Parsable):
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
        Instantiates a new IdentityProtectionRoot and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Risk detection in Azure AD Identity Protection and the associated information about the detection.
        self._risk_detections: Optional[List[risk_detection.RiskDetection]] = None
        # Users that are flagged as at-risk by Azure AD Identity Protection.
        self._risky_users: Optional[List[risky_user.RiskyUser]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityProtectionRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityProtectionRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentityProtectionRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "risk_detections": lambda n : setattr(self, 'risk_detections', n.get_collection_of_object_values(risk_detection.RiskDetection)),
            "risky_users": lambda n : setattr(self, 'risky_users', n.get_collection_of_object_values(risky_user.RiskyUser)),
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
    def risk_detections(self,) -> Optional[List[risk_detection.RiskDetection]]:
        """
        Gets the riskDetections property value. Risk detection in Azure AD Identity Protection and the associated information about the detection.
        Returns: Optional[List[risk_detection.RiskDetection]]
        """
        return self._risk_detections
    
    @risk_detections.setter
    def risk_detections(self,value: Optional[List[risk_detection.RiskDetection]] = None) -> None:
        """
        Sets the riskDetections property value. Risk detection in Azure AD Identity Protection and the associated information about the detection.
        Args:
            value: Value to set for the riskDetections property.
        """
        self._risk_detections = value
    
    @property
    def risky_users(self,) -> Optional[List[risky_user.RiskyUser]]:
        """
        Gets the riskyUsers property value. Users that are flagged as at-risk by Azure AD Identity Protection.
        Returns: Optional[List[risky_user.RiskyUser]]
        """
        return self._risky_users
    
    @risky_users.setter
    def risky_users(self,value: Optional[List[risky_user.RiskyUser]] = None) -> None:
        """
        Sets the riskyUsers property value. Users that are flagged as at-risk by Azure AD Identity Protection.
        Args:
            value: Value to set for the riskyUsers property.
        """
        self._risky_users = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("riskDetections", self.risk_detections)
        writer.write_collection_of_object_values("riskyUsers", self.risky_users)
        writer.write_additional_data_value(self.additional_data)
    

