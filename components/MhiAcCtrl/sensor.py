import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    DEVICE_CLASS_FREQUENCY,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_CELSIUS,
    UNIT_PERCENT,
    UNIT_HOUR,
    UNIT_HERTZ,
    UNIT_AMPERE,
    ICON_THERMOMETER,
    ICON_FAN,
    ICON_TIMER,
)
from . import MhiAcCtrl, CONF_MHI_AC_CTRL_ID

CONF_ERROR_CODE = "error_code"
CONF_OUTDOOR_TEMPERATURE = "outdoor_temperature"
CONF_RETURN_AIR_TEMPERATURE = "return_air_temperature"
CONF_OUTDOOR_UNIT_FAN_SPEED = "outdoor_unit_fan_speed"
CONF_INDOOR_UNIT_FAN_SPEED = "indoor_unit_fan_speed"
CONF_COMPRESSOR_FREQUENCY = "compressor_frequency"
CONF_INDOOR_UNIT_TOTAL_RUN_TIME = "indoor_unit_total_run_time"
CONF_COMPRESSOR_TOTAL_RUN_TIME = "compressor_total_run_time"
CONF_CURRENT_POWER = "current_power"
CONF_VANES_POS = "vanes_pos"
CONF_VANES_POS_OLD = "vanes_pos_old"
CONF_ENERGY_USED = "energy_used"
CONF_INDOOR_UNIT_THI_R1 = "indoor_unit_thi_r1"
CONF_INDOOR_UNIT_THI_R2 = "indoor_unit_thi_r2"
CONF_INDOOR_UNIT_THI_R3 = "indoor_unit_thi_r3"
CONF_OUTDOOR_UNIT_THO_R1 = "outdoor_unit_tho_r1"
CONF_OUTDOOR_UNIT_EXPANSION_VALVE = "outdoor_unit_expansion_valve"
CONF_OUTDOOR_UNIT_DISCHARGE_PIPE = "outdoor_unit_discharge_pipe"
CONF_OUTDOOR_UNIT_DISCHARGE_PIPE_SUPER_HEAT = "outdoor_unit_discharge_pipe_super_heat"
CONF_PROTECTION_STATE_NUMBER = "protection_state_number"
CONF_VANESLR_POS = "vanesLR_pos"
CONF_VANESLR_POS_OLD = "vanesLR_pos_old"
CONF_THREED_AUTO = "threeD_auto_enabled"

ICON_SINE = "mdi:sine-wave"

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(MhiAcCtrl),
    cv.GenerateID(CONF_MHI_AC_CTRL_ID): cv.use_id(MhiAcCtrl),
    cv.Optional(CONF_ERROR_CODE): sensor.sensor_schema(
    ),
    cv.Optional(CONF_OUTDOOR_TEMPERATURE): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        icon = ICON_THERMOMETER,
    ),
    cv.Optional(CONF_RETURN_AIR_TEMPERATURE): sensor.sensor_schema(
        unit_of_measurement=UNIT_CELSIUS,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_TEMPERATURE,
        state_class=STATE_CLASS_MEASUREMENT,
        icon = ICON_THERMOMETER,
    ),
    cv.Optional(CONF_OUTDOOR_UNIT_FAN_SPEED): sensor.sensor_schema(
        icon = ICON_FAN,
    ),
    cv.Optional(CONF_INDOOR_UNIT_FAN_SPEED): sensor.sensor_schema(
        icon = ICON_FAN,
    ),
    cv.Optional(CONF_COMPRESSOR_FREQUENCY): sensor.sensor_schema(
        icon = ICON_SINE,
        unit_of_measurement=UNIT_HERTZ ,
        accuracy_decimals=1,
        device_class=DEVICE_CLASS_FREQUENCY ,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_INDOOR_UNIT_TOTAL_RUN_TIME): sensor.sensor_schema(
        icon=ICON_TIMER,
        unit_of_measurement=UNIT_HOUR,
        accuracy_decimals=1,
        state_class=STATE_CLASS_TOTAL_INCREASING ,
    ),
    cv.Optional(CONF_COMPRESSOR_TOTAL_RUN_TIME): sensor.sensor_schema(
        icon=ICON_TIMER,
        unit_of_measurement=UNIT_HOUR,
        accuracy_decimals=1,
        state_class=STATE_CLASS_TOTAL_INCREASING ,
    ),
    cv.Optional(CONF_CURRENT_POWER): sensor.sensor_schema(
        unit_of_measurement=UNIT_AMPERE,
        accuracy_decimals=2,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    cv.Optional(CONF_VANES_POS): sensor.sensor_schema(
    ),
    cv.Optional(CONF_VANES_POS_OLD): sensor.sensor_schema(
    ),
    cv.Optional(CONF_ENERGY_USED): sensor.sensor_schema(
    ),
    cv.Optional(CONF_INDOOR_UNIT_THI_R1): sensor.sensor_schema(
    ),
    cv.Optional(CONF_INDOOR_UNIT_THI_R2): sensor.sensor_schema(
    ),
    cv.Optional(CONF_INDOOR_UNIT_THI_R3): sensor.sensor_schema(
    ),
    cv.Optional(CONF_OUTDOOR_UNIT_THO_R1): sensor.sensor_schema(
    ),
    cv.Optional(CONF_OUTDOOR_UNIT_EXPANSION_VALVE): sensor.sensor_schema(
    ),
    cv.Optional(CONF_OUTDOOR_UNIT_DISCHARGE_PIPE): sensor.sensor_schema(
    ),
    cv.Optional(CONF_OUTDOOR_UNIT_DISCHARGE_PIPE_SUPER_HEAT): sensor.sensor_schema(
    ),
    cv.Optional(CONF_PROTECTION_STATE_NUMBER): sensor.sensor_schema(
    ),
    cv.Optional(CONF_VANESLR_POS): sensor.sensor_schema(
    ),
    cv.Optional(CONF_VANESLR_POS_OLD): sensor.sensor_schema(
    ),
    cv.Optional(CONF_THREED_AUTO): sensor.sensor_schema(
    ),
})


