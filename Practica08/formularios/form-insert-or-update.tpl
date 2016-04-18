<!DOCTYPE html>
<html lang='es'>

	<head>
		<title>Insert or Update</title>
		<meta charset="utf-8" />
	</head>

	<body>
	
		<form action="/insert_or_update" method="post">
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
			<p><input type="submit" value="Insert or Update"/></p>
		</form>
			
	</body>
	
</html>