<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>Lista de peliculas</title>
		<meta charset="utf-8" />
	</head>

	<body>

		<header>
			<h1>Peliculas</h1>
		<header>
		
		<ul>
			% for pelicula in lista:
				<li> {{pelicula}} </li>
			% end
		</ul>
		
		<a href="/principal">Volver</a>

	</body>
	
</html>