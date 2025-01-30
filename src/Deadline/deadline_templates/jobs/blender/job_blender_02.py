from Deadline.deadline_templates.jobs.blender.job_blender import job
from Deadline.deadline_templates.plugins.blender.plugin_blender__4_1_1 import plugin


# http://michimussato-fuji.nord/productions/6c5dfed4-0f11-48f7-aba2-4d4d5cce85fc/shots/tasks/9bb09bfa-0a97-40c6-a6e6-27405b198570


job['job_file'] = '/nfs/AWSPortalRoot1/fixtures/blender/sh030_001.blend'
job['plugin_dict'] = plugin
# job['plugin_file'] = f'{os.getenv("PLUGIN_BASE_DIR")}/plugin_blender__4.1.1.py'
job['kitsu_task'] = 'ca153978-9ed2-4d3b-8f54-22584099490a'  # SQ020 / SQ020_SH030  Layout  http://miniboss/productions/6c5dfed4-0f11-48f7-aba2-4d4d5cce85fc/shots/tasks/ca153978-9ed2-4d3b-8f54-22584099490a
job['append_draft_job_png'] = True
job['append_draft_job_mov'] = True
job['with_kitsu_publish'] = True
job['deadline_job_with_draft'] = True
job['render_engine'] = 'CYCLES'
job['comment'] = 'This is Bender job comment'
job['frame_start'] = 1201
job['frame_end'] = 1250
