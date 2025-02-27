import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor

from . import MhiAcCtrl, CONF_MHI_AC_CTRL_ID

CONF_DEFROST = "defrost"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(MhiAcCtrl),
    cv.GenerateID(CONF_MHI_AC_CTRL_ID): cv.use_id(MhiAcCtrl),
    cv.Optional(CONF_DEFROST): binary_sensor.binary_sensor_schema(
    ),
})


async def to_code(config):
    mhi = await cg.get_variable(config[CONF_MHI_AC_CTRL_ID])

    if CONF_DEFROST in config:
        conf = config[CONF_DEFROST]
        sens = await binary_sensor.new_binary_sensor(conf)
        cg.add(mhi.set_defrost(sens))