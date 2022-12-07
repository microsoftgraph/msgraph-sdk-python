from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')

class SubjectRightsRequestDetail(AdditionalDataHolder, Parsable):
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
        Instantiates a new subjectRightsRequestDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Count of items that are excluded from the request.
        self._excluded_item_count: Optional[int] = None
        # Count of items per insight.
        self._insight_counts: Optional[List[key_value_pair.KeyValuePair]] = None
        # Count of items found.
        self._item_count: Optional[int] = None
        # Count of item that need review.
        self._item_need_review: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Count of items per product, such as Exchange, SharePoint, OneDrive, and Teams.
        self._product_item_counts: Optional[List[key_value_pair.KeyValuePair]] = None
        # Count of items signed off by the administrator.
        self._signed_off_item_count: Optional[int] = None
        # Total item size in bytes.
        self._total_item_size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectRightsRequestDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubjectRightsRequestDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubjectRightsRequestDetail()
    
    @property
    def excluded_item_count(self,) -> Optional[int]:
        """
        Gets the excludedItemCount property value. Count of items that are excluded from the request.
        Returns: Optional[int]
        """
        return self._excluded_item_count
    
    @excluded_item_count.setter
    def excluded_item_count(self,value: Optional[int] = None) -> None:
        """
        Sets the excludedItemCount property value. Count of items that are excluded from the request.
        Args:
            value: Value to set for the excludedItemCount property.
        """
        self._excluded_item_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "excluded_item_count": lambda n : setattr(self, 'excluded_item_count', n.get_int_value()),
            "insight_counts": lambda n : setattr(self, 'insight_counts', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "item_count": lambda n : setattr(self, 'item_count', n.get_int_value()),
            "item_need_review": lambda n : setattr(self, 'item_need_review', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "product_item_counts": lambda n : setattr(self, 'product_item_counts', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "signed_off_item_count": lambda n : setattr(self, 'signed_off_item_count', n.get_int_value()),
            "total_item_size": lambda n : setattr(self, 'total_item_size', n.get_int_value()),
        }
        return fields
    
    @property
    def insight_counts(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the insightCounts property value. Count of items per insight.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._insight_counts
    
    @insight_counts.setter
    def insight_counts(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the insightCounts property value. Count of items per insight.
        Args:
            value: Value to set for the insightCounts property.
        """
        self._insight_counts = value
    
    @property
    def item_count(self,) -> Optional[int]:
        """
        Gets the itemCount property value. Count of items found.
        Returns: Optional[int]
        """
        return self._item_count
    
    @item_count.setter
    def item_count(self,value: Optional[int] = None) -> None:
        """
        Sets the itemCount property value. Count of items found.
        Args:
            value: Value to set for the itemCount property.
        """
        self._item_count = value
    
    @property
    def item_need_review(self,) -> Optional[int]:
        """
        Gets the itemNeedReview property value. Count of item that need review.
        Returns: Optional[int]
        """
        return self._item_need_review
    
    @item_need_review.setter
    def item_need_review(self,value: Optional[int] = None) -> None:
        """
        Sets the itemNeedReview property value. Count of item that need review.
        Args:
            value: Value to set for the itemNeedReview property.
        """
        self._item_need_review = value
    
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
    def product_item_counts(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the productItemCounts property value. Count of items per product, such as Exchange, SharePoint, OneDrive, and Teams.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._product_item_counts
    
    @product_item_counts.setter
    def product_item_counts(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the productItemCounts property value. Count of items per product, such as Exchange, SharePoint, OneDrive, and Teams.
        Args:
            value: Value to set for the productItemCounts property.
        """
        self._product_item_counts = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("excludedItemCount", self.excluded_item_count)
        writer.write_collection_of_object_values("insightCounts", self.insight_counts)
        writer.write_int_value("itemCount", self.item_count)
        writer.write_int_value("itemNeedReview", self.item_need_review)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("productItemCounts", self.product_item_counts)
        writer.write_int_value("signedOffItemCount", self.signed_off_item_count)
        writer.write_int_value("totalItemSize", self.total_item_size)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def signed_off_item_count(self,) -> Optional[int]:
        """
        Gets the signedOffItemCount property value. Count of items signed off by the administrator.
        Returns: Optional[int]
        """
        return self._signed_off_item_count
    
    @signed_off_item_count.setter
    def signed_off_item_count(self,value: Optional[int] = None) -> None:
        """
        Sets the signedOffItemCount property value. Count of items signed off by the administrator.
        Args:
            value: Value to set for the signedOffItemCount property.
        """
        self._signed_off_item_count = value
    
    @property
    def total_item_size(self,) -> Optional[int]:
        """
        Gets the totalItemSize property value. Total item size in bytes.
        Returns: Optional[int]
        """
        return self._total_item_size
    
    @total_item_size.setter
    def total_item_size(self,value: Optional[int] = None) -> None:
        """
        Sets the totalItemSize property value. Total item size in bytes.
        Args:
            value: Value to set for the totalItemSize property.
        """
        self._total_item_size = value
    

