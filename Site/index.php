<html>
	<header>
		<link rel="stylesheet" href="style.css">
	</header>
	<body>
		<center>
		<img id='logo' src='logo.png'>
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