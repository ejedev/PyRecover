<?php  session_start(); ?>
<?php
if(!isset($_SESSION['role']))
       {
           header("Location:login.php");
       }
?>
<html>
	<header>
		<link rel="stylesheet" href="style.css">
	</header>
	<body>
		<center>
		<img id='logo' src='logo.png'>
		<br>
		<form action="logout.php" method="POST">
		<input type="submit" value="Log out" style="width:20%;height:30;" />
		<br>
		</form>
		<table id = 'table'>
			<tr>
				<th><strong>Site</strong></th>
				<th><strong>Username</strong></th>
				<th><strong>Password</strong></th>
			</tr>
				<?php
				$url = 'data.json';
				$data = file_get_contents($url);
				$characters = json_decode($data);
				foreach ($characters as $character) {
					echo '<tr>';
					echo '<td>' . $character->url . '</td>';
					echo '<td>' . $character->username . '</td>';
					echo '<td>' . $character->password . '</td>';
					echo '</tr>';
				}
				 ?>
		</center>
		</table>
	</body>
</html>
