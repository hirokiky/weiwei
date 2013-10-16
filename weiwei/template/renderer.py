from weiwei.template.loader import get_loader


def renderer_factory(path):
    loader = get_loader()
    template = loader.import_(path)

    def template_renderer(context):
        return template(context).render()

    return template_renderer


def using_template(template_path):
    def wrapper(view_callable):
        def _wrapped(request, *args, **kwargs):
            renderer = renderer_factory(template_path)
            res = view_callable(request, *args, **kwargs)
            if isinstance(res, dict):
                res['request'] = request
                return renderer(res)
            else:
                return res
        return _wrapped
    return wrapper
