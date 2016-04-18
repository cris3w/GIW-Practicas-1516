<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>Add</title>
		<meta charset="utf-8" />
	</head>

	<body>
	
		<form action="/add_user" method="post">
			<p><label for="_id">ID:</label></p>
	        	<input name="_id" type="text"/></p>
			<p><label for="country">Country:</label></p>
	        	<input name="country" type="text"/></p>
			<p><label for="zip">Zip:</label></p>
	        	<input name="zip" type="number"/></p>
			<p><label for="email">Email:</label></p>
	        	<input name="email" type="email"/></p>
	        <p><label for="gender">Gender:</label></p>
	        	<input name="gender" type="text"/></p>
	        <p><label for="likes">Likes:</label></p>
	        	<input name="likes" type="text"/></p>
	        <p><label for="password">Password:</label></p>
	        	<input name="password" type="password"/></p>
	        <p><label for="year">Year:</label></p>
	        	<input name="year" type="number"/></p>
			<p><input type="submit" value="Add"/></p>
		</form>
			
	</body>
	
</html>