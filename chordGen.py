#!C:/Users/hp/AppData/Local/Programs/Python/Python39/python.exe
import cgi,cgitb
from scaleGenarator import ScaleGenarator
from chordsGenarator import ChordsGenarator


cgitb.enable()
data = cgi.FieldStorage()

key = data.getvalue('key')
scale = data.getvalue('scale')
scalegentor = ScaleGenarator(key,scale)
print("Content-Type: text/html\n")
notesList = scalegentor.scaleGen()

chordgenror = ChordsGenarator(scale,notesList)
chordsList = chordgenror.genChords()

print(''' <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChordGenarator</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
</head> ''')

print('<body>')
print('<div class="container-fluid">')
print('<div class="row text-box">')
print('<h1 class="header-text">'+key +' '+scale+' Scale Chords</h1>')
print('</div>')
print('<div class="form-box">')
print('<h2 class="header-text">'+str(chordsList)+'</h2>')
print('</div>')
print('<div class="btn-box">')
print('<a class="btn btn-primary" href="./index.html" role="button">Back</a>')
print('</div>')
print('</div>')
print('</body>')