from django import template

register = template.Library()


def build_tree(tree):
    markup = "<ul>"
    for entry in tree:
        markup += "<li>"
        if isinstance(tree[entry], dict):
            markup += "<strong>{}</strong>".format(entry)
            markup += build_tree(tree[entry])
        else:
            markup += "<a href='#'>{}</a>".format(entry)
        markup += "</li>"
    markup += "</ul>"
    return markup


@register.simple_tag
def source_tree(tree):
    return build_tree(tree)
