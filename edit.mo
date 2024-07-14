<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

</style>
</head>

<body>
<h1>Add image</h1>
<form action="/flowers/image_CREATE.cgi" method="POST" enctype="multipart/form-data">
  Photo: <input type="file" name="photo">
  <br>
  <input type="submit" name="submit" value="UPLOAD!">
</form>

<h1>Remove image</h1>
<form action="/flowers/image_DELETE.cgi" method="POST" onsubmit="return confirm('Are you sure you want to delete this image FOREVER?');">
  {{#IMAGES}}
    <input type="radio" id="{{.}}" name="photo" value="{{.}}">
    <label for="{{.}}">{{.}}</label>
    <img width=30 height=30 src={{.}}>
    <br>
  {{/IMAGES}}
  <input type="submit" name="submit" value="DELETE!">
</form>

</body>
