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


plugin['submitter']['render_engines'] = ['CYCLES', 'BLENDER_EEVEE', 'WORKBENCH']

plugin['submitter']['args'].append('--background')
plugin['submitter']['args'].append('<QUOTE>"{job_file}"<QUOTE>')
plugin['submitter']['args'].extend(['--render-output', '<QUOTE>"{render_output}"<QUOTE>'])
plugin['submitter']['args'].extend(['--render-format', '{output_format}'])
plugin['submitter']['args'].extend(['--engine', '{render_engine}'])
plugin['submitter']['args'].extend(['--frame-start', '<STARTFRAME>'])
plugin['submitter']['args'].extend(['--frame-end', '<ENDFRAME>'])
plugin['submitter']['args'].extend(['--threads', '0'])
plugin['submitter']['args'].append('--render-anim')
