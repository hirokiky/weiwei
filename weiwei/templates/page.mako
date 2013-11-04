<%inherit file="base.mako" />
<%block name="title">${page.title}</%block>
<%block name="page_header">${page.title}</%block>
<%block name="content">
    ${parent.content()}
    ${page.markuped_text|n}
</%block>
