import os
import pathlib
import importlib.util
import sys


parent =  # pathlib.Path(os.getenv("DAGSTER_JOB_BASE_DIR")) / 'job_template.py'
# parent = pathlib.Path("/opt/dagster/repos/deadline-dagster/tests/test_assets/fixtures/jobs/job_template.py")


spec = importlib.util.spec_from_file_location(str(parent.parent).replace(os.sep, '.'), parent)
module_from_spec = importlib.util.module_from_spec(spec)
sys.modules[str(parent.parent).replace(os.sep, '.')] = module_from_spec
spec.loader.exec_module(module_from_spec)
job = module_from_spec.job


job['job_file'] = '/nfs/projects/tests/blender/2023-11-13_EskofBubble/ColoredBubble_013.blend'
job['plugin_file'] =  # f'{os.getenv("DAGSTER_PLUGIN_BASE_DIR")}/plugin_blender.py'
job['kitsu_task'] = 'dae34b5a-efff-4cd9-a7e9-3e69fd4ef1bd'
job['append_draft_job_png'] = True
job['append_draft_job_mov'] = True
job['with_kitsu_publish'] = True
job['deadline_job_with_draft'] = True
job['render_engine'] = 'CYCLES'
job['comment'] = 'SQ010_SH030'
job['frame_start'] = 1001
job['frame_end'] = 1300
