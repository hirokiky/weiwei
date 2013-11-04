<%inherit file="base.mako" />
<%block name="title">not found</%block>
<%block name="page_header">not found</%block>
<%block name="content">
    ${parent.content()}
    <a href="?edit">edit</a>
</%block>
