<%inherit file="base.mako" />
<%block name="title">${page_title}</%block>
<%block name="page_header">${page_title}</%block>
<%block name="content">
    ${parent.content()}
    ${form|n}
</%block>

