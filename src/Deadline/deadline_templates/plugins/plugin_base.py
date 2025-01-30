args = list()

plugin = {
    'submitter':
    {
        'executable': None,
        'output_formats_plugin': ['png', 'exr', 'jpg'],
        'args': args,
        'padding_deadline': "'#' * Deadline.deadline_dagster.settings.constants.PADDING",  # results in "####"
        'padding_command': "'#' * Deadline.deadline_dagster.settings.constants.PADDING",   # results in "####"
    }
}
