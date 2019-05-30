

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

<h1>Rotate with flask</h1>
<div id="content">

    <div id="pane">
        <img class="limg" src="{{prevImage}}" alt="{{prevImage}}"/>
        <img class="cimg" src="{{image}}"     alt="{{image}}"/>
        <img class="rimg" src="{{nextImage}}" alt="{{nextImage}}"/>
    </div>
    
    <div id="forms">
        <form action="/backward/" method="post">
            <button  class="lbut" name="previousButton" type="submit">Left</button>
        </form>
        
        <form action="/forward/" method="post">
            <button  class="rbut" name="previousButton" type="submit">Right</button>
        </form>
    </div>

</div>

</html>
'''
