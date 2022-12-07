from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

rbac_application = lazy_import('msgraph.generated.models.rbac_application')

class RoleManagement(AdditionalDataHolder, Parsable):
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
        Instantiates a new RoleManagement and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The directory property
        self._directory: Optional[rbac_application.RbacApplication] = None
        # Container for roles and assignments for entitlement management resources.
        self._entitlement_management: Optional[rbac_application.RbacApplication] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleManagement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleManagement()
    
    @property
    def directory(self,) -> Optional[rbac_application.RbacApplication]:
        """
        Gets the directory property value. The directory property
        Returns: Optional[rbac_application.RbacApplication]
        """
        return self._directory
    
    @directory.setter
    def directory(self,value: Optional[rbac_application.RbacApplication] = None) -> None:
        """
        Sets the directory property value. The directory property
        Args:
            value: Value to set for the directory property.
        """
        self._directory = value
    
    @property
    def entitlement_management(self,) -> Optional[rbac_application.RbacApplication]:
        """
        Gets the entitlementManagement property value. Container for roles and assignments for entitlement management resources.
        Returns: Optional[rbac_application.RbacApplication]
        """
        return self._entitlement_management
    
    @entitlement_management.setter
    def entitlement_management(self,value: Optional[rbac_application.RbacApplication] = None) -> None:
        """
        Sets the entitlementManagement property value. Container for roles and assignments for entitlement management resources.
        Args:
            value: Value to set for the entitlementManagement property.
        """
        self._entitlement_management = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "directory": lambda n : setattr(self, 'directory', n.get_object_value(rbac_application.RbacApplication)),
            "entitlement_management": lambda n : setattr(self, 'entitlement_management', n.get_object_value(rbac_application.RbacApplication)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("directory", self.directory)
        writer.write_object_value("entitlementManagement", self.entitlement_management)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

