import os
import pathlib
import importlib.util
import sys


parent = None # pathlib.Path(os.getenv("DAGSTER_JOB_BASE_DIR")) / 'job_template.py'
# parent = pathlib.Path("/opt/dagster/repos/deadline-dagster/tests/test_assets/fixtures/jobs/job_template.py")


spec = importlib.util.spec_from_file_location(str(parent.parent).replace(os.sep, '.'), parent)
module_from_spec = importlib.util.module_from_spec(spec)
sys.modules[str(parent.parent).replace(os.sep, '.')] = module_from_spec
spec.loader.exec_module(module_from_spec)
job = module_from_spec.job


job['job_file'] = '/nfs/projects/Sandbox/2022-12-14_ConnectPoints/Connect_Points_004.blend'
job['plugin_file'] = None # f'{os.getenv("DAGSTER_PLUGIN_BASE_DIR")}/plugin_blender.py'
# job['plugin_file'] = f'/opt/dagster/repos/deadline-dagster/tests/test_assets/fixtures/jobs/plugin_blender.py'
job['kitsu_task'] = '1cd5dd8b-c727-41b1-a88c-ba3a3fbc562a'
job['append_draft_job_png'] = True
job['append_draft_job_mov'] = True
job['with_kitsu_publish'] = True
job['deadline_job_with_draft'] = True
job['render_engine'] = 'CYCLES'
job['comment'] = 'SQ010_SH010'
job['frame_start'] = 1001
job['frame_end'] = 1200
