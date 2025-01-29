from Deadline.deadline_templates.jobs.job_base import job
from Deadline.deadline_templates.plugins.blender.plugin_blender_base import plugin


job['job_file'] = '/nfs/projects/tests/blender/2023-11-13_EskofBubble/ColoredBubble_013.blend'
job['plugin_dict'] = plugin
# job['plugin_file'] =  # f'{os.getenv("DAGSTER_PLUGIN_BASE_DIR")}/plugin_blender.py'
job['kitsu_task'] = 'dae34b5a-efff-4cd9-a7e9-3e69fd4ef1bd'
job['append_draft_job_png'] = True
job['append_draft_job_mov'] = True
job['with_kitsu_publish'] = True
job['deadline_job_with_draft'] = True
job['render_engine'] = 'CYCLES'
job['comment'] = 'SQ010_SH030'
job['frame_start'] = 1001
job['frame_end'] = 1300
