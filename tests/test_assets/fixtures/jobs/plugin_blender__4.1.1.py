import os
import pathlib
import importlib.util
import sys


parent =  # pathlib.Path(os.getenv("DAGSTER_PLUGIN_BASE_DIR")) / 'plugin_blender.py'
# parent = pathlib.Path("/opt/dagster/repos/deadline-dagster/tests/test_assets/fixtures/jobs/plugin_blender.py")


spec = importlib.util.spec_from_file_location(str(parent.parent).replace(os.sep, '.'), parent)
module_from_spec = importlib.util.module_from_spec(spec)
sys.modules[str(parent.parent).replace(os.sep, '.')] = module_from_spec
spec.loader.exec_module(module_from_spec)
plugin = module_from_spec.plugin


plugin['submitter']['executable'] = '/nfs/rez-packages/wrappers/blender-4.1.1'
