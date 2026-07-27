from typing import Union, Tuple, Dict

from .service_definition import ServiceDefinition
from .service_runtime_state import ServiceRuntimeState
from .tray_menu_item_data import TrayMenuItemData
from .tray_menu_separator_data import TrayMenuSeparatorData

ServiceRecord = Tuple[ServiceDefinition, ServiceRuntimeState]
ServiceRegistry = Dict[str, ServiceRecord]
TrayItem = Union[TrayMenuItemData, TrayMenuSeparatorData]
