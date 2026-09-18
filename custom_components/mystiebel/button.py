"""Button platform for MyStiebel integration."""

import logging

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN, MOMENTARY_REGISTERS
from .sensor import MyStiebelBaseEntity

_LOGGER = logging.getLogger(__name__)


def _setup_button_entities(coordinator):
    params_to_check, fields_to_create = (
        coordinator.parameters,
        coordinator.active_fields,
    )
    buttons = []
    for idx in MOMENTARY_REGISTERS:
        if idx not in fields_to_create:
            continue
        param = params_to_check.get(idx)
        if param and "read_write" in param.get("access", []):
            buttons.append(MyStiebelButton(coordinator, idx, param))
    return buttons


async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    buttons = await hass.async_add_executor_job(_setup_button_entities, coordinator)
    async_add_entities(buttons, True)


class MyStiebelButton(MyStiebelBaseEntity, ButtonEntity):
    _attr_entity_registry_enabled_default = False

    def __init__(self, coordinator, register_index, param) -> None:
        super().__init__(coordinator, param)
        self._register_index = register_index
        self._attr_unique_id = f"mystiebel_{register_index}_button"
        self._attr_name = param.get("display_name")
        self._attr_icon = "mdi:filter-remove-outline"
        self._attr_entity_category = EntityCategory.CONFIG

    async def async_press(self) -> None:
        await self.coordinator.async_set_value(self._register_index, 1)
