<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>users by country mr</title>
		<meta charset="utf-8" />
	</head>

	<body>	
	 
		<table>
			<tr>
				<td><strong>País</strong></td>
				<td><strong>Num. Usuarios</strong></td>
			</tr>
		
			% for result in results:
				<tr>
					<td>{{result["_id"]}}</td>
					<td>{{result["value"]["count"]}}</td>
				</tr>
			% end

	</body>
	
</html>