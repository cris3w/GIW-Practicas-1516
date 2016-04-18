<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>Log in</title>
		<meta charset="utf-8" />
	</head>

	<body>

		<form action="/login_totp" method="post">
			<p><label for="nickname">Nickname:</label></p>
				<input name="nickname" type="text"/></p>
			<p><label for="password">Password:</label></p>
				<input name="password" type="password"/></p>
			<p><label for="totp">Totp:</label></p>
				<input name="totp" type="text"/></p>
			<p><input type="submit" value="Log in"/></p>
		</form>
			
	</body>

</html>