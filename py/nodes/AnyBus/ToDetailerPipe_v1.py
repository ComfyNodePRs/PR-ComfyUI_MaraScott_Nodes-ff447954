#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
###
#
# Bus.  Converts X connectors into one, and back again.  You can provide a bus as input
#       or the X separate inputs, or a combination.  If you provide a bus input and a separate
#       input (e.g. a model), the model will take precedence.
#
#       The term 'bus' comes from computer hardware, see https://en.wikipedia.org/wiki/Bus_(computing)
#       Largely inspired by Was Node Suite - Bus Node 
#
###

from ...inc.nodes import Configuration as _CONF
from ...inc.profiles.any import Node as ProfileNodeAny
from ...inc.profiles.pipe_basic import Node as ProfileNodePipeBasic
# from ..inc.profiles.pipe_detailer import Node as ProfileNodePipeDetailer

from ...utils.log import *

class ToDetailerPipe_v1:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "hidden": {"id":"UNIQUE_ID"},
            "required":{
                "bus": ("BUS",),
            },
            "optional": {
            }
        }

    RETURN_TYPES = (
        ("DETAILER_PIPE", ) 
    )
    
    RETURN_NAMES = (
        ("detailer_pipe", )
    )
    
    OUTPUT_NODE = _CONF.OUTPUT_NODE
    CATEGORY = _CONF.CATEGORY
    DESCRIPTION = "An \"ANY\" Bus Node to Basic Pipe"
    FUNCTION = "fn"
    
    def fn(self, **kwargs):
        # Initialize the bus tuple with None values for each parameter
        bus = kwargs.get('bus', (None,) * len(ProfileNodeAny.INPUT_NAMES))
        # if len(bus) != len(ProfileNodeAny.INPUT_NAMES):
        #     raise ValueError("The 'bus' tuple must have the same number of elements as 'ProfileNodeAny.INPUT_NAMES'")
        
        # outputs = {}
        # for name, bus_value in zip(ProfileNodeAny.INPUT_NAMES[:5], bus[:5]):
        #     _input = _CONF.get_kwarg_with_prefix(kwargs, name, bus_value)
        #     outputs[name] = _CONF.determine_output_value(name, _input, bus_value)
        # _CONF.handle_special_parameters(outputs)

        # # Prepare and return the output bus tuple with updated values
        # out_bus_values = tuple((None, outputs[name]) for name in ProfileNodeAny.INPUT_NAMES[:5])
        # out_bus_names = tuple((name, None) for name in ProfileNodePipeBasic.INPUT_NAMES[:5])
        # out_pipe = tuple(out_value for (out_name, _), (_, out_value) in zip(out_bus_names, out_bus_values))        

        # if len(out_pipe) != len(ProfileNodePipeBasic.INPUT_NAMES):
        #     raise ValueError("The 'pipe' tuple must have the same number of elements as 'ProfileNodePipeBasic.INPUT_NAMES'")

        return ( bus[:14], )
