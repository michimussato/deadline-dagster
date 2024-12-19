import os
import pathlib
import importlib.util
import sys


parent = pathlib.Path(os.getenv("DAGSTER_PLUGIN_BASE_DIR")) / 'plugin_template.py'


spec = importlib.util.spec_from_file_location(str(parent.parent).replace(os.sep, '.'), parent)
module_from_spec = importlib.util.module_from_spec(spec)
sys.modules[str(parent.parent).replace(os.sep, '.')] = module_from_spec
spec.loader.exec_module(module_from_spec)
plugin = module_from_spec.plugin


plugin['submitter']['padding_command'] = "'\\$F' + str(constants.PADDING)"  # results in "$F4"
plugin['submitter']['args'].append('/nfs/deadline/DeadlineRepository10/plugins/Houdini/hrender_dl.py')
plugin['submitter']['args'].append('-e')
plugin['submitter']['args'].extend(['-f', '<STARTFRAME> <ENDFRAME> {chunk_size}'])
plugin['submitter']['args'].extend(['-d', '{rop}'])
plugin['submitter']['args'].extend(['-o', '<QUOTE>{render_output}<QUOTE>'])
plugin['submitter']['args'].append('<QUOTE>{job_file}<QUOTE>')
