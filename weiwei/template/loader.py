import kajiki

package_template_loader = None


def get_loader():
    return package_template_loader


def setup_template_loader():
    global package_template_loader
    package_template_loader = kajiki.PackageLoader()
