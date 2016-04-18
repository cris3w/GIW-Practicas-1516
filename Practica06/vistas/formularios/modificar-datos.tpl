<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>Modificar datos</title>
		<meta charset="utf-8" />
	</head>

	<body>
		
		<form action="/personales" method="post">
			<p><label for="nombre">Nombre: {{nombre}}</label></p>
				<input name="nombre" type="text"/></p>
			<p><label for="apellido">Apellido: {{apellido}}</label></p>
				<input name="apellido" type="text"/></p>
			<p><label for="usuario">Usuario: {{usuario}}</label></p>
				<input name="usuario" type="text"/></p>
			<p><label for="password">Password:</label></p>
				<input name="password" type="password"/></p>
			<p><input type="submit" value="Modificar"/></p>
		</form>
			
	</body>
	
</html>