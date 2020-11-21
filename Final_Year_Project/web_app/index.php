<?php
session_start();
if(!isset($_SESSION["username"])){
header("Location: login.php");
exit(); }
?>
<html>
<head>
<style>
table
{
border-style:solid;
border-width:2px;
border-color:red;
}
</style>
</head>
<body bgcolor="#EEFDE">
<h1><p>Welcome <?php printf($_SESSION["username"]) ?></p><h1>
  <h4><?php
  require('db.php');
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }
  $sql = "SELECT * FROM RC";
  echo '<table border="1" cellspacing="2" cellpadding="2">
      <tr>
          <th> <font face="Arial">Name</font> </td>
          <th> <font face="Arial">Vehicle_Name</font> </td>
          <th> <font face="Arial">Regestration_no</font> </td>
          <th> <font face="Arial">Date</font> </td>
          <th> <font face="Arial">Time</font> </td>
      </tr>';
  $result = $con->query($sql);
  if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
          $Name = $row["Name"];
          $Vehicle_Name = $row["Vehicle_name"];
          $Regestration_no = $row["Regestration_no"];
          $Date = $row["Date"];
          $Time = $row["Time"];

          echo '<tr>
                    <td>'.$Name.'</td>
                    <td>'.$Vehicle_Name.'</td>
                    <td>'.$Regestration_no.'</td>
                    <td>'.$Date.'</td>
                    <td>'.$Time.'</td>
                </tr>';
      }
      $result->free();
  }
  $con->close();
  ?><h4>
</html>
