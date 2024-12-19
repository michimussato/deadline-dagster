import os
import pathlib
import importlib.util
import sys


parent = pathlib.Path(os.getenv("DAGSTER_JOB_BASE_DIR")) / 'job_template.py'


spec = importlib.util.spec_from_file_location(str(parent.parent).replace(os.sep, '.'), parent)
module_from_spec = importlib.util.module_from_spec(spec)
sys.modules[str(parent.parent).replace(os.sep, '.')] = module_from_spec
spec.loader.exec_module(module_from_spec)
job = module_from_spec.job


# Overrides
job['chunk_size'] = 10
job['plugin_file'] = f'{os.getenv("DAGSTER_PLUGIN_BASE_DIR")}/plugin_nuke.py'

# Plugin specific k/v
job['write_nodes'] = ['write_farm']
