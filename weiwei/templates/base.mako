<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="${request.matching.reverse('weiwei:static', path=['css', 'bootstrap.css'])}" rel="stylesheet" />
    <link href="${request.matching.reverse('weiwei:static', path=['css', 'weiwei.css'])}" rel="stylesheet" />
    <title><%block name="title" /></title>
</head>
<body>
<div class="container">
    <div class="btn-group editor_panel">
        <a href="?edit" class="btn btn-default"><span class="glyphicon glyphicon-edit"></span> edit</a>
    </div>
    <%block name="content">
        <h1 class="page-header"><%block name="page_header" /></h1>
    </%block>
</div>
</body>
</html>
