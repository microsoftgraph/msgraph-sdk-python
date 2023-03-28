from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delegated_admin_access_container_type

class DelegatedAdminAccessContainer(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new delegatedAdminAccessContainer and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identifier of the access container (for example, a security group). For 'securityGroup' access containers, this must be a valid ID of an Azure AD security group in the Microsoft partner's tenant.
        self._access_container_id: Optional[str] = None
        # The accessContainerType property
        self._access_container_type: Optional[delegated_admin_access_container_type.DelegatedAdminAccessContainerType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def access_container_id(self,) -> Optional[str]:
        """
        Gets the accessContainerId property value. The identifier of the access container (for example, a security group). For 'securityGroup' access containers, this must be a valid ID of an Azure AD security group in the Microsoft partner's tenant.
        Returns: Optional[str]
        """
        return self._access_container_id
    
    @access_container_id.setter
    def access_container_id(self,value: Optional[str] = None) -> None:
        """
        Sets the accessContainerId property value. The identifier of the access container (for example, a security group). For 'securityGroup' access containers, this must be a valid ID of an Azure AD security group in the Microsoft partner's tenant.
        Args:
            value: Value to set for the access_container_id property.
        """
        self._access_container_id = value
    
    @property
    def access_container_type(self,) -> Optional[delegated_admin_access_container_type.DelegatedAdminAccessContainerType]:
        """
        Gets the accessContainerType property value. The accessContainerType property
        Returns: Optional[delegated_admin_access_container_type.DelegatedAdminAccessContainerType]
        """
        return self._access_container_type
    
    @access_container_type.setter
    def access_container_type(self,value: Optional[delegated_admin_access_container_type.DelegatedAdminAccessContainerType] = None) -> None:
        """
        Sets the accessContainerType property value. The accessContainerType property
        Args:
            value: Value to set for the access_container_type property.
        """
        self._access_container_type = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminAccessContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminAccessContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DelegatedAdminAccessContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delegated_admin_access_container_type

        fields: Dict[str, Callable[[Any], None]] = {
            "accessContainerId": lambda n : setattr(self, 'access_container_id', n.get_str_value()),
            "accessContainerType": lambda n : setattr(self, 'access_container_type', n.get_enum_value(delegated_admin_access_container_type.DelegatedAdminAccessContainerType)),
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("accessContainerId", self.access_container_id)
        writer.write_enum_value("accessContainerType", self.access_container_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

