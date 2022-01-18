"""
Home Assistant component to monitor websites availability
https://github.com/bmelim/websitemonitor
"""

import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_URL, CONF_NAME
from homeassistant.helpers import config_validation as cv

from .const import DOMAIN, CONF_WEBSITES

_WEBSITES_SCHEMA = vol.All(
    cv.ensure_list,
    [
        vol.Schema(
            {vol.Optional(CONF_NAME): cv.string, vol.Required(CONF_URL): vol.Url()}
        )
    ],
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {vol.Required(CONF_WEBSITES): _WEBSITES_SCHEMA},
        ),
    },
    extra=vol.ALLOW_EXTRA,
)

PLATFORMS = ["binary_sensor"]


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up WebsiteMonitor integration."""
    for component in PLATFORMS:
        hass.async_create_task(
            hass.helpers.discovery.async_load_platform(
                component, DOMAIN, config.get(DOMAIN), config
            )
        )
    return True
