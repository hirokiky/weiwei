import colander
from deform.widget import TextAreaWidget


class Page(colander.MappingSchema):
    title = colander.SchemaNode(colander.String(),
                                validator=colander.Length(max=255))
    text = colander.SchemaNode(colander.String(),
                               widget=TextAreaWidget())
