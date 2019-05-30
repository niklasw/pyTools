

# Lägg märke till {{keyword}} nedan. Dessa är parametrar
# i Jinja2.Temlate

template='''
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Bildkarusellen</title>
  <meta name="description" content="Bildkarusellen">
  <meta name="author" content="SitePoint">

  <link rel= "stylesheet" type="text/css" href="{{css}}">

</head>
<script>
function goLeft()
{
    var x = event.which || event.keyCode;
    if (x == 108)
    {
        document.getElementById("left").submit();
    }
    if (x == 114)
    {
        document.getElementById("right").submit();
    }
        
}
</script>
<body onkeypress="goLeft()">

<h1>Rotate with flask</h1>
<p> Now with javascript navigation: Press "r" or "l"</p>
<div id="content">

    <div id="pane">
        <img class="limg" src="{{prevImage}}" alt="{{prevImage}}"/>
        <img class="cimg" src="{{image}}"     alt="{{image}}"/>
        <img class="rimg" src="{{nextImage}}" alt="{{nextImage}}"/>
    </div>
    
    <div id="forms">
        <form id="left" action="/backward/" method="post">
            <button  class="lbut" name="previousButton" type="submit">Left</button>
        </form>
        
        <form id="right" action="/forward/" method="post">
            <button  class="rbut" name="previousButton" type="submit">Right</button>
        </form>
    </div>
</div>
</body>

</html>
'''
