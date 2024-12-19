import os
import pathlib
import importlib.util
import sys


parent_plugin = pathlib.Path(os.getenv("DAGSTER_PLUGIN_BASE_DIR")) / 'plugin_nuke.py'


spec = importlib.util.spec_from_file_location(str(parent_plugin.parent).replace(os.sep, '.'), parent_plugin)
module_from_spec = importlib.util.module_from_spec(spec)
sys.modules[str(parent_plugin.parent).replace(os.sep, '.')] = module_from_spec
spec.loader.exec_module(module_from_spec)
plugin = module_from_spec.plugin


plugin['submitter']['executable'] = '/nfs/rez-packages/wrappers/nuke-15.0v4'
