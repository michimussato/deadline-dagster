from Deadline.deadline_templates.jobs.job_base import job
from Deadline.deadline_templates.plugins.blender.plugin_blender_base import plugin


job['job_file'] = '/nfs/projects/Sandbox/2022-12-14_ConnectPoints/Connect_Points_004.blend'
job['plugin_dict'] = plugin
# job['plugin_file'] =  # f'{os.getenv("DAGSTER_PLUGIN_BASE_DIR")}/plugin_blender.py'
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
