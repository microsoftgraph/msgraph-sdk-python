from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_identifier = lazy_import('msgraph.generated.models.mobile_app_identifier')

class ManagedAppPolicyDeploymentSummaryPerApp(AdditionalDataHolder, Parsable):
    """
    Represents policy deployment summary per app.
    """
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
    
    @property
    def configuration_applied_user_count(self,) -> Optional[int]:
        """
        Gets the configurationAppliedUserCount property value. Number of users the policy is applied.
        Returns: Optional[int]
        """
        return self._configuration_applied_user_count
    
    @configuration_applied_user_count.setter
    def configuration_applied_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the configurationAppliedUserCount property value. Number of users the policy is applied.
        Args:
            value: Value to set for the configurationAppliedUserCount property.
        """
        self._configuration_applied_user_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedAppPolicyDeploymentSummaryPerApp and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Number of users the policy is applied.
        self._configuration_applied_user_count: Optional[int] = None
        # Deployment of an app.
        self._mobile_app_identifier: Optional[mobile_app_identifier.MobileAppIdentifier] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppPolicyDeploymentSummaryPerApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppPolicyDeploymentSummaryPerApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAppPolicyDeploymentSummaryPerApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration_applied_user_count": lambda n : setattr(self, 'configuration_applied_user_count', n.get_int_value()),
            "mobile_app_identifier": lambda n : setattr(self, 'mobile_app_identifier', n.get_object_value(mobile_app_identifier.MobileAppIdentifier)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def mobile_app_identifier(self,) -> Optional[mobile_app_identifier.MobileAppIdentifier]:
        """
        Gets the mobileAppIdentifier property value. Deployment of an app.
        Returns: Optional[mobile_app_identifier.MobileAppIdentifier]
        """
        return self._mobile_app_identifier
    
    @mobile_app_identifier.setter
    def mobile_app_identifier(self,value: Optional[mobile_app_identifier.MobileAppIdentifier] = None) -> None:
        """
        Sets the mobileAppIdentifier property value. Deployment of an app.
        Args:
            value: Value to set for the mobileAppIdentifier property.
        """
        self._mobile_app_identifier = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("configurationAppliedUserCount", self.configuration_applied_user_count)
        writer.write_object_value("mobileAppIdentifier", self.mobile_app_identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

