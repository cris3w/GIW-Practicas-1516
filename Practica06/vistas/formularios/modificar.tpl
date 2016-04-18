<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>Modificar</title>
		<meta charset="utf-8" />
	</head>

	<body>

		<form action="/modificar/{{titulo}}" method="post">
			<p><label for="titulo">Titulo: {{titulo}}</label></p>
				<input name="titulo" type="text"/></p>
			<p><label for="autor">Autor: {{autor}}</label></p>
				<input name="autor" type="text"/></p>
			<p><label for="genero">Genero: {{genero}}</label></p>
				<input name="genero" type="text"/></p>
			<p><input type="submit" value="Modificar"/></p>
		</form>
			
	</body>
	
</html>