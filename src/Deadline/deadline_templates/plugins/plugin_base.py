args = list()

plugin = {
    'submitter':
    {
        'executable': None,
        'output_formats_plugin': ['png', 'exr', 'jpg'],
        'args': args,
        'padding_deadline': "'#' * constants.PADDING",  # results in "####"
        'padding_command': "'#' * constants.PADDING",   # results in "####"
    }
}
