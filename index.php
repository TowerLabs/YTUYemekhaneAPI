<?php

$token = $_GET['token'];

$response = array();

if(isset($token) && !empty($token) && 'token' == $token){

	$filename = "example.json";
	
	$handle = fopen($filename, "r");
	
	$contents = fread($handle, filesize($filename));

	fclose($handle);

	$response['err'] = 0;

	$response['data'] = $contents;

	$response['msg'] = 'Here you go';

}else{
	$response['err'] = 1;

	$response['msg'] = 'Token is required';
}

header('Content-type: application/json');

echo json_encode($response);exit;

?>