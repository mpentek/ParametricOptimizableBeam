'''
Copyright and license disclosure:
a partial replica of https://github.com/KratosMultiphysics/Kratos/blob/master/applications/CoSimulationApplication/custom_data_structure/pyKratos/Parameters.py
'''

import json


def validate_and_assign_defaults(defaults, settings, recursive=False):
    for key, val in settings.items():
        # check if the current entry also exists in the defaults
        if not key in defaults.keys():
            err_msg = 'The item with name "' + key + '" is present in this '
            err_msg += 'settings\nbut NOT in the defaults!\n'
            err_msg += 'settings are:\n'
            err_msg += json.dumps(settings, indent=4)
            err_msg += '\ndefaults are:\n'
            err_msg += json.dumps(defaults, indent=4)
            raise Exception(err_msg)

        # check if the type is the same in the defaults
        if type(settings[key]) != type(defaults[key]):
            err_msg = 'The type of the item with name "' + key + '" (type: "'
            err_msg += str(type(settings[key]).__name__)+'") in this '
            err_msg += 'settings\nis NOT the same as in the defaults (type: "'
            err_msg += str(type(defaults[key]).__name__)+'")!\n'
            err_msg += 'settings are:\n'
            err_msg += json.dumps(settings, indent=4)
            err_msg += '\ndefaults are:\n'
            err_msg += json.dumps(defaults, indent=4)
            raise Exception(err_msg)

    # loop the defaults and add the missing entries
    for key_d, val_d in defaults.items():
        if key_d not in settings:  # add the default in case the setting is not present
            settings[key_d] = val_d
        elif recursive and type(val_d) is dict:
            recursively_validate_and_assign_defaults(val_d, settings[key_d])


def recursively_validate_and_assign_defaults(defaults, settings):
    validate_and_assign_defaults(defaults, settings, recursive=True)
