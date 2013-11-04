from docutils.core import publish_parts


def rst_renderer(markup):
    defaults = {'file_insertion_enabled': 0,
                'raw_enabled': 0,
                'input_encoding': 'utf-8',
                'output_encoding': 'utf-8',
                '_disable_config': 1}
    return publish_parts(markup, writer_name='html',
                         settings_overrides=defaults)['html_body']
