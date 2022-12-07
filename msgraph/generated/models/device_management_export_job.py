from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_export_job_localization_type = lazy_import('msgraph.generated.models.device_management_export_job_localization_type')
device_management_report_file_format = lazy_import('msgraph.generated.models.device_management_report_file_format')
device_management_report_status = lazy_import('msgraph.generated.models.device_management_report_status')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceManagementExportJob(entity.Entity):
    """
    Entity representing a job to export a report
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementExportJob and sets the default values.
        """
        super().__init__()
        # Time that the exported report expires
        self._expiration_date_time: Optional[datetime] = None
        # Filters applied on the report
        self._filter: Optional[str] = None
        # Possible values for the file format of a report
        self._format: Optional[device_management_report_file_format.DeviceManagementReportFileFormat] = None
        # Configures how the requested export job is localized
        self._localization_type: Optional[device_management_export_job_localization_type.DeviceManagementExportJobLocalizationType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Name of the report
        self._report_name: Optional[str] = None
        # Time that the exported report was requested
        self._request_date_time: Optional[datetime] = None
        # Columns selected from the report
        self._select: Optional[List[str]] = None
        # A snapshot is an identifiable subset of the dataset represented by the ReportName. A sessionId or CachedReportConfiguration id can be used here. If a sessionId is specified, Filter, Select, and OrderBy are applied to the data represented by the sessionId. Filter, Select, and OrderBy cannot be specified together with a CachedReportConfiguration id.
        self._snapshot_id: Optional[str] = None
        # Possible statuses associated with a generated report
        self._status: Optional[device_management_report_status.DeviceManagementReportStatus] = None
        # Temporary location of the exported report
        self._url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementExportJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementExportJob
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementExportJob()
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Time that the exported report expires
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Time that the exported report expires
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    @property
    def filter(self,) -> Optional[str]:
        """
        Gets the filter property value. Filters applied on the report
        Returns: Optional[str]
        """
        return self._filter
    
    @filter.setter
    def filter(self,value: Optional[str] = None) -> None:
        """
        Sets the filter property value. Filters applied on the report
        Args:
            value: Value to set for the filter property.
        """
        self._filter = value
    
    @property
    def format(self,) -> Optional[device_management_report_file_format.DeviceManagementReportFileFormat]:
        """
        Gets the format property value. Possible values for the file format of a report
        Returns: Optional[device_management_report_file_format.DeviceManagementReportFileFormat]
        """
        return self._format
    
    @format.setter
    def format(self,value: Optional[device_management_report_file_format.DeviceManagementReportFileFormat] = None) -> None:
        """
        Sets the format property value. Possible values for the file format of a report
        Args:
            value: Value to set for the format property.
        """
        self._format = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "filter": lambda n : setattr(self, 'filter', n.get_str_value()),
            "format": lambda n : setattr(self, 'format', n.get_enum_value(device_management_report_file_format.DeviceManagementReportFileFormat)),
            "localization_type": lambda n : setattr(self, 'localization_type', n.get_enum_value(device_management_export_job_localization_type.DeviceManagementExportJobLocalizationType)),
            "report_name": lambda n : setattr(self, 'report_name', n.get_str_value()),
            "request_date_time": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "select": lambda n : setattr(self, 'select', n.get_collection_of_primitive_values(str)),
            "snapshot_id": lambda n : setattr(self, 'snapshot_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(device_management_report_status.DeviceManagementReportStatus)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def localization_type(self,) -> Optional[device_management_export_job_localization_type.DeviceManagementExportJobLocalizationType]:
        """
        Gets the localizationType property value. Configures how the requested export job is localized
        Returns: Optional[device_management_export_job_localization_type.DeviceManagementExportJobLocalizationType]
        """
        return self._localization_type
    
    @localization_type.setter
    def localization_type(self,value: Optional[device_management_export_job_localization_type.DeviceManagementExportJobLocalizationType] = None) -> None:
        """
        Sets the localizationType property value. Configures how the requested export job is localized
        Args:
            value: Value to set for the localizationType property.
        """
        self._localization_type = value
    
    @property
    def report_name(self,) -> Optional[str]:
        """
        Gets the reportName property value. Name of the report
        Returns: Optional[str]
        """
        return self._report_name
    
    @report_name.setter
    def report_name(self,value: Optional[str] = None) -> None:
        """
        Sets the reportName property value. Name of the report
        Args:
            value: Value to set for the reportName property.
        """
        self._report_name = value
    
    @property
    def request_date_time(self,) -> Optional[datetime]:
        """
        Gets the requestDateTime property value. Time that the exported report was requested
        Returns: Optional[datetime]
        """
        return self._request_date_time
    
    @request_date_time.setter
    def request_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the requestDateTime property value. Time that the exported report was requested
        Args:
            value: Value to set for the requestDateTime property.
        """
        self._request_date_time = value
    
    @property
    def select(self,) -> Optional[List[str]]:
        """
        Gets the select property value. Columns selected from the report
        Returns: Optional[List[str]]
        """
        return self._select
    
    @select.setter
    def select(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the select property value. Columns selected from the report
        Args:
            value: Value to set for the select property.
        """
        self._select = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("filter", self.filter)
        writer.write_enum_value("format", self.format)
        writer.write_enum_value("localizationType", self.localization_type)
        writer.write_str_value("reportName", self.report_name)
        writer.write_datetime_value("requestDateTime", self.request_date_time)
        writer.write_collection_of_primitive_values("select", self.select)
        writer.write_str_value("snapshotId", self.snapshot_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("url", self.url)
    
    @property
    def snapshot_id(self,) -> Optional[str]:
        """
        Gets the snapshotId property value. A snapshot is an identifiable subset of the dataset represented by the ReportName. A sessionId or CachedReportConfiguration id can be used here. If a sessionId is specified, Filter, Select, and OrderBy are applied to the data represented by the sessionId. Filter, Select, and OrderBy cannot be specified together with a CachedReportConfiguration id.
        Returns: Optional[str]
        """
        return self._snapshot_id
    
    @snapshot_id.setter
    def snapshot_id(self,value: Optional[str] = None) -> None:
        """
        Sets the snapshotId property value. A snapshot is an identifiable subset of the dataset represented by the ReportName. A sessionId or CachedReportConfiguration id can be used here. If a sessionId is specified, Filter, Select, and OrderBy are applied to the data represented by the sessionId. Filter, Select, and OrderBy cannot be specified together with a CachedReportConfiguration id.
        Args:
            value: Value to set for the snapshotId property.
        """
        self._snapshot_id = value
    
    @property
    def status(self,) -> Optional[device_management_report_status.DeviceManagementReportStatus]:
        """
        Gets the status property value. Possible statuses associated with a generated report
        Returns: Optional[device_management_report_status.DeviceManagementReportStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[device_management_report_status.DeviceManagementReportStatus] = None) -> None:
        """
        Sets the status property value. Possible statuses associated with a generated report
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. Temporary location of the exported report
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. Temporary location of the exported report
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    

