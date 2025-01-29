from Deadline.deadline_templates.jobs.job_base import job
from Deadline.deadline_templates.plugins.nuke.plugin_nuke_base import plugin


# Overrides
job['chunk_size'] = 10
job['plugin_dict'] = plugin
# job['plugin_file'] =  # f'{os.getenv("DAGSTER_PLUGIN_BASE_DIR")}/plugin_nuke.py'

# Plugin specific k/v
job['write_nodes'] = ['write_farm']
