<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>Change password</title>
		<meta charset="utf-8" />
	</head>

	<body>

		<form action="/change_password" method="post">
			<p><label for="nickname">Nickname:</label></p>
				<input name="nickname" type="text"/></p>
			<p><label for="old_password">Old password:</label></p>
				<input name="old_password" type="password"/></p>
			<p><label for="new_password">New password:</label></p>
				<input name="new_password" type="password"/></p>
			<p><input type="submit" value="Change password"/></p>
		</form>
			
	</body>
	
</html>