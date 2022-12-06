from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class EmployeeOrgData(AdditionalDataHolder, Parsable):
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
        Instantiates a new employeeOrgData and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cost center associated with the user. Returned only on $select. Supports $filter.
        self._cost_center: Optional[str] = None
        # The name of the division in which the user works. Returned only on $select. Supports $filter.
        self._division: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def cost_center(self,) -> Optional[str]:
        """
        Gets the costCenter property value. The cost center associated with the user. Returned only on $select. Supports $filter.
        Returns: Optional[str]
        """
        return self._cost_center
    
    @cost_center.setter
    def cost_center(self,value: Optional[str] = None) -> None:
        """
        Sets the costCenter property value. The cost center associated with the user. Returned only on $select. Supports $filter.
        Args:
            value: Value to set for the costCenter property.
        """
        self._cost_center = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmployeeOrgData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmployeeOrgData
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmployeeOrgData()
    
    @property
    def division(self,) -> Optional[str]:
        """
        Gets the division property value. The name of the division in which the user works. Returned only on $select. Supports $filter.
        Returns: Optional[str]
        """
        return self._division
    
    @division.setter
    def division(self,value: Optional[str] = None) -> None:
        """
        Sets the division property value. The name of the division in which the user works. Returned only on $select. Supports $filter.
        Args:
            value: Value to set for the division property.
        """
        self._division = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cost_center": lambda n : setattr(self, 'cost_center', n.get_str_value()),
            "division": lambda n : setattr(self, 'division', n.get_str_value()),
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
        writer.write_str_value("costCenter", self.cost_center)
        writer.write_str_value("division", self.division)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

