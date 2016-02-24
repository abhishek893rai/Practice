import urllib.request, urllib.parse
data = {
's':'basics',
'submit':'search'
}
data = bytes( urllib.parse.urlencode( data ).encode() )
handler = urllib.request.urlopen( 'http://www.pythonprogramming.net', data );
print( handler.read().decode( 'utf-8' ) );

