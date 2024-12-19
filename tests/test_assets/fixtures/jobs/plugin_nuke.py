import os
import pathlib
import importlib.util
import sys


parent_plugin = pathlib.Path(os.getenv("DAGSTER_PLUGIN_BASE_DIR")) / 'plugin_template.py'
parent_job = pathlib.Path(os.getenv("DAGSTER_JOB_BASE_DIR")) / 'job_nuke.py'


spec = importlib.util.spec_from_file_location(str(parent_plugin.parent).replace(os.sep, '.'), parent_plugin)
module_from_spec = importlib.util.module_from_spec(spec)
sys.modules[str(parent_plugin.parent).replace(os.sep, '.')] = module_from_spec
spec.loader.exec_module(module_from_spec)
plugin = module_from_spec.plugin


spec = importlib.util.spec_from_file_location(str(parent_job.parent).replace(os.sep, '.'), parent_job)
module_from_spec = importlib.util.module_from_spec(spec)
sys.modules[str(parent_job.parent).replace(os.sep, '.')] = module_from_spec
spec.loader.exec_module(module_from_spec)
job = module_from_spec.job


# plugin['submitter']['type'] = 'NukeSubmitter'
plugin['submitter']['args'].append('--nukex')
plugin['submitter']['args'].append('-t')  # terminal only (no gui); if <script> is a .py file it will be executed
plugin['submitter']['args'].append('-f')  # render at full size (turns off proxy; use -p to force render at proxy)
if bool(job['write_nodes']):
    plugin['submitter']['args'].extend(['-X', f'{",".join(job["write_nodes"])}'])
plugin['submitter']['args'].extend(['-F', '<STARTFRAME>-<ENDFRAME>'])
plugin['submitter']['args'].append('-x')
plugin['submitter']['args'].append('<QUOTE>{job_file}<QUOTE>')

# --------------------------------------------------------------
# This next argument specifies the output of the write_farm node.
# Write nodes are able to take extra arguments i.e. like this:
# WriteNode.file: [argv 0]/write_farm/[argv 1].####.[argv 2] etc.
# So, [argv <index>]
# write_farm.file has "[argv 0]" as value (as of now),
# so the last argument of this args must be the full, absolute
# path of the final image.

# This allows to specify the output from commandline
# However, this needs a special Write Node that
# reads the sysargv to redirect the output

# If a write node is expecting an argument that was
# not specified, the error would look somehow
# like this:
# Missing command-line argument #2 for write_farm.file
plugin['submitter']['args'].append('<QUOTE>\\\"{render_output}\\\"<QUOTE>')
