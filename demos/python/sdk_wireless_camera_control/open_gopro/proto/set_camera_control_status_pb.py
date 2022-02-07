# set_camera_control_status_pb.py/Open GoPro, Version 2.0 (C) Copyright 2021 GoPro, Inc. (http://gopro.com/OpenGoPro).
# This copyright was auto-generated on Sat Feb  5 00:21:38 UTC 2022

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: set_camera_control_status.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class EnumCameraControlStatus(betterproto.Enum):
    CAMERA_IDLE = 0
    CAMERA_CONTROL = 1
    CAMERA_EXTERNAL_CONTROL = 2


@dataclass
class RequestSetCameraControlStatus(betterproto.Message):
    camera_control_status: "EnumCameraControlStatus" = betterproto.enum_field(1)
