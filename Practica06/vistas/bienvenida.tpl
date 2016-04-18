<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>Bienvenid@</title>
		<meta charset="utf-8" />
	</head>

	<body>

		<h1> Bienvenid@ {{nombre}} </strong><h1>
		<h3><a href="/personales">Modificar datos personales</a><h3>
		
		</ul>
			<li>
				<form action='/nueva'>
					<p><input type="submit" value="Nueva"/><p>
				</form>
				<form action='/listar'>
					<p><input type="submit" value="Listar"/><p>
				</form>
				<form action='/buscar'>
					<p><input type="submit" value="Buscar"/><p>
				</form>
				<form action='/eliminar'>
					<p><input type="submit" value="Eliminar"/><p>
				</form>
				<form action='/modificar'>
					<p><input type="submit" value="Modificar"/><p>
				</form>
			</li>
		</ul>
		
	</body>
	
</html>