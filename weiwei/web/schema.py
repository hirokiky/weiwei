import colander
from deform.widget import TextAreaWidget


class PageText(colander.MappingSchema):
    text = colander.SchemaNode(colander.String(),
                               widget=TextAreaWidget())


class PageTitle(colander.MappingSchema):
    title = colander.SchemaNode(colander.String(),
                                validator=colander.Length(max=255),
                                missing='')
