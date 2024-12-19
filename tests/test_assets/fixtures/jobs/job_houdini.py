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


job['job_file'] = '/nfs/AWSPortalRoot1/fixtures/houdini/project/vivi_025.hip'
job['plugin_file'] = f'{os.getenv("DAGSTER_PLUGIN_BASE_DIR")}/plugin_houdini__19.5.805.py'
job['kitsu_task'] = '9890944f-fe39-4408-baf3-bcd34dc9807d'  # SQ010 / SQ010_SH020  Layout  http://miniboss/productions/6c5dfed4-0f11-48f7-aba2-4d4d5cce85fc/shots/tasks/9890944f-fe39-4408-baf3-bcd34dc9807d
job['append_draft_job_png'] = True
job['append_draft_job_mov'] = True
job['with_kitsu_publish'] = True
job['deadline_job_with_draft'] = True
job['comment'] = 'This is Houdini job comment'
job['frame_start'] = 1001
job['frame_end'] = 1020
job['rop'] = '/stage/usdrender_rop_camera2'
