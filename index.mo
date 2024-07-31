<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}
html, body {
  margin: 0;
  padding: 0;
}
body {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
img {
  max-width: 90vw;
  max-height: 40rem;
}
.images {
  width: 100%;
  max-width: 20rem;
  display: flex;
  flex-wrap: wrap;
}
.images > * {
  flex: 0 0 auto;
}
.images a {
  display: block;
  text-align: center;
  text-decoration: none;
  background: grey;
  margin: 1rem;
  min-height: 3rem;
  line-height: 3rem;
  min-width: 3rem;
}
</style>
</head>

<body>
<section class="images">
  {{#IMAGES}}
    <a href={{.}}>
      📷
    </a>
  {{/IMAGES}}
</section>
<footer>
<a class="edit-link" href="/flowers/edit.cgi">edit website</a>
.
<a href="https://github.com/alifeee/flowers-website">source</a>
</footer>
</body>
