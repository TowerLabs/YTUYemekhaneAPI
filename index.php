<?php

$token = $_GET['token'];

$response = array();

header('Content-Type: application/json');

error_reporting(0);

if(isset($token) && !empty($token) && 'token' == $token){

	$filename = "example.json";
	
	$handle = fopen($filename, "r");
	
	$contents = fread($handle, filesize($filename));

	fclose($handle);

	echo json_encode(json_decode($contents),JSON_PRETTY_PRINT);

}else{
	$response['err'] = 1;

	$response['msg'] = 'Token is required';
	echo json_encode($response,JSON_PRETTY_PRINT);

}
exit;
?>