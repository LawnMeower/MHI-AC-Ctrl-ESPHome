import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor

from . import MhiAcCtrl, CONF_MHI_AC_CTRL_ID

CONF_PROTECTION_STATE = "protection_state"

ICON_ALERT_OUTLINE = "mdi:shield-alert-outline"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(MhiAcCtrl),
    cv.GenerateID(CONF_MHI_AC_CTRL_ID): cv.use_id(MhiAcCtrl),
    cv.Optional(CONF_PROTECTION_STATE): text_sensor.text_sensor_schema(
        icon=ICON_ALERT_OUTLINE,
    ),
})


async def to_code(config):
    mhi = await cg.get_variable(config[CONF_MHI_AC_CTRL_ID])

    if CONF_PROTECTION_STATE in config:
        conf = config[CONF_PROTECTION_STATE]
        sens = await text_sensor.new_text_sensor(conf)
        cg.add(mhi.set_protection_state(sens))