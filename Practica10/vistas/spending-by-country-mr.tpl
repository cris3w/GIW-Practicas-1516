<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>spending by country mr</title>
		<meta charset="utf-8" />
	</head>

	<body>	
	 
		<table>
			<tr>
				<td><strong>País</strong></td>
				<td><strong>Total gastos</strong></td>
			</tr>
		
			% for result in results:
				<tr>
					<td>{{result["_id"]}}</td>
					<td>{{result["value"]["count"]}}</td>
				</tr>
			% end

	</body>
	
</html>