async def to_code(config):
    mhi = await cg.get_variable(config[CONF_MHI_AC_CTRL_ID])

    if CONF_ERROR_CODE in config:
        conf = config[CONF_ERROR_CODE]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_error_code(sens))
    if CONF_OUTDOOR_TEMPERATURE in config:
        conf = config[CONF_OUTDOOR_TEMPERATURE]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_outdoor_temperature(sens))
    if CONF_RETURN_AIR_TEMPERATURE in config:
        conf = config[CONF_RETURN_AIR_TEMPERATURE]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_return_air_temperature(sens))
    if CONF_OUTDOOR_UNIT_FAN_SPEED in config:
        conf = config[CONF_OUTDOOR_UNIT_FAN_SPEED]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_outdoor_unit_fan_speed(sens))
    if CONF_INDOOR_UNIT_FAN_SPEED in config:
        conf = config[CONF_INDOOR_UNIT_FAN_SPEED]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_indoor_unit_fan_speed(sens))
    if CONF_COMPRESSOR_FREQUENCY in config:
        conf = config[CONF_COMPRESSOR_FREQUENCY]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_compressor_frequency(sens))
    if CONF_INDOOR_UNIT_TOTAL_RUN_TIME in config:
        conf = config[CONF_INDOOR_UNIT_TOTAL_RUN_TIME]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_indoor_unit_total_run_time(sens))
    if CONF_COMPRESSOR_TOTAL_RUN_TIME in config:
        conf = config[CONF_COMPRESSOR_TOTAL_RUN_TIME]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_compressor_total_run_time(sens))
    if CONF_CURRENT_POWER in config:
        conf = config[CONF_CURRENT_POWER]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_current_power(sens))
    if CONF_VANES_POS in config:
        conf = config[CONF_VANES_POS]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_vanes_pos(sens))
    if CONF_VANES_POS_OLD in config:
        conf = config[CONF_VANES_POS_OLD]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_vanes_pos_old(sens))
    if CONF_ENERGY_USED in config:
        conf = config[CONF_ENERGY_USED]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_energy_used(sens))
    if CONF_INDOOR_UNIT_THI_R1 in config:
        conf = config[CONF_INDOOR_UNIT_THI_R1]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_indoor_unit_thi_r1(sens))
    if CONF_INDOOR_UNIT_THI_R2 in config:
        conf = config[CONF_INDOOR_UNIT_THI_R2]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_indoor_unit_thi_r2(sens))
    if CONF_INDOOR_UNIT_THI_R3 in config:
        conf = config[CONF_INDOOR_UNIT_THI_R3]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_indoor_unit_thi_r3(sens))
    if CONF_OUTDOOR_UNIT_THO_R1 in config:
        conf = config[CONF_OUTDOOR_UNIT_THO_R1]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_outdoor_unit_tho_r1(sens))
    if CONF_OUTDOOR_UNIT_EXPANSION_VALVE in config:
        conf = config[CONF_OUTDOOR_UNIT_EXPANSION_VALVE]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_outdoor_unit_expansion_valve(sens))
    if CONF_OUTDOOR_UNIT_DISCHARGE_PIPE in config:
        conf = config[CONF_OUTDOOR_UNIT_DISCHARGE_PIPE]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_outdoor_unit_discharge_pipe(sens))
    if CONF_OUTDOOR_UNIT_DISCHARGE_PIPE_SUPER_HEAT in config:
        conf = config[CONF_OUTDOOR_UNIT_DISCHARGE_PIPE_SUPER_HEAT]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_outdoor_unit_discharge_pipe_super_heat(sens))
    if CONF_PROTECTION_STATE_NUMBER in config:
        conf = config[CONF_PROTECTION_STATE_NUMBER]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_protection_state_number(sens))
    if CONF_VANESLR_POS in config:
        conf = config[CONF_VANESLR_POS]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_vanesLR_pos(sens))
    if CONF_VANESLR_POS_OLD in config:
        conf = config[CONF_VANESLR_POS_OLD]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_vanesLR_pos_old(sens))
    if CONF_THREED_AUTO in config:
        conf = config[CONF_THREED_AUTO]
        sens = await sensor.new_sensor(conf)
        cg.add(mhi.set_threeD_auto_enabled(sens